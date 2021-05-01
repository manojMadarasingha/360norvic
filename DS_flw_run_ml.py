from sklearn.preprocessing import MinMaxScaler

import settings

import pandas as pd
import numpy as np

from sklearn.metrics import average_precision_score, recall_score
from xgboost.sklearn import XGBClassifier
from sklearn.metrics import accuracy_score

from sklearn.utils import shuffle



def run_xgboost_ml(df_train, df_test, platform_folder):
    target = 'Vid_type_mean'

    df_train.drop(['Vid_pltform_ML_mean'], axis=1, inplace=True)
    df_test.drop(['Vid_pltform_ML_mean'], axis=1, inplace=True)

    counts = np.asarray(df_train[target].value_counts())
    base_score = counts[1] / (counts[0] + counts[1])

    predictors = [x for x in df_train.columns if x not in [target]]

    x_train = df_train[predictors]
    y_train = df_train[target]
    x_test = df_test[predictors]
    y_test = df_test[target]

    # select mode features for xgboost
    ns, md, mcw, g, ss, csbt, sps, rl, ra = select_params_xgboost(platform_folder)
    xgboost_model = XGBClassifier(base_score=base_score,
                                  learning_rate=0.01,
                                  n_estimators=ns,
                                  max_depth=md,
                                  min_child_weight=mcw,
                                  gamma=g,
                                  subsample=ss,  # 0.9,
                                  colsample_bytree=csbt,  # 0.8,
                                  objective='binary:logistic',
                                  nthread=1,
                                  scale_pos_weight=sps,  # 2.0,
                                  reg_lambda=rl,
                                  reg_alpha=ra,
                                  seed=123)

    xgboost_model.fit(x_train, y_train, eval_metric='error')

    # get the performance
    y_pred = xgboost_model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    precsion = average_precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred, average='binary')

    # print('mean acc ' + platform_folder + ' ' + str(accuracy))

    return accuracy, precsion, recall

# based on the traffic_type (platform) select the classifier parameters.
def select_params_xgboost(platform):
    # ns,md, mcw, g, ss, csbt, sps, rl, ra

    if platform == 'yt':
        return [1000, 3, 2, 1, 0.6, 0.5, 1.0, 0.1, 0.1]

    elif platform == 'fb':
        return [1000, 7, 3, 1, 0.9, 0.6, 1.0, 0.1, 0.1]

    else:
        return [1000, 7, 2, 1, 0.8, 0.6, 1.0, 1, 0.1]

# split the data to train and test split based on the video id
def split_by_control_param(df, platform, random_seed):
    # read the NC data
    Sydney = 1
    Random = 0

    test_df = df[
        (df['location'] == Sydney)&
        (df['bandwidth'] == Random)&
        (df['Vid_pltform_mean'] == platform)]

    train_df = df[
        (df['location'] == Sydney)&
        (df['bandwidth'] == Random)&
        (df['Vid_pltform_mean'] == platform)]

    train_df_360 = train_df[train_df['Vid_type_mean'] == settings.V_360]
    train_df_normal = train_df[train_df['Vid_type_mean'] == settings.V_NORMAL]
    test_df_360 = test_df[test_df['Vid_type_mean'] == settings.V_360]
    test_df_normal = test_df[test_df['Vid_type_mean'] == settings.V_NORMAL]

    # take the vid numbers separaetely
    vid_numbers_360_test = np.unique(test_df_360['Vid_number_mean'].values)
    vid_numbers_normal_test = np.unique(test_df_normal['Vid_number_mean'].values)

    vid_numbers_360_train = np.unique(train_df_360['Vid_number_mean'].values)
    vid_numbers_normal_train = np.unique(train_df_normal['Vid_number_mean'].values)

    vid_numbers_360 = np.union1d(vid_numbers_360_test, vid_numbers_360_train)
    vid_numbers_normal = np.union1d(vid_numbers_normal_test, vid_numbers_normal_train)

    train_test_split_value = 5

    # randomly select the video ids to be in trian and test sets
    np.random.seed(random_seed)
    test_360_ind = list(
        np.random.choice(vid_numbers_360, len(vid_numbers_360) // train_test_split_value, replace=False))
    if len(test_360_ind) == 0:
        test_360_ind = [vid_numbers_360[0]]
    np.random.seed(random_seed)
    test_normal_ind = list(
        np.random.choice(vid_numbers_normal, len(vid_numbers_normal) // train_test_split_value, replace=False))
    if len(test_normal_ind) == 0:
        test_normal_ind = [vid_numbers_normal[0]]

    train_360_ind = list(set(vid_numbers_360) - set(test_360_ind))
    train_normal_ind = list(set(vid_numbers_normal) - set(test_normal_ind))

    train_df_360_new = train_df_360.loc[train_df_360['Vid_number_mean'].isin(list(train_360_ind))]
    train_df_normal_new = train_df_normal.loc[train_df_normal['Vid_number_mean'].isin(list(train_normal_ind))]

    test_df_360_new = test_df_360.loc[test_df_360['Vid_number_mean'].isin(list(test_360_ind))]
    test_df_normal_new = test_df_normal.loc[test_df_normal['Vid_number_mean'].isin(list(test_normal_ind))]

    # combine the 360 and normal video traces to train and test sets
    train_df_new = pd.concat([train_df_360_new, train_df_normal_new])
    train_df_new = shuffle(train_df_new, random_state=random_seed)
    test_df_new = pd.concat([test_df_360_new, test_df_normal_new])
    test_df_new = shuffle(test_df_new, random_state=random_seed)

    return train_df_new, test_df_new


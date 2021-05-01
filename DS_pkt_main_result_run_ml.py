import numpy as np
from xgboost.sklearn import XGBClassifier
from sklearn.utils import shuffle
import settings
import pandas as pd
import assign_control_condition
from sklearn.metrics import roc_curve, roc_auc_score, \
    average_precision_score, recall_score, accuracy_score


def run_xgboost(df_train, df_test, platform, iter):
    target = 'Vid_type'
    predictors = [x for x in df_train.columns if x not in [target]]

    x_train = df_train[predictors]
    y_train = df_train[target]
    x_test = df_test[predictors]
    y_test = df_test[target]

    # to assess only the first 20 features uncomment the line
    # x_train = select_top_20_features(df=x_train,
    #                                  platform=platform)
    # x_test = select_top_20_features(df=x_test,
    #                                 platform=platform)

    # initialize the XGBoost classifier.
    # classifier parameters were selected running RandomizedSearchCV operation in sklearn with CV=10
    xgboost_model = XGBClassifier(n_estimators=1000,
                                  max_depth=7,
                                  min_child_weight=1,
                                  gamma=0,
                                  objective='binary:logistic',
                                  subsample=0.6,
                                  colsample_bytree=0.6,
                                  reg_lambda=1,
                                  # reg_alpha=10,
                                  scale_pos_weight=1.0,
                                  verbosity=0)

    xgboost_model.fit(x_train, y_train)
    y_pred = xgboost_model.predict(x_test)

    # store the predictions for each trace with their corresponding traces
    accuracy = accuracy_score(y_test, y_pred)
    precsion = average_precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred, average='binary')

    # get the ROC data. ROC data not appeared in the research paper
    # predict probabilities
    model_probs = xgboost_model.predict_proba(x_test)
    # keep probabilities for the positive outcome only
    model_probs = model_probs[:, 1]
    # calculate scores
    model_auc = roc_auc_score(y_test, model_probs)

    # calculate roc curves
    model_fpr, model_tpr, _ = roc_curve(y_test, model_probs)

    roc_data = pd.DataFrame({'_fpr': model_fpr,
                             '_tpr': model_tpr,
                             '_auc': model_auc})

    print('Iteration: %.2f === Acc: %.2f  Prec: %.2f  Reca: %.2f ===' % (iter, accuracy, precsion, recall))

    return accuracy, precsion, recall, roc_data


# split the dataset
# non of the traces of the same video ID do not appear in both train and test datasets
def split_train_test(df, random_seed):
    np.random.seed(random_seed)
    all_videos = np.arange(0, 51, 1)
    test_ind = np.random.choice(all_videos, size=15, replace=False)

    train_ind = list(set(list(all_videos)) - set(list(test_ind)))

    train_df = df.loc[df['Vid_num'].isin(list(train_ind))]
    test_df = df.loc[df['Vid_num'].isin(list(test_ind))]

    Sydney = 1
    Random = 0

    train_df = train_df[
        (train_df['loc'] == Sydney) &
        (train_df['bandwidth'] == Random)]

    test_df = test_df[
        (test_df['loc'] == Sydney) &
        (test_df['bandwidth'] == Random)]

    if test_df.shape[0] == 0:
        test_ind = np.random.choice(train_ind, size=(len(train_ind)) // 4, replace=False)
        train_ind = list(set(list(all_videos)) - set(list(test_ind)))

        train_df.reset_index(inplace=True, drop=True)

        test_df = train_df.loc[train_df['Vid_num'].isin(list(test_ind))]
        train_df = train_df.loc[train_df['Vid_num'].isin(list(train_ind))]

    train_df = shuffle(train_df, random_state=random_seed)
    test_df = shuffle(test_df, random_state=random_seed)

    return train_df, test_df


# selec the top 20 features defined by the xgboost model
# selecting the top 20 features may slightly reduce the performance
def select_top_20_features(df, platform):
    # select the features according to the platform
    if platform == settings.PLATFORM_YT:
        features = YT_W_5s_1s
    elif platform == settings.PLATFORM_FB:
        features = FB_W_5s_1s
    else:
        features = BOTH_W_5s_1s

    df.reset_index(inplace=True, drop=True)

    final_df_val = df[features].values

    filtered_final_df = pd.DataFrame(data=final_df_val,
                                     columns=features)
    return filtered_final_df


# most important features as is seen by the model
YT_W_5s_1s = ['bytes_ip_dl_75%',
              'bytes_frame_dl_75%',
              'bytes_frame_dl_mean',
              'packet_size_std_dl_50%',
              'bytes_frame_dl_max',
              'bytes_frame_dl_std',
              'packet_size_std_dl_75%',
              'packet_size_mean_dl_50%',
              'bytes_ip_dl_max',
              'bytes_hdr_dl_max',
              'bytes_hdr_dl_std',
              'packet_size_mean_ul_std',
              'num_of_packets_dl_25%',
              'bytes_frame_dl_50%',
              'packet_size_std_dl_25%',
              'packet_size_std_dl_max',
              'packet_size_std_ul_mean',
              'packet_size_max_dl_mean',
              'bytes_frame_ul_min',
              'packet_size_max_ul_min',
              'packet_size_max_ul_mean',
              'packet_size_std_ul_min',
              'packet_size_max_ul_25%',
              'bytes_hdr_dl_50%',
              'packet_size_mean_ul_25%',
              'bytes_hdr_dl_mean',
              'bytes_hdr_dl_75%',
              'bytes_frame_ul_75%',
              'bytes_frame_dl_min',
              'packet_size_min_dl_50%']

FB_W_5s_1s = ['bytes_ip_dl_mean',
              'packet_size_std_ul_25%',
              'packet_size_std_ul_50%',
              'packet_size_mean_ul_25%',
              'bytes_ip_ul_mean',
              'bytes_ip_ul_std',
              'packet_size_std_ul_75%',
              'bytes_frame_ul_std',
              'bytes_frame_ul_max',
              'bytes_hdr_dl_25%',
              'bytes_ip_ul_max',
              'packet_size_mean_ul_50%',
              'packet_size_mean_dl_50%',
              'packet_size_std_dl_50%',
              'packet_size_mean_dl_max',
              'bytes_ip_ul_50%',
              'num_of_packets_ul_75%',
              'packet_size_std_ul_min',
              'bytes_frame_dl_std',
              'packet_size_max_ul_75%',
              'bytes_frame_ul_75%',
              'packet_size_mean_ul_75%',
              'packet_size_min_dl_max',
              'packet_size_max_ul_mean',
              'packet_size_min_dl_25%',
              'bytes_frame_dl_25%',
              'bytes_frame_dl_mean',
              'packet_size_max_ul_min',
              'bytes_frame_dl_max',
              'packet_size_mean_dl_25%',
              'num_of_packets_dl_max',
              'packet_size_max_ul_50%',
              'bytes_frame_ul_min',
              'bytes_frame_dl_50%',
              'bytes_hdr_ul_std',
              'bytes_hdr_ul_max',
              'packet_size_mean_ul_min',
              'packet_size_std_ul_max',
              'bytes_hdr_dl_std']

BOTH_W_5s_1s = ['packet_size_std_ul_min',
                'bytes_frame_dl_25%',
                'packet_size_std_ul_75%',
                'bytes_ip_dl_75%',
                'bytes_frame_ul_max',
                'packet_size_mean_dl_50%',
                'packet_size_std_dl_75%',
                'packet_size_mean_ul_25%',
                'num_of_packets_dl_75%',
                'packet_size_mean_dl_25%',
                'packet_size_mean_ul_min',
                'bytes_frame_dl_75%',
                'bytes_frame_dl_mean',
                'packet_size_mean_ul_50%',
                'packet_size_mean_dl_75%',
                'packet_size_max_ul_75%',
                'bytes_frame_ul_std',
                'bytes_ip_ul_max',
                'packet_size_std_ul_50%',
                'bytes_ip_ul_std',
                'num_of_packets_dl_50%',
                'packet_size_std_dl_50%',
                'packet_size_max_ul_mean',
                'packet_size_mean_dl_max',
                'bytes_hdr_dl_50%',
                'bytes_hdr_dl_max',
                'packet_size_max_ul_25%',
                'bytes_ip_dl_std',
                'packet_size_std_dl_max',
                'packet_size_min_dl_mean',
                'bytes_frame_ul_50%',
                'packet_size_mean_ul_mean',
                'num_of_packets_ul_std',
                'packet_size_min_ul_min',
                'packet_size_min_ul_75%',
                'packet_size_std_dl_25%',
                'packet_size_mean_ul_75%',
                'bytes_frame_dl_min',
                'bytes_frame_ul_25%',
                'packet_size_min_dl_25%']

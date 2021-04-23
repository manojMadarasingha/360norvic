import numpy as np
from xgboost.sklearn import XGBClassifier
import pandas as pd
from sklearn.metrics import average_precision_score, recall_score, accuracy_score

# run_xgboost_model
def run_xgboost(df_train, df_test, train_list, test_list):

    target = 'Vid_type'
    predictors = [x for x in df_train.columns if x not in [target]]

    x_train = df_train[predictors].values
    y_train = df_train[target].values
    x_test = df_test[predictors].values
    y_test = df_test[target].values

    # initialize the XGBoost classifier.
    xgboost_model = XGBClassifier(n_estimators=1000,
                                  max_depth=7,
                                  min_child_weight=1,
                                  gamma=0,
                                  objective='binary:logistic',
                                  subsample=0.6,
                                  colsample_bytree=0.6,
                                  reg_lambda=1,
                                  scale_pos_weight=1.0,
                                  verbosity=3)


    xgboost_model.fit(x_train, y_train)

    # print the accuracy considering all the test data: DS_pkt 5s bins
    y_pred = xgboost_model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    precsion = average_precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred, average='binary')

    print('Acc: %.2f  Prec: %.2f  Reca: %.2f' % (accuracy, precsion, recall))

    # get the train of bin for each video and store return df containning 115 bins with their loc, time and
    bins = np.arange(1, 116, 1).astype(str)
    bin_name = np.asarray(['bin_'] * 115)
    bin_cols = list(np.char.add(bin_name, bins))
    all_df = []

    y_pred_list = []
    y_gt_list = []

    # get the prediction for each 5s bin separately from the trained model and
    # store.
    for d, df in enumerate(test_list):

        v_pltfrom = df.at[0, 'Vid_pltform']
        v_pltfrom_ml = df.at[0, 'Vid_pltform_ml']
        v_type = df.at[0, 'Vid_type']
        v_number = df.at[0, 'Vid_num']
        loc = df.at[0, 'loc']
        time = df.at[0, 'time']
        bw = df.at[0, 'bandwidth']

        x_test = df[predictors].values
        y_pred = xgboost_model.predict(x_test)

        y_pred_list.append(y_pred)
        y_gt_list.append(np.repeat(v_type, len(y_pred)))

        pred_df = pd.DataFrame(columns=bin_cols,
                               data=np.asarray(y_pred).reshape([1, -1]))

        gt_df = pd.DataFrame(
            columns=['Vid_num', 'Vid_type', 'Vid_pltform', 'Vid_pltform_ml', 'loc', 'time', 'bandwidth'],
            data=np.asarray([v_number, v_type, v_pltfrom, v_pltfrom_ml, loc, time, bw]).reshape([1, -1]))

        final_df = pd.concat([gt_df, pred_df], axis=1)
        all_df.append(final_df)

    # return a summary of all the predictions in one DataFrame
    final_df = pd.concat(all_df, axis=0)
    return final_df
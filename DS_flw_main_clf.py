import argparse
from scipy import interpolate
from sklearn.utils import shuffle
import os
import pandas as pd
import numpy as np

import settings
import DS_flw_feat_sel as feat_sel
import DS_flw_run_ml as run_ml


final_gt_related_features_2_remove = [
    'Vid_pltform_mean',
    "Vid_number_mean",
    'Vid_begin_mean',
    'Vid_end_mean']


# Author: Chamara
# Description: Based on the feature importance graph derived filter the data
# Params: final_df: Final df containing the most important parameters
# Return: Filtered df with limited features
def filter_before_ml(final_df, platform, num_of_traces):
    # this feature list is derived based on feature importance graphs in the first trial
    rows_for_both_sel = []
    if platform == settings.PLATFORM_YT:
        if num_of_traces == 100:
            features = feat_sel.feature_list_exp1_yt_all
        elif num_of_traces == 1:
            features = feat_sel.feature_list_exp1_yt_1
        elif num_of_traces == 2:
            features = feat_sel.feature_list_exp1_yt_2
        elif num_of_traces == 4:
            features = feat_sel.feature_list_exp1_yt_4
        elif num_of_traces == 6:
            features = feat_sel.feature_list_exp1_yt_6
        elif num_of_traces == 8:
            features = feat_sel.feature_list_exp1_yt_8
        else:  # at 10
            features = feat_sel.feature_list_exp1_yt_10

    elif platform == settings.PLATFORM_FB:
        if num_of_traces == 100:
            features = feat_sel.feature_list_exp1_fb_all
        elif num_of_traces == 1:
            features = feat_sel.feature_list_exp1_fb_1
        elif num_of_traces == 2:
            features = feat_sel.feature_list_exp1_fb_2
        elif num_of_traces == 4:
            features = feat_sel.feature_list_exp1_fb_4
        elif num_of_traces == 6:
            features = feat_sel.feature_list_exp1_fb_6
        elif num_of_traces == 8:
            features = feat_sel.feature_list_exp1_fb_8
        else:  # at 10
            features = feat_sel.feature_list_exp1_fb_10

    else:
        if num_of_traces == 100:
            features = feat_sel.feature_list_exp1_both_all
        elif num_of_traces == 1:
            features = feat_sel.feature_list_exp1_both_1
        elif num_of_traces == 2:
            features = feat_sel.feature_list_exp1_both_2
        elif num_of_traces == 4:
            features = feat_sel.feature_list_exp1_both_4
        elif num_of_traces == 6:
            features = feat_sel.feature_list_exp1_both_6
        elif num_of_traces == 8:
            features = feat_sel.feature_list_exp1_both_8
        else:  # at 10
            features = feat_sel.feature_list_exp1_both_10

    final_df_val = final_df.loc[:, features].values
    filtered_final_df = pd.DataFrame(data=final_df_val,
                                     columns=features)
    return filtered_final_df


# Authour : Chamara
# Description: Function to control processing
# Params: Details of .csv file containing each video
def main_control(platform, df_from_main_train, df_from_main_test, num_of_traces):
    pd.set_option('display.max_rows', None)

    if platform == settings.PLATFORM_YT:
        platform_folder = 'yt'
    elif platform == settings.PLATFORM_FB:
        platform_folder = 'fb'
    else:
        platform_folder = 'both'

    # split trainning and test dataset
    train_df = df_from_main_train
    test_df = df_from_main_test

    # remove ground turth dependend data
    train_df = train_df.drop(final_gt_related_features_2_remove, axis=1)
    test_df = test_df.drop(final_gt_related_features_2_remove, axis=1)

    # reduce number of features to feed
    # train_df = filter_before_ml(train_df, platform, num_of_traces)
    # test_df = filter_before_ml(test_df, platform, num_of_traces)

    performance = run_ml.run_xgboost_ml(train_df, test_df, platform_folder)

    return performance


# Description: interpolate the points in teh AUC curve
def interpolate_points(df):
    x = df['fpr'].values
    y = df['tpr'].values
    auc = df['auc'].values
    f = interpolate.interp1d(x, y)

    fpr = np.arange(0, 1, 0.005)
    tpr = f(fpr)
    auc = np.repeat(auc[0], len(fpr))

    fpr = np.reshape(fpr, [-1, 1])
    tpr = np.reshape(tpr, [-1, 1])
    auc = np.reshape(auc, [-1, 1])
    auc_val_arry = np.concatenate([fpr, tpr, auc], axis=1)

    print(1)
    return auc_val_arry


def get_mean_auc_val(df_list):
    df_names = ['yt', 'fb', 'both', 'sel_both']
    values = ['fpr', 'tpr', 'auc']
    processed_df = []
    for df_ind, df in enumerate(df_list):

        df_sum = np.zeros((200, 3))

        for d in range(len(df)):
            df_sum = np.add(df_sum, df[d])

        df_mean = df_sum / len(df)

        new_names = []
        for i in range(len(values)):
            new_names.append(df_names[df_ind] + '_' + values[i])

        processed_df.append(pd.DataFrame(columns=new_names,
                                         data=df_mean))

    return_df = pd.concat(processed_df, axis=1)
    return_df.to_csv('/Users/ckat9988/Documents/Research/Passive_analaysis/Analysis/Experiments/temp/flow_lvl_df.csv')

    return return_df

# read the command line arguments
def read_argparse():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--t_type',
                        type=str,
                        default='YT',
                        help='Select one of the traffic type as a String variable: ' + '"' + 'YT' + '",' + '"' + 'FB' + '",' + 'or ' + '"' + 'BOTH' + '"')
    parser.add_argument('--num_of_flows',
                        type=int,
                        default=4,
                        help="Select the num_of_flows of the trace: 1, 2, 4, 6, 8, 10, 100-(denotes all flows)")
    parser.add_argument('--num_of_trials',
                        type=int,
                        default=20,
                        help="num of different train/test splits")

    parser.add_argument('--path',
                        type=str,
                        default=os.path.abspath(os.getcwd()),
                        help="Set the working dir path")

    args = parser.parse_args()

    # set default path to the current working directory.
    pltform_str = args.t_type
    if pltform_str == 'YT':
        pltform = settings.PLATFORM_YT
    elif pltform_str == 'FB':
        pltform = settings.PLATFORM_FB
    elif pltform_str == 'BOTH':
        pltform = settings.PLATFORM_BOTH
    else:
        print('Enter valid Platform name')
        return

    num_of_flows = args.num_of_flows
    if not num_of_flows in [1, 2, 4, 6, 8, 10, 100]:
        print('Enter valid Duration')
        return
    else:
        num_of_flows = args.num_of_flows

    num_of_trials = args.num_of_trials

    path = args.path

    return pltform, num_of_flows, num_of_trials, path


def main():
    platform, num_of_traces, num_of_trial, path = read_argparse()

    if platform == settings.PLATFORM_YT:
        pltform_folder = 'yt'
    elif platform == settings.PLATFORM_FB:
        pltform_folder = 'fb'
    else:
        pltform_folder = 'both'

    acc = []
    for i in range(num_of_trial):
        np.random.seed(i * 50)

        # according to the traffic type select read the data
        if platform != settings.PLATFORM_BOTH:
            final_df = pd.read_csv(
                path + '/processed_data_flow_lvl/num_traces_' + str(num_of_traces) + '/' + pltform_folder + '.csv')
            final_df = shuffle(final_df, random_state=i * 50)
            # split the data to train and test splits based on the video id
            train_df, test_df = run_ml.split_by_control_param(final_df,
                                                              platform=platform,
                                                              random_seed=i * 50)
        # for 'BOTH' traffic type combine yt and fb data
        else:
            final_df_yt = pd.read_csv(path + '/processed_data_flow_lvl/num_traces_' + str(num_of_traces) + '/yt.csv')
            final_df_yt = shuffle(final_df_yt, random_state=i * 50)
            train_df_yt, test_df_yt = run_ml.split_by_control_param(final_df_yt,
                                                                    platform=settings.PLATFORM_YT,
                                                                    random_seed=i * 50)

            final_df_fb = pd.read_csv(path + '/processed_data_flow_lvl/num_traces_' + str(num_of_traces) + '/fb.csv')
            final_df_fb = shuffle(final_df_fb, random_state=i * 50)
            train_df_fb, test_df_fb = run_ml.split_by_control_param(final_df_fb,
                                                                    platform=settings.PLATFORM_FB,
                                                                    random_seed=i * 50)

            train_df_both = pd.concat([train_df_yt, train_df_fb])
            test_df_both = pd.concat([test_df_yt, test_df_fb])
            train_df = shuffle(train_df_both, random_state=i * 50)
            test_df = shuffle(test_df_both, random_state=i * 50)

        # run the machine learning classification
        performance = main_control(platform=platform,
                                   df_from_main_train=train_df,
                                   df_from_main_test=test_df,
                                   num_of_traces=num_of_traces)
        print(performance)
        acc.append(performance)

    output_path = path + '/clf_result_DS_flw_main/' + pltform_folder
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    columns = ['accuracy', 'precision', 'recall']
    data = np.asarray(acc)
    df = pd.DataFrame(columns=columns,
                      data=data)

    print(np.mean(data[:, 0]))

    df.to_csv(output_path + '/' + 'result_num_of_trace_' + str(num_of_traces) + '_num_of_trials_'+ str(num_of_trial) + '.csv',
              index=False)

    return


if __name__ == main():
    main()

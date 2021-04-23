# This function to classify the data in real time
import argparse

import pandas as pd
import numpy as np
import os
import random

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from scipy import stats
import pathlib

import DS_pkt_near_realtime_run_ml as run_ml
import settings


def read_data(dataset_dir):
    df_list = []
    video_list = os.listdir(dataset_dir)

    for video in video_list:
        if video == '.DS_Store':
            continue
        video_path = pathlib.Path(str(dataset_dir) + '/' + video)
        t_df = pd.read_csv(video_path)

        if len(t_df) > 0:
            df_list.append(t_df)

    return df_list


def split_to_train_test(input_path, random_seed, platform):
    print('split for xgboost')
    loc_1 = 1
    bw_nc = 0

    loc = loc_1
    bw = bw_nc

    dataset_list = os.listdir(input_path)

    # read all  the data under given dataset
    df_list = []
    for dataset_ind, dataset in enumerate(dataset_list):

        if dataset == '.DS_Store':
            continue
        conditions = dataset.split('_')

        if int(conditions[1]) == loc and int(conditions[3]) == bw:
            condition_path = input_path + '/' + dataset

            temp_df_list = read_data(condition_path)

            # select for the given platform
            for i in range(len(temp_df_list)):
                if temp_df_list[i].loc[0, 'Vid_pltform'] == platform:
                    df_list.append(temp_df_list[i])

    # split to train and test dataset
    train_list = []
    test_list = []

    all_videos = np.arange(0, 51, 1)
    np.random.seed(random_seed)
    test_ind = np.random.choice(all_videos, size=15, replace=False)

    train_ind = list(set(list(all_videos)) - set(list(test_ind)))
    test_ind = list(test_ind)

    for df in df_list:
        if df.loc[0, 'Vid_num'] in test_ind:
            test_list.append(df)
        elif df.loc[0, 'Vid_num'] in train_ind:
            train_list.append(df)

    # train_list = [j for sub in train_list for j in sub]
    # test_list = [j for sub in test_list for j in sub]

    random.Random(random_seed).shuffle(train_list)
    random.Random(random_seed).shuffle(test_list)

    train_df = pd.concat(train_list, axis=0)
    test_df = pd.concat(test_list, axis=0)

    return train_df, test_df, train_list, test_list


# train and test xgboost models
def train_xgboost_model(train_df, test_df, train_list, test_list):
    print('run_xgboost')

    feature_removed = [
        'Unnamed: 0',
        'index1',
        'Vid_pltform',
        'Vid_pltform_ml',
        'Vid_begin',
        'Vid_end',
        'loc',
        'time',
        'bandwidth',
        'Vid_num',

    ]
    train_df.drop(feature_removed, inplace=True, axis=1)
    test_df.drop(feature_removed, inplace=True, axis=1)

    # print(train_df.dtypes)
    final_df = run_ml.run_xgboost(train_df, test_df, train_list, test_list)

    return final_df


# split the data for naive bayes
def train_test_split(xgboost_pred, random_seed):
    all_videos = np.arange(0, 51, 1)
    np.random.seed(random_seed)
    test_ind = np.random.choice(all_videos, size=15, replace=False)

    train_ind = list(set(list(all_videos)) - set(list(test_ind)))
    test_ind = list(test_ind)

    train_df = xgboost_pred.loc[xgboost_pred['Vid_num'].isin(list(train_ind))]
    test_df = xgboost_pred.loc[xgboost_pred['Vid_num'].isin(list(test_ind))]

    train_df.to_csv(
        '/Users/ckat9988/Documents/Research/Passive_analaysis/Analysis/Experiments/temp/train_csv_naive.csv')
    test_df.to_csv(
        '/Users/ckat9988/Documents/Research/Passive_analaysis/Analysis/Experiments/temp/test_csv_naive.csv')

    return train_df, test_df


# get the raw bin data.
def get_raw_bin_acc(xgboost_data, time_point):
    gt = xgboost_data.loc[:, 'Vid_type'].values
    predictions = xgboost_data.loc[:, 'bin_1':'bin_' + str(time_point)].values

    mode_prefictions = stats.mode(predictions, axis=1)[0]
    acc_mode = accuracy_score(gt, mode_prefictions)
    prec_mode = precision_score(gt, mode_prefictions)
    rec_mode = recall_score(gt, mode_prefictions)
    f1_mode = f1_score(gt, mode_prefictions)
    mode_performance = [acc_mode, prec_mode, rec_mode, f1_mode]

    return mode_performance


def store_data(platform, data, outpath):
    if platform == settings.PLATFORM_YT:
        write_folder = 'yt'
    elif platform == settings.PLATFORM_FB:
        write_folder = 'fb'
    else:
        write_folder = 'both'

    t = np.arange(10, 121, 5).reshape([-1, 1])
    cols = ['time', 'acc', 'prec', 'recall', 'f1']
    mertic_data = np.asarray(data)

    df_data = np.concatenate([t, mertic_data], axis=1)

    df = pd.DataFrame(columns=cols,
                      data=df_data)

    df.to_csv(outpath + '/' + write_folder + '.csv', index=False)

    return


def read_xgboost_data(read_path, read_folder):
    df_list = []

    for p in read_folder:
        path_in = read_path + '/' + p

        df = pd.read_csv(path_in + '.csv')
        df_list.append(df)

    final_df = pd.concat(df_list, axis=0)

    return final_df

# check whether XGBoost predictions are taken
def check_for_xgboost_data(read_path, platform):
    for p in platform:
        if not os.path.exists(read_path+'/'+p+'.csv'):
            return False
        else:
            return True

# Run the majority voting operation
def run_mode_prediction(platform, read_path, outpath):
    if platform == settings.PLATFORM_YT:
        read_folder = ['yt']
        # check whether the xgboost predictions are existis
        if not check_for_xgboost_data(read_path,read_folder):
            print('No XGBoost predictions for YT ')
            return
    elif platform == settings.PLATFORM_FB:
        read_folder = ['fb']
        if not check_for_xgboost_data(read_path,read_folder):
            print('No XGBoost predictions for FB ')
            return
    else:
        read_folder = ['yt', 'fb']
        if not check_for_xgboost_data(read_path,read_folder):
            print('No XGBoost predictions for FB / YT')
            return

    # read xgboost prediction
    xgboost_data = read_xgboost_data(read_path, read_folder)

    all_mode_results = []

    for t in range(10, 121, 5):
        print(t)
        # get raw predictions from XGBoost
        mode_performance = get_raw_bin_acc(xgboost_data, time_point=t - 5)
        all_mode_results.append(mode_performance)

    # store the data
    store_data(platform, all_mode_results,outpath)


# main function to contorll the data
def main_controller(path,num_of_rounds, platform, is_xgboost,is_mode,is_already_processed):
    path_bin_data = path + '/' + 'processed_data_DS_pkt_near_realtime/bin_data'

    if platform == settings.PLATFORM_YT:
        platform_name = 'yt'
    elif platform == settings.PLATFORM_FB:
        platform_name = 'fb'
    else:
        platform_name = 'both'

    # run the XGBoost prediction
    if is_xgboost:
        # predict using XGBoost
        if not is_already_processed:
            # XGBoost predicitons are for the platforms separately
            if platform==settings.PLATFORM_YT or  platform==settings.PLATFORM_FB:
                print('start runnin xgboost')
                xgboost_pred_list = []
                for i in range(num_of_rounds):
                    print('Round: '+str(num_of_rounds))
                    train_df, test_df, train_list, test_list = split_to_train_test(path_bin_data, i * 50, platform)
                    xgboost_pred_list.append(train_xgboost_model(train_df, test_df, train_list, test_list))

                path_xgboost_predict = path + '/clf_result_DS_pkt_near_realtime/' + 'XGBoost_prediction'
                if not os.path.exists(path_xgboost_predict):
                    os.makedirs(path_xgboost_predict)

                final_xgboost_pred = pd.concat(xgboost_pred_list, axis=0)
                final_xgboost_pred.to_csv(path_xgboost_predict + '/' + platform_name + '.csv', index=False)
            else:
                print('Run XGBoost prediction for YT and FB individually')
        # use author provided data
        else:
            print('You have selected to XGBoost predications by the authors')

    # run the Majority voting operation
    if is_mode:
        # get the predictions using author provided dat
        if is_already_processed:
            read_path = path + '/clf_result_DS_pkt_near_realtime/XGBoost_prediction_processed'
            outpath = path + '/clf_result_DS_pkt_near_realtime/MODE_prediction_processed'
        else:
            # check whether the XGBoost predictions have been taken before
            read_path = path + '/clf_result_DS_pkt_near_realtime/XGBoost_prediction'
            outpath = path + '/clf_result_DS_pkt_near_realtime/MODE_prediction'
            if not os.path.exists(read_path):
                print('You have not run XGBoost predictions before')
                return
        # if all conditions are satisfied, run the operation
        if not os.path.exists(outpath):
            os.makedirs(outpath)
        run_mode_prediction(platform, read_path, outpath)
    return


def main():

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--t_type',
                        type=str,
                        default='YT',
                        help='Select one of the traffic type as a String variable: ' + '"' + 'YT' + '",' +  '"'+'FB'+'",'+  'or '+'"'+'BOTH' + '"')

    parser.add_argument('--num_of_rounds_xgboost',
                        type=int,
                        default=10,
                        help='Number of rounds for XGBoost prediction')

    parser.add_argument('--run_xgboost',
                        default=False,
                        action="store_true",
                        help='Set the varible to run the initial XGBoost prediction on DS-pkt binned data')

    parser.add_argument('--run_mode_operation',
                        default=False,
                        action="store_true",
                        help='Set the varible to get the final prediciton results')

    parser.add_argument('--already_processed',
                        default=False,
                        action="store_true",
                        help='Run the mode operation with already processed XGBoost prediction by the authors')

    parser.add_argument('--path',
                        type=str,
                        # set default path to the current working directory.
                        default=os.path.abspath(os.getcwd()),
                        help="Set the working dir path")

    args = parser.parse_args()


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
    num_of_rounds = args.num_of_rounds_xgboost
    is_xgboost = args.run_xgboost
    is_mode = args.run_mode_operation
    is_already_processed = args.already_processed

    print(num_of_rounds)
    print(is_xgboost)
    print(is_mode)
    print(is_already_processed)

    path = args.path

    main_controller(path,num_of_rounds, pltform, is_xgboost,is_mode,is_already_processed )

    return


if __name__ == main():
    main()

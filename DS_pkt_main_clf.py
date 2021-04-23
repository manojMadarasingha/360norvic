import settings
import pandas as pd
import numpy as np
import os
import pathlib

import preprocess_data
import DS_pkt_main_result_run_ml as run_ml
import feature_importance
from scipy import interpolate
from sklearn.utils import shuffle
import argparse


def main_controller(platform, duration, num_of_iterations, path):
    # select the traffic type
    if platform == settings.PLATFORM_YT:
        platform_folder = 'yt'
    elif platform == settings.PLATFORM_FB:
        platform_folder = 'fb'
    else:
        platform_folder = 'both'

    output_path = path + '/' + 'clf_results_DS_pkt_main' + '/' + platform_folder
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # read data to assess individul platforms
    if platform != settings.PLATFORM_BOTH:
        path_in = path + '/' + 'processed_data_DS_pkt' + '/' + platform_folder
        final_df = pd.read_csv(path_in + '/' + 's_1_w_5_t_' + str(duration) + '.csv', )
    # read both platforms to assess the 'BOTH' traffic types
    else:
        path_in = path + '/' + 'processed_data_DS_pkt' + '/' + 'yt'
        final_df_yt = pd.read_csv(path_in + '/' + 's_1_w_5_t_' + str(duration) + '.csv')
        path_in = path + '/' + 'processed_data_DS_pkt' + '/' + 'fb'
        final_df_fb = pd.read_csv(path_in + '/' + 's_1_w_5_t_' + str(duration) + '.csv')
        final_df = pd.concat([final_df_yt, final_df_fb], axis=0)
        final_df.reset_index(inplace=True, drop=True)

    final_df = shuffle(final_df, random_state=123)

    roc_list = []
    acc_list = []
    prec_list = []
    recal_list = []

    # run the classification
    for i in range(num_of_iterations):

        # in every iteration change the train and test data
        train_df, test_df = run_ml.split_train_test(final_df, random_seed=i)

        # remove ground truth variables
        feature_removed = [
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

        counts = np.asarray(test_df['Vid_type'].value_counts())

        # run the classification
        if len(counts) > 1:
            acc, prec, recall, roc = run_ml.run_xgboost(train_df, test_df, platform, i)
            roc_list.append(roc)
            acc_list.append(acc)
            prec_list.append(prec)
            recal_list.append(recall)

    final_performance = pd.DataFrame({'Acc': np.asarray(acc_list),
                                      'Pred': np.asarray(prec_list),
                                      'Reca': np.asarray(recal_list)})

    print('average === Acc: %.2f  Prec: %.2f  Reca: %.2f ===' % (np.mean(np.asarray(acc_list)),
                                                                 np.mean(np.asarray(prec_list)),
                                                                 np.mean(np.asarray(prec_list))))
    # store the data.
    final_performance.to_csv(
        output_path + '/' + 's_1_w_5_duration_' + str(duration) + '_iterations_' + str(num_of_iterations) + '.csv',
        index=False)

    return


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--t_type',
                        type=str,
                        default='YT',
                        help='Select one of the traffic type as a String variable: ' + '"' + 'YT' + '",' + '"' + 'FB' + '",' + 'or ' + '"' + 'BOTH' + '"')
    parser.add_argument('--duration',
                        type=int,
                        default=60,
                        help="Select onr of the duration of the trace: 20,30,60,90 or 120")

    parser.add_argument('--num_of_iterations',
                        type=int,
                        default=20,
                        help="Select onr of the duration of the trace: 20,30,60,90 or 120")

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

    duration = args.duration
    if not duration in [20, 30, 60, 90, 120]:
        print('Enter valid Duration')
        return
    else:
        duration = args.duration
    num_of_iterations = args.num_of_iterations

    path = args.path

    print('===Start running classification====')
    main_controller(platform=pltform,
                    duration=duration,
                    num_of_iterations=num_of_iterations,
                    path=path)

    return


if __name__ == main():
    main()

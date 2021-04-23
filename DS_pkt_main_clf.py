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


def main_controller(platform, duration, path):
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

    num_of_iterations = 20

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
    final_performance.to_csv(output_path + '/' + 's_1_w_5_t_' + str(duration) + '.csv')

    return


# interpolate the data
def interpolate_auc(roc_list):
    # store the values of auc
    new_tpr_list = []
    auc_val_list = []
    new_fpr = np.arange(0, 1, 0.01)
    for auc in roc_list:
        auc_val_list.append(auc.loc[0, '_auc'])
        fpr = auc['_fpr'].values
        tpr = auc['_tpr'].values

        f = interpolate.interp1d(fpr, tpr)
        new_tpr_list.append(f(new_fpr))

    new_tpr = np.asarray(new_tpr_list).mean(axis=0)
    auc_val = np.asarray(auc_val_list).mean()
    auc_val = np.repeat(auc_val, len(new_fpr))

    final_auc_df = pd.DataFrame({'fpr': new_fpr,
                                 'tpr': new_tpr,
                                 'auc': auc_val})

    final_auc_df.to_csv('/Users/ckat9988/Documents/Research/Passive_analaysis/Analysis/Experiments/temp/final_auc.csv')
    return final_auc_df


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
    path = args.path

    print('===Start running classification====')
    main_controller(platform=pltform,
                    duration=duration,
                    path=path)

    return


if __name__ == main():
    main()

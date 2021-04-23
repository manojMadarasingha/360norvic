# finally remvoig features which are at the ground truth
final_gt_related_features_2_remove = [
    'Vid_pltform_mean',
    "Vid_number_mean",
    'Vid_begin_mean',
    'Vid_end_mean'

]

# ========EXP 1===========================
# ========EXP 1===========================
# features to be selected before feeding to the machine learning model

# ========YT =============================
feature_list_exp1_yt_all = [
    'Vid_type_mean',
    'Vid_pltform_ML_mean',
    # "Vid_number_mean",

    'mean_size_frame_dl_mean_max',
    'mean_size_frame_ul_mean_mean',
    'Avg_throughput_dl_sum',
    'Avg_throughput_dl_max',
    'maxserverburstsize_max',
    'mean_size_frame_ul_mean_sum',
    'mean_gap_frame_ul_mean_max',
    'flow_gap_sum',
    'maxclientbursttime_mean',
    'mean_gap_frame_ul_mean_mean',
    'burst_size_dl_mean_max',
    'burst_sizerate_dl_mean_mean',
    'burst_gap_dl_mean_mean',
    'maxclientburstsize_max',
    'mean_gap_frame_ul_mean_sum',
    'burst_duration_ul_mean_sum',
    'burst_gap_dl_mean_sum',
    'Avg_throughput_dl_mean',
    'burst_duration_dl_mean_mean',
    'burst_size_dl_mean_sum',
]

feature_list_exp1_yt_1 = [
    'Vid_type_mean',
    'Vid_pltform_ML_mean',

    'Avg_throughput_uldl_mean',
    'burst_size_uldl_mean_mean',
    'burst_duration_ul_mean_mean',
    'mean_size_frame_dl_mean_mean',
    'mean_size_frame_ul_mean_mean',
    'maxserverburstrate_mean',
    'maxserverburstsize_mean',
    'maxclientburstpacket_mean',
    'mean_size_frame_uldl_mean_mean',
    'mean_gap_frame_dl_mean_mean',
    'burst_duration_dl_mean_mean',
    'burst_gap_ul_mean_mean',
    'burst_sizerate_dl_mean_mean',
    'Avg_throughput_dl_mean',
]

feature_list_exp1_yt_2 = [
    'Vid_type_mean',
    'Vid_pltform_ML_mean',

    'mean_size_frame_dl_mean_max',
    'mean_size_frame_ul_mean_min',
    'maxserverburstsize_max',
    'burst_size_uldl_mean_max',
    'mean_gap_frame_ul_mean_max',
    'burst_duration_ul_mean_max',
    'maxclientburstrate_max',
    'maxserverburstsize_sum',
    'burst_sizerate_ul_mean_max',
    'Avg_throughput_uldl_sum',
    'Avg_throughput_uldl_max',
    'maxserverburstrate_min',
    'burst_size_dl_mean_max',
    'maxclientburstsize_max',
    # 'sum_of_packets_uldl_mean_max',
    'maxserverburstpacket_sum',
    'maxserverburstpacket_max',
    'burst_duration_dl_mean_max',
    'Avg_throughput_ul_mean',
    'burst_gap_ul_mean_max'
]

feature_list_exp1_yt_4 = [
    'Vid_type_mean',
    'Vid_pltform_ML_mean',

    'mean_size_frame_dl_mean_max',
    'mean_size_frame_ul_mean_min',
    'maxserverburstsize_max',
    'burst_size_uldl_mean_max',
    'maxserverbursttime_max',
    'mean_gap_frame_ul_mean_max',
    'burst_duration_ul_mean_max',
    'maxclientburstrate_mean',
    'burst_size_dl_mean_max',
    'maxserverburstsize_mean',
    'maxserverburstpacket_sum',
    'maxserverburstpacket_mean',
    'maxserverburstsize_sum',
    'maxserverbursttime_mean',
    'maxclientburstrate_max',
    'maxclientbursttime_sum',
    'burst_gap_ul_mean_min',
    'burst_gap_dl_mean_max',
    # 'sum_of_packets_uldl_mean_max',
    'maxserverburstpacket_max'

]

feature_list_exp1_yt_6 = [
    'Vid_type_mean',
    'Vid_pltform_ML_mean',

   'mean_size_frame_ul_mean_min',
   'mean_size_frame_dl_mean_max',
   'burst_size_dl_mean_max',
   'burst_num_of_packets_dl_mean_max',
   'mean_gap_frame_ul_mean_max'



    # 'mean_size_frame_dl_mean_max',
    # 'mean_size_frame_ul_mean_min',
    # 'maxserverburstsize_max',
    # 'flow_gap_min',
    # 'mean_gap_frame_ul_mean_max',
    # 'maxserverburstpacket_max',
    # 'maxclientbursttime_sum',
    # # 'burst_sum_of_packets_uldl_mean_max',
    # 'maxserverburstsize_mean',
    # 'burst_size_uldl_mean_max',
    # 'flow_gap_max',
    # 'flow_gap_mean',
    # 'burst_sizerate_dl_mean_max',
    # 'burst_gap_ul_mean_min',
    # 'burst_size_dl_mean_max',
    # 'maxclientbursttime_max',
    # 'mean_gap_frame_dl_mean_min',
    # 'burst_size_ul_mean_min',
    # 'Avg_throughput_ul_max',
    # 'burst_sizerate_dl_mean_mean'

]

feature_list_exp1_yt_8 = [
    'Vid_type_mean',
    'Vid_pltform_ML_mean',

    'mean_size_frame_dl_mean_max',
    'mean_size_frame_ul_mean_min',
    'mean_gap_frame_ul_mean_mean',
    'maxserverburstsize_max',
    'Avg_throughput_uldl_max',
    'mean_gap_frame_ul_mean_max',
    'flow_gap_sum',
    'burst_duration_ul_mean_max',
    'maxserverburstpacket_max',
    'Avg_throughput_dl_max',
    'Avg_throughput_ul_max',
    'mean_size_frame_ul_mean_sum',
    'burst_size_dl_mean_max',
    'burst_size_ul_mean_sum',
    'burst_size_uldl_mean_max',
    'Avg_throughput_uldl_sum',
    'maxserverburstsize_sum',
    'mean_size_frame_ul_mean_mean',
    'maxserverburstrate_min',
    'mean_gap_frame_ul_mean_sum'

]

feature_list_exp1_yt_10 = [
    'Vid_type_mean',
    'Vid_pltform_ML_mean',

    'mean_size_frame_dl_mean_max',
    'mean_size_frame_ul_mean_min',
    'maxserverburstsize_max',
    'maxclientbursttime_max',
    'flow_gap_sum',
    'maxserverburstpacket_max',
    'burst_duration_ul_mean_max',
    'Avg_throughput_uldl_max',
    'flow_gap_max',
    'maxserverbursttime_sum',
    'burst_duration_ul_mean_sum',
    'burst_sizerate_dl_mean_max',
    'mean_gap_frame_ul_mean_max',
    'maxserverbursttime_mean',
    'maxclientbursttime_sum',
    # 'sum_of_packets_uldl_mean_max',
    'burst_size_uldl_mean_max',
    'burst_gap_dl_mean_min',
    'flow_gap_mean',
    'burst_size_ul_mean_min'

]

feature_stdpercentile_list_exp1_yt = [
    'Vid_type_mean',
    'Vid_pltform_ML_mean',
    # "Vid_number_mean",

    'maxserverburstrate_50%',
    'maxserverburstpacket_max',
    'burst_sizerate_dl_mean_mean',
    'burst_duration_ul_mean_std',

    'mean_size_frame_dl_mean_max',
    'mean_size_frame_ul_mean_min',
    'maxserverburstsize_max',
    'maxserverburstrate_75%',
    'mean_size_frame_ul_mean_75%',
    'Avg_throughput_dl_sum',
    'mean_gap_frame_ul_mean_std',
    'Avg_throughput_dl_max',
    'burst_gap_dl_mean_min',
    'mean_gap_frame_ul_mean_mean',

    'burst_size_ul_mean_25%',
    'mean_gap_frame_ul_mean_max',
    'burst_duration_dl_mean_min',
    'mean_gap_frame_ul_mean_25%',
    'maxclientburstrate_25%',
    'burst_size_dl_mean_50%',
    'maxserverburstsize_50%',
    'maxclientbursttime_mean',
    'burst_duration_dl_mean_25%',
    'burst_gap_ul_mean_min',
]

# == == == == FB == == == == == == == == == == == == == == =

feature_list_exp1_fb_all = [
    'Vid_type_mean',
    'Vid_pltform_ML_mean',

    'mean_size_frame_dl_mean_sum',
    'mean_size_frame_dl_mean_max',
    'mean_size_frame_dl_mean_mean',
    'burst_size_dl_mean_max',
    'burst_gap_ul_mean_mean',
    'flow_gap_max',
    'maxserverburstsize_mean',
    'burst_sizerate_dl_mean_mean',
    'burst_size_dl_mean_sum',
    'Avg_throughput_dl_max',
    'burst_duration_ul_mean_max',
    'Avg_throughput_dl_sum',
    'burst_size_ul_mean_max',
    'maxserverburstsize_sum',
    'burst_duration_dl_mean_mean',
    'maxclientburstsize_mean',
    'burst_num_of_packets_ul_mean_max',
    'burst_gap_dl_mean_mean',
    'maxclientburstsize_max',
    'mean_size_frame_ul_mean_max',

]

feature_list_exp1_fb_1 = [

    'Vid_type_mean',
    'Vid_pltform_ML_mean',

    'mean_size_frame_ul_mean_mean',
    'maxclientburstrate_mean',
    'burst_gap_ul_mean_mean',
    'mean_gap_frame_ul_mean_mean',
    'maxserverbursttime_mean',
    'Avg_throughput_ul_mean',
    'mean_size_frame_dl_mean_mean',
    'maxclientburstsize_mean',
    'burst_size_uldl_mean_mean',
    'Avg_throughput_uldl_mean',
    'mean_gap_frame_dl_mean_mean'
]

feature_list_exp1_fb_2 = [

    'Vid_type_mean',
    'Vid_pltform_ML_mean',

    'mean_size_frame_ul_mean_min',
    'mean_gap_frame_ul_mean_max',
    'Avg_throughput_dl_min',
    'mean_size_frame_dl_mean_min',
    'Avg_throughput_ul_min',
    'maxserverburstsize_min',
    'maxclientburstrate_min',
    'mean_gap_frame_ul_mean_min',
    'Avg_throughput_uldl_max',
    'Avg_throughput_uldl_mean',
    'burst_sizerate_ul_mean_min',
    'maxclientburstrate_mean',
    'burst_duration_ul_mean_min',
    'burst_size_ul_mean_min',
    'burst_sizerate_ul_mean_max',
    'burst_sizerate_ul_mean_mean',
    'burst_gap_dl_mean_max',
    'burst_duration_ul_mean_max',
    'mean_gap_frame_ul_mean_mean',
    'burst_gap_dl_mean_mean'
]

feature_list_exp1_fb_4 = [

    'Vid_type_mean',
    'Vid_pltform_ML_mean',

   'mean_size_frame_dl_mean_mean',
   'mean_size_frame_dl_mean_sum',
   'burst_size_uldl_mean_mean',
   'mean_size_frame_ul_mean_min',
   'burst_gap_ul_mean_mean'


    # 'mean_size_frame_ul_mean_min',
    # 'maxserverburstrate_min',
    # 'mean_size_frame_dl_mean_mean',
    # 'mean_gap_frame_ul_mean_max',
    # 'burst_size_ul_mean_max',
    # 'flow_gap_min',
    # 'Avg_throughput_uldl_max',
    # 'burst_gap_ul_mean_mean',
    # 'mean_size_frame_dl_mean_sum',
    # 'flow_gap_max',
    # 'burst_num_of_packets_dl_mean_min',
    # 'burst_size_uldl_mean_min',
    # 'flow_gap_mean',
    # 'Avg_throughput_dl_max',
    # 'burst_size_ul_mean_min',
    # 'mean_size_frame_dl_mean_max',
    # 'burst_size_dl_mean_min',
    # 'burst_sizerate_ul_mean_min',
    # 'burst_duration_ul_mean_max',
    # 'burst_num_of_packets_ul_mean_max'
]

feature_list_exp1_fb_6 = [

    'Vid_type_mean',
    'Vid_pltform_ML_mean',

    'mean_size_frame_ul_mean_min',
    'mean_size_frame_dl_mean_sum',
    'flow_gap_min',
    'mean_size_frame_dl_mean_mean',
    'Avg_throughput_uldl_max',
    'maxclientburstsize_min',
    'burst_duration_ul_mean_max',
    'burst_size_dl_mean_sum',
    'flow_gap_mean',
    'mean_size_frame_dl_mean_max',
    'burst_gap_ul_mean_mean',
    'mean_gap_frame_ul_mean_max',
    'Avg_throughput_dl_max',
    'burst_gap_dl_mean_mean',
    'maxserverburstsize_sum',
    'mean_size_frame_uldl_mean_mean',
    'burst_num_of_packets_dl_mean_sum',
    'mean_size_frame_ul_mean_max',
    'mean_size_frame_uldl_mean_max',
    'burst_sizerate_dl_mean_sum'
]

feature_list_exp1_fb_8 = [
    'Vid_type_mean',
    'Vid_pltform_ML_mean',

    'mean_size_frame_dl_mean_sum',
    'mean_size_frame_dl_mean_max',
    'Avg_throughput_uldl_max',
    'mean_size_frame_ul_mean_min',
    'burst_gap_ul_mean_mean',
    'mean_size_frame_dl_mean_mean',
    'flow_gap_mean',
    'burst_sizerate_dl_mean_mean',
    'flow_gap_min',
    'burst_duration_ul_mean_max',
    'mean_size_frame_uldl_mean_mean',
    'Avg_throughput_dl_max',
    'burst_gap_ul_mean_sum',
    # '_num_of_packets_dl_mean_sum',
    'burst_sizerate_dl_mean_sum',
    'flow_gap_sum',
    'Avg_throughput_uldl_mean',
    'burst_size_uldl_mean_min',
    'maxserverburstrate_min',
    'burst_gap_dl_mean_mean'

]

feature_list_exp1_fb_10 = [
    'Vid_type_mean',
    'Vid_pltform_ML_mean',

    'mean_size_frame_dl_mean_sum',
    'mean_size_frame_dl_mean_max',
    'Avg_throughput_uldl_max',
    'flow_gap_mean',
    'mean_size_frame_uldl_mean_mean',
    'burst_gap_ul_mean_mean',
    'mean_size_frame_dl_mean_mean',
    'burst_sizerate_dl_mean_mean',
    'mean_size_frame_dl_mean_min',
    'Avg_throughput_dl_max',
    'burst_duration_ul_mean_max',
    'burst_sizerate_dl_mean_sum',
    'mean_size_frame_uldl_mean_sum',
    'flow_gap_min',
    'flow_gap_sum',
    'burst_gap_dl_mean_mean',
    'flow_gap_max',
    'mean_size_frame_uldl_mean_max',
    'burst_size_dl_mean_sum',
    'mean_gap_frame_ul_mean_max'

]

feature_stdpercentile_list_exp1_fb = [
    'Vid_type_mean',
    'Vid_pltform_ML_mean',
    # "Vid_number_mean",

    'mean_size_frame_dl_mean_max',
    'mean_size_frame_dl_mean_sum',
    'burst_size_dl_mean_75%',
    'mean_size_frame_dl_mean_75%',
    'burst_num_of_packets_ul_mean_std',
    'burst_num_of_packets_dl_mean_std',
    'burst_num_of_packets_dl_mean_75%',
    'maxserverbursttime_25%',
    'flow_gap_min',
    'Max_rtt_sum',
    'Avg_throughput_dl_sum',
    'burst_size_dl_mean_std',
    'flow_gap_25%',
    'burst_duration_ul_mean_25%',
    'Avg_throughput_dl_mean',
    'burst_size_dl_mean_sum',
    'maxclientburstsize_std',
    'Avg_throughput_ul_75%',
    'Avg_throughput_dl_50%',
    'maxclientbursttime_50%'

]

feature_list_exp1_both_all = [
    'Vid_type_mean',
    'Vid_pltform_ML_mean',

    'Vid_pltform_ML_mean',
    'mean_size_frame_dl_mean_max',
    'mean_size_frame_dl_mean_sum',
    'mean_size_frame_dl_mean_mean',
    'mean_gap_frame_ul_mean_max',
    'mean_size_frame_ul_mean_mean',
    'Avg_throughput_dl_sum',
    'burst_size_ul_mean_max',
    'flow_gap_max',
    'Avg_throughput_dl_max',
    'flow_gap_sum',
    'burst_gap_dl_mean_mean',
    'maxclientburstsize_max',
    'burst_size_dl_mean_max',
    'burst_num_of_packets_dl_mean_sum',
    'mean_gap_frame_ul_mean_sum',
    'burst_gap_ul_mean_mean',
    'Avg_throughput_dl_mean',
    'burst_size_dl_mean_mean',
    'Avg_throughput_ul_mean',
    'mean_gap_frame_ul_mean_mean'
]

feature_list_exp1_both_1 = [

    'Vid_type_mean',
    'Vid_pltform_ML_mean',

    'mean_size_frame_ul_mean_mean',
    'burst_duration_ul_mean_mean',
    'mean_size_frame_dl_mean_mean',
    'maxserverburstrate_mean',
    'burst_gap_ul_mean_mean',
    'maxclientburstrate_mean',
    'burst_size_uldl_mean_mean',
    'maxclientburstsize_mean',
    'mean_gap_frame_ul_mean_mean',
    'mean_size_frame_uldl_mean_mean',
    'burst_sizerate_ul_mean_mean',
    'burst_duration_dl_mean_mean',
    'Avg_throughput_uldl_mean',
    'Avg_throughput_ul_mean',
    'maxserverbursttime_mean',
    'burst_size_ul_mean_mean',

]

feature_list_exp1_both_2 = [

    'Vid_type_mean',
    'Vid_pltform_ML_mean',

    'mean_size_frame_ul_mean_min',
    'mean_size_frame_dl_mean_max',
    'mean_gap_frame_ul_mean_max',
    'Avg_throughput_ul_min',
    'maxserverburstsize_sum',
    'burst_duration_ul_mean_max',
    'maxserverburstsize_min',
    'Avg_throughput_dl_min',
    'burst_size_uldl_mean_max',
    'maxclientburstrate_min',
    'Avg_throughput_uldl_min',
    'burst_sizerate_ul_mean_min',
    'maxclientburstrate_max',
    'burst_size_dl_mean_max',
    'maxclientburstsize_max',
    'maxserverburstsize_mean',
    'burst_gap_dl_mean_max',
    'burst_gap_dl_mean_mean',
    'maxclientburstrate_mean',
    'burst_gap_ul_mean_max'
]

feature_list_exp1_both_4 = [

    'Vid_type_mean',
    'Vid_pltform_ML_mean',

    'mean_size_frame_ul_mean_min',
    'mean_size_frame_dl_mean_max',
    'burst_gap_ul_mean_mean',
    'mean_size_frame_dl_mean_mean',
    'mean_gap_frame_ul_mean_max',
    'burst_duration_ul_mean_max',
    'maxserverburstsize_max',
    'maxserverburstrate_min',
    'flow_gap_min',
    'mean_size_frame_uldl_mean_mean',
    'maxserverburstsize_sum',
    'flow_gap_max',
    'Avg_throughput_ul_max',
    'maxclientburstrate_min',
    'burst_size_ul_mean_min',
    'mean_size_frame_dl_mean_sum',
    'flow_gap_mean',
    'Avg_throughput_uldl_max',
    'burst_gap_dl_mean_max',
    'burst_size_uldl_mean_max'
]

feature_list_exp1_both_6 = [

    'Vid_type_mean',
    'Vid_pltform_ML_mean',

    'mean_size_frame_ul_mean_min',
    'mean_size_frame_dl_mean_max',
    'mean_size_frame_dl_mean_mean',
    'mean_size_frame_dl_mean_sum',
    'flow_gap_sum',
    'mean_gap_frame_ul_mean_max',
    'Avg_throughput_uldl_max',
    'flow_gap_max',
    'burst_gap_dl_mean_mean',
    'maxserverburstsize_max',
    'maxserverburstsize_sum',
    'flow_gap_min',
    'mean_size_frame_uldl_mean_mean',
    'maxserverburstrate_mean',
    'burst_num_of_packets_ul_mean_min',
    'mean_gap_frame_ul_mean_mean',
    'burst_duration_ul_mean_max',
    'burst_sizerate_dl_mean_min',
    'burst_gap_ul_mean_mean',
    'flow_gap_mean',
]

feature_list_exp1_both_8 = [

    'Vid_type_mean',
    'Vid_pltform_ML_mean',

    'mean_size_frame_ul_mean_min',
    'mean_size_frame_dl_mean_max',
    'mean_size_frame_dl_mean_sum',
    'burst_duration_ul_mean_max',
    'mean_gap_frame_ul_mean_mean',
    'Avg_throughput_uldl_max',
    'burst_gap_ul_mean_mean',
    'mean_gap_frame_ul_mean_max',
    'mean_size_frame_dl_mean_mean',
    'maxserverburstsize_sum',
    'mean_size_frame_uldl_mean_mean',
    'flow_gap_sum',
    'flow_gap_min',
    'maxserverburstsize_max',
    'Avg_throughput_dl_max',
    'flow_gap_mean',
    # '_num_of_packets_ul_mean_min'
    'burst_sizerate_dl_mean_mean',
    'burst_size_uldl_mean_max',
    'maxserverburstpacket_sum',

]

feature_list_exp1_both_10 = [

    'Vid_type_mean',
    'Vid_pltform_ML_mean',

    'mean_size_frame_dl_mean_max',
    'mean_size_frame_ul_mean_min',
    'mean_size_frame_dl_mean_sum',
    'burst_duration_ul_mean_max',
    'Avg_throughput_uldl_max',
    'mean_gap_frame_ul_mean_mean',
    'mean_gap_frame_ul_mean_max',
    'mean_size_frame_uldl_mean_mean',
    'mean_size_frame_dl_mean_mean',
    'Avg_throughput_dl_max',
    'burst_gap_ul_mean_mean',
    'maxserverburstsize_sum',
    'flow_gap_max',
    'burst_sizerate_dl_mean_mean',
    'maxserverburstsize_max',
    'flow_gap_sum',
    'flow_gap_min',
    'burst_size_ul_mean_sum',
    'mean_size_frame_dl_mean_min',
    'mean_size_frame_uldl_mean_sum'

]

feature_stdpercentile_list_exp1_both = [
    'Vid_type_mean',
    'Vid_pltform_ML_mean',
    # "Vid_number_mean",

    'mean_size_frame_dl_mean_max',
    'mean_size_frame_dl_mean_sum',
    'burst_size_dl_mean_75%',
    'mean_gap_frame_ul_mean_max',
    'mean_size_frame_ul_mean_min',
    'mean_size_frame_dl_mean_75%',
    'Avg_throughput_dl_mean',
    'mean_gap_frame_ul_mean_std',
    'burst_size_dl_mean_std',
    'burst_duration_dl_mean_min',
    'mean_gap_frame_ul_mean_sum',
    'mean_size_frame_ul_mean_75%',
    'Max_rtt_std',
    'maxclientburstrate_min',
    'mean_size_frame_ul_mean_50%',
    'Avg_throughput_dl_50%',
    'burst_num_of_packets_dl_mean_std',
    'burst_duration_ul_mean_max',
    'burst_size_ul_mean_25%',
    'maxclientburstpacket_sum'

    # 'mean_size_frame_dl_mean_max',
    # 'mean_size_frame_dl_mean_sum',
    # 'mean_size_frame_ul_mean_min',
    # 'mean_gap_frame_ul_mean_max'
    # 'mean_size_frame_dl_mean_75%',
    # 'burst_size_dl_mean_75%',
    # 'mean_gap_frame_ul_mean_std',
    # 'mean_gap_frame_ul_mean_sum',
    # 'Avg_throughput_dl_mean',
    # 'mean_size_frame_uldl_mean_max',
    # 'mean_size_frame_ul_mean_75%',
    # 'maxserverbursttime_25%',
    # 'maxserverburstrate_50%',
    # 'burst_duration_dl_mean_min',
    # 'Max_rtt_std',
    # 'maxserverburstrate_75%',
    # 'burst_duration_ul_mean_max',
    # 'mean_size_frame_ul_mean_50%',
    # 'Avg_throughput_ul_75%',
    # 'burst_size_ul_mean_25%'

]

# ========EXP 2===========================
# ========EXP 2===========================

feature_list_exp2_yt = [
    'Vid_type_mean',
    'Vid_pltform_ML_mean',

    'maxserverburstsize_max',
    'Avg_throughput_dl_max',
    'maxclientburstsize_max',
    'flow_gap_sum',
    'flow_gap_max',
    'maxserverbursttime_max',
    'Avg_throughput_dl_sum',
    'maxserverbursttime_mean',
    'Avg_throughput_ul_sum',
    'maxclientbursttime_mean',
    'maxclientburstsize_mean',
    'Avg_throughput_ul_mean',
    'Avg_throughput_ul_max',
    'maxclientbursttime_max',
    'flow_gap_mean',
    'Avg_throughput_dl_mean',
    'maxserverburstsize_mean',
    'maxclientbursttime_sum',
    'maxclientburstsize_sum',
    'maxserverbursttime_sum'

]

feature_stdpercentile_list_exp2_yt = [
    'Vid_type_mean',
    'Vid_pltform_ML_mean',
    # "Vid_number_mean",

    'Avg_throughput_dl_max',
    'maxserverburstsize_max',
    'Avg_throughput_dl_sum',
    'maxserverburstsize_50%',
    'Avg_throughput_dl_75%',
    'maxclientburstsize_max',
    'flow_gap_sum',
    'maxclientbursttime_75%',
    'maxserverburstsize_std',
    'flow_gap_50%',
    'Avg_throughput_dl_min',
    'maxserverbursttime_75%',
    'maxserverbursttime_50%',
    'Avg_throughput_dl_std',
    'maxclientbursttime_50%',
    'maxserverburstsize_25%',
    'Avg_throughput_ul_50%',
    'maxclientbursttime_25%',
    'flow_gap_25%',
    'maxserverbursttime_std'

    # 'maxserverburstsize_max',
    # 'maxserverburstsize_50%',
    # 'Avg_throughput_uldl_75%',
    # 'Avg_throughput_dl_max',
    # 'maxserverbursttime_75%',
    # 'maxclientburstsize_max',
    # 'maxserverburstsize_std',
    # 'Avg_throughput_uldl_min',
    # 'maxserverbursttime_50%',
    # 'flow_gap_sum',
    # 'maxclientbursttime_mean',
    # 'Avg_throughput_dl_sum',
    # 'maxclientbursttime_50%',
    # 'Avg_throughput_uldl_max',
    # 'maxclientbursttime_25%',
    # 'Avg_throughput_uldl_sum',
    # 'Avg_throughput_ul_std',
    # 'Avg_throughput_ul_50%',
    # 'maxserverburstsize_25%',
    # 'maxclientbursttime_75%',

]

feature_list_exp2_fb = [

    'Vid_type_mean',
    'Avg_throughput_dl_max',
    'maxserverburstsize_sum',
    'flow_gap_mean',
    'Avg_throughput_ul_sum',
    'maxclientburstsize_max',
    'Avg_throughput_dl_sum',
    'flow_gap_max',
    'maxclientburstsize_sum',
    'maxserverburstsize_mean',
    'Avg_throughput_ul_mean',
    'Avg_throughput_ul_max',
    'Packet_loss_mean',
    'flow_ct',
    'maxclientburstsize_mean',
    'maxserverburstsize_max',
    'flow_gap_sum',
    'Avg_rtt_mean',
    'maxserverbursttime_max',
    'maxclientbursttime_mean',
    'maxserverbursttime_mean'
]
feature_stdpercentile_list_exp2_fb = [
    'Vid_type_mean',
    'Vid_pltform_ML_mean',
    # "Vid_number_mean",

    'maxserverburstsize_75%',
    'Avg_throughput_dl_50%',
    'flow_gap_min',
    'Avg_throughput_ul_25%',
    'maxclientburstsize_sum',
    'maxserverburstsize_sum',
    'Avg_throughput_dl_mean',
    'Avg_throughput_dl_25%',
    'maxserverbursttime_50%',
    'Avg_throughput_ul_min',
    'maxclientbursttime_50%',
    'Avg_throughput_dl_std',
    'Avg_throughput_ul_max',
    'Avg_throughput_dl_max',
    'flow_ct',
    'maxclientburstsize_max',
    'Avg_throughput_ul_50%',
    'Avg_throughput_ul_mean',
    'flow_gap_std',
    'flow_gap_75%',
]

feature_list_exp2_both = [
    'Vid_type_mean',
    'maxclientburstsize_max',
    'Avg_throughput_dl_max',
    'maxserverburstsize_max',
    'maxserverburstsize_sum',
    'Avg_throughput_ul_sum',
    'flow_gap_max',
    'flow_gap_sum',
    'Avg_throughput_dl_sum',
    'Avg_throughput_ul_max',
    'maxclientbursttime_mean',
    'maxserverbursttime_mean',
    'maxserverbursttime_max',
    'Avg_throughput_ul_mean',
    'Avg_throughput_dl_mean',
    'flow_gap_mean',
    'maxclientburstsize_sum',
    'maxclientburstsize_mean',
    'maxserverburstsize_mean',
    'Max_rtt_mean',
    'maxclientbursttime_max'
]
feature_stdpercentile_list_exp2_both = [
    'Vid_type_mean',
    'Vid_pltform_ML_mean',
    # "Vid_number_mean",

    'maxserverburstsize_75%',
    'Avg_throughput_dl_std',
    'Avg_throughput_dl_50%',
    'Avg_throughput_dl_max',
    'maxserverburstsize_max',
    'maxserverburstsize_sum',
    'Avg_throughput_dl_min',
    'Avg_throughput_dl_75%',
    'Avg_throughput_ul_25%',
    'maxclientburstsize_max',
    'maxserverburstsize_50%',
    'flow_gap_min',
    'Avg_throughput_ul_50%',
    'Avg_throughput_dl_mean',
    'maxserverburstsize_std',
    'maxserverbursttime_75%',
    'flow_gap_25%',
    'maxserverbursttime_25%',
    'Avg_throughput_dl_sum',
    'Avg_throughput_ul_75%',

    # 'maxserverburstsize_75%',
    #  'maxserverburstsize_sum',
    #  'maxserverburstsize_max',
    #  'maxserverburstsize_50%',
    #  'Avg_throughput_ul_25%' ,
    #  'Avg_throughput_uldl_min',
    #  'maxclientburstsize_max',
    #  'Avg_throughput_ul_50%',
    #  'Avg_throughput_uldl_75%',
    #  'Avg_throughput_dl_std',
    #  'maxserverbursttime_75%',
    #  'flow_gap_min',
    #  'maxserverburstsize_std',
    #  'Avg_throughput_uldl_std',
    #  'Avg_throughput_dl_50%',
    #  'Avg_throughput_uldl_50%',
    #  'Avg_throughput_dl_min',
    #  'maxserverbursttime_25%',
    #  'flow_gap_25%',
    #  'flow_gap_75%'

]

# ========EXP 3===========================
# ========EXP 3===========================

feature_list_exp3_yt = [
    'Vid_type_mean',
    'flow_gap_sum',
    'burst_size_dl_mean_max',
    'Packets_dl_sum',
    'mean_size_frame_dl_mean_max',
    'mean_size_frame_ul_mean_mean',
    'mean_size_frame_ul_mean_sum',
    'Bytes_dl_max',
    'Bytes_ul_max',
    'mean_gap_frame_ul_mean_sum',
    'Bytes_dl_sum',
    'Bytes_ul_sum',
    'burst_gap_dl_mean_sum',
    'Avg_throughput_dl_sum',
    'Avg_throughput_dl_max',
    'maxclientbursttime_mean',
    # 'maxserverburstsize_max',
    # 'burst_sizerate_dl_mean_mean',
    # 'mean_gap_frame_ul_mean_max',
    # 'burst_duration_ul_mean_max',
    # 'Avg_throughput_ul_max'
]

feature_stdpercentile_list_exp3_yt = [
    'Vid_type_mean',
    'Vid_pltform_ML_mean',
    "Vid_number_mean",

    'Packets_dl_sum',
    'burst_size_ul_mean_25%',
    'mean_size_frame_dl_mean_max',
    'flow_gap_sum',
    'Bytes_dl_sum',
    'maxclientbursttime_75%',
    'Bytes_dl_max',
    'mean_size_frame_ul_mean_min',
    'maxserverburstrate_75%',
    'Bytes_ul_max',
    'burst_duration_dl_mean_min',
    'mean_size_frame_ul_mean_75%',
    'burst_sizerate_dl_mean_50%',
    'mean_gap_frame_ul_mean_max',
    'Bytes_dl_50%',
    'Packets_dl_max',
    'flow_gap_25%',
    'Bytes_ul_sum',
    'Packets_dl_min',
    'burst_size_dl_mean_max'

    # 'Packets_uldl_sum',
    # 'burst_size_ul_mean_25%',
    # 'flow_gap_sum',
    # 'maxclientbursttime_75%',
    # 'mean_size_frame_dl_mean_max',
    # 'Packets_uldl_max',
    # 'maxserverburstrate_75%',
    # 'flow_gap_25%',
    # 'mean_gap_frame_ul_mean_max',
    # 'Bytes_dl_50%',
    # 'burst_duration_dl_mean_min',
    # 'mean_size_frame_ul_mean_75%',
    # 'mean_size_frame_ul_mean_min',
    # 'Bytes_ul_max',
    # 'maxserverbursttime_50%',
    # 'mean_gap_frame_ul_mean_sum',
    # 'Bytes_ul_75%',
    # 'Bytes_ul_sum',
    # 'burst_sizerate_dl_mean_50%',
    # 'mean_size_frame_uldl_mean_max',

]

feature_list_exp3_fb = [
    'Vid_type_mean',
    'mean_size_frame_dl_mean_sum',
    'mean_size_frame_dl_mean_max',
    'mean_size_frame_dl_mean_mean',
    'Bytes_dl_mean',
    'Packets_ul_mean',
    'burst_size_dl_mean_max',
    'Bytes_ul_mean',
    'burst_size_dl_mean_sum',
    'maxserverburstsize_mean',
    'mean_size_frame_ul_mean_max',
    'burst_sizerate_dl_mean_mean',
    'maxserverburstsize_sum',
    'burst_gap_ul_mean_mean',
    'flow_gap_max',
    'maxclientburstsize_mean',
    'burst_size_ul_mean_mean',
    'maxserverburstpacket_mean',
    'burst_num_of_packets_dl_mean_sum',
    'mean_gap_frame_dl_mean_mean',
    'mean_size_frame_ul_mean_sum'
]

feature_stdpercentile_list_exp3_fb = [
    'Vid_type_mean',
    'Vid_pltform_ML_mean',
    "Vid_number_mean",

    'mean_size_frame_dl_mean_max',
    'mean_size_frame_dl_mean_sum',
    'mean_size_frame_dl_mean_75%',
    'Packets_dl_75%',
    'Bytes_dl_75%',
    'Bytes_dl_mean',
    'burst_size_dl_mean_75%',
    'Packets_ul_mean',
    'burst_num_of_packets_ul_mean_std',
    'burst_num_of_packets_dl_mean_75%',
    'burst_size_dl_mean_std',
    'burst_num_of_packets_dl_mean_sum',
    'Bytes_ul_mean',
    'maxserverbursttime_25%',
    'Avg_throughput_dl_sum',
    'maxclientburstpacket_std',
    'maxclientburstsize_std',
    'burst_size_dl_mean_max',
    'burst_num_of_packets_dl_mean_std',
    'mean_size_frame_ul_mean_50%'

    # 'mean_size_frame_dl_mean_sum',
    # 'mean_size_frame_dl_mean_max',
    # 'mean_size_frame_uldl_mean_max',
    # 'mean_size_frame_dl_mean_75%',
    # 'Packets_dl_75%',
    # 'mean_size_frame_uldl_mean_75%',
    # 'Bytes_dl_75%',
    # 'Packets_ul_mean',
    # 'burst_size_uldl_mean_std',
    # 'burst_num_of_packets_ul_mean_std',
    # 'Packets_uldl_mean',
    # 'burst_num_of_packets_dl_mean_75%',
    # 'burst_size_dl_mean_75%',
    # 'Bytes_ul_mean',
    # 'Bytes_uldl_75%',
    # 'maxclientburstpacket_std',
    # 'Bytes_dl_mean',
    # 'Max_rtt_std',
    # 'mean_size_frame_ul_mean_50%',
    # 'maxserverbursttime_25%'

]

feature_list_exp3_both = [
    'Vid_type_mean',
    'mean_size_frame_dl_mean_max',
    'Bytes_dl_mean',
    'mean_size_frame_dl_mean_sum',
    'mean_size_frame_dl_mean_mean',
    'burst_gap_ul_mean_mean',
    'maxclientburstsize_mean',
    'burst_num_of_packets_dl_mean_sum',
    'mean_size_frame_ul_mean_sum',
    'Bytes_ul_mean',
    'Packets_ul_mean',
    'mean_gap_frame_dl_mean_mean',
    'burst_size_dl_mean_max',
    'flow_gap_max',
    'burst_sizerate_dl_mean_mean',
    'maxserverburstsize_sum',
    'mean_size_frame_ul_mean_max',
    'burst_size_dl_mean_sum',
    'burst_size_ul_mean_mean',
    'maxserverburstsize_mean',
    'maxserverburstpacket_mean'
]

feature_stdpercentile_list_exp3_both = [
    'Vid_type_mean',
    'Vid_pltform_ML_mean',
    "Vid_number_mean",

    'mean_size_frame_dl_mean_sum',
    'mean_size_frame_dl_mean_max',
    'mean_size_frame_dl_mean_75%',
    'Bytes_dl_75%',
    'Bytes_ul_75%',
    'mean_gap_frame_ul_mean_max',
    'mean_gap_frame_ul_mean_sum',
    'Bytes_dl_sum',
    'Bytes_dl_std',
    'flow_gap_sum',
    'mean_gap_frame_ul_mean_std',
    'mean_size_frame_ul_mean_min',
    'Avg_throughput_dl_mean',
    'Max_rtt_std',
    'burst_size_dl_mean_std',
    'Packets_dl_sum',
    'Packets_dl_mean',
    'mean_size_frame_ul_mean_75%',
    'burst_duration_dl_mean_min',
    'burst_size_dl_mean_75%'

    # 'mean_size_frame_dl_mean_sum',
    # 'mean_size_frame_dl_mean_max',
    # 'mean_gap_frame_ul_mean_max',
    # 'mean_size_frame_dl_mean_75%',
    # 'Bytes_ul_75%',
    # 'mean_gap_frame_ul_mean_sum',
    # 'flow_gap_sum',
    # 'Bytes_dl_75%',
    # 'Bytes_uldl_75%',
    # 'burst_duration_dl_mean_min',
    # 'mean_gap_frame_ul_mean_std',
    # 'mean_size_frame_uldl_mean_max',
    # 'mean_size_frame_ul_mean_min',
    # 'Avg_throughput_dl_mean',
    # 'burst_size_dl_mean_75%',
    # 'Packets_uldl_sum',
    # 'Max_rtt_std',
    # 'maxserverburstrate_75%',
    # # 'num_of_packets_uldl_mean_sum',
    # 'maxclientburstsize_std'

]

# ========EXP 4===========================
# ========EXP 4===========================

feature_list_exp4_yt = [
    'Vid_type_mean',
    'flow_gap_sum',
    'maxserverburstsize_max',
    'Packets_ul_max',
    'maxserverburstsize_mean',
    'maxclientbursttime_mean',
    'maxclientburstsize_max',
    'Bytes_ul_max',
    'Bytes_dl_sum',
    'Packets_dl_sum',
    'maxserverbursttime_mean',
    'Bytes_dl_max',
    'Avg_throughput_dl_max',
    'Bytes_ul_sum',
    'flow_gap_max',
    'maxclientburstsize_mean',
    # 'Packets_ul_sum',
    # 'Bytes_ul_mean',
    # 'Avg_throughput_ul_sum',
    # 'maxclientbursttime_sum',
    # 'Avg_rtt_sum'
]

feature_stdpercentile_list_exp4_yt = [
    'Vid_type_mean',
    'Vid_pltform_ML_mean',
    "Vid_number_mean",

    'flow_gap_sum',
    'maxclientbursttime_75%',
    'Bytes_ul_75%',
    'Bytes_dl_sum',
    'Packets_dl_sum',
    'flow_gap_25%',
    'Bytes_dl_min',
    'Packets_dl_min',
    'Packets_ul_max',
    'Bytes_dl_max',
    'Bytes_ul_max',
    'maxserverbursttime_50%',
    'Bytes_ul_sum',
    'flow_gap_75%',
    'Packets_dl_max',
    'Packets_ul_25%',
    'flow_gap_50%',
    'maxclientburstsize_std',
    'Packets_ul_sum',
    'maxserverburstsize_max'
]

feature_list_exp4_fb = [
    'Vid_type_mean',
    'maxserverburstsize_sum',
    'Avg_throughput_dl_max',
    'Bytes_dl_mean',
    'Avg_throughput_ul_sum',
    'maxclientburstsize_max',
    'maxserverburstsize_max',
    'maxclientburstsize_sum',
    'flow_gap_mean',
    'Avg_throughput_ul_max',
    'maxclientburstsize_mean',
    'Bytes_ul_mean',
    'maxserverburstsize_mean',
    'flow_gap_max',
    'Packet_loss_mean',
    'Avg_rtt_mean',
    # 'maxclientbursttime_sum',
    # 'Avg_throughput_dl_sum',
    # 'maxserverbursttime_mean',
    # 'Avg_rtt_max',
    # 'Max_rtt_mean'

]

feature_stdpercentile_list_exp4_fb = [
    'Vid_type_mean',
    'Vid_pltform_ML_mean',
    "Vid_number_mean",

    'Bytes_dl_75%',
    'Bytes_dl_mean',
    'Avg_throughput_ul_min',
    'Packets_dl_75%',
    'maxserverburstsize_sum',
    'Bytes_ul_mean',
    'maxclientburstsize_sum',
    'Max_rtt_std',
    'Avg_throughput_ul_25%',
    'maxserverbursttime_50%',
    'flow_gap_min',
    'Avg_throughput_dl_50%',
    'Avg_throughput_ul_max',
    'Packets_dl_mean',
    'Avg_throughput_dl_mean',
    'maxserverburstsize_75%',
    'Bytes_dl_min',
    'flow_ct',
    'Packet_loss_mean',
    'flow_gap_25%'
]

feature_list_exp4_both = [
    'Vid_type_mean',
    'maxserverburstsize_sum',
    'flow_gap_sum',
    'maxclientburstsize_max',
    'Bytes_dl_mean',
    'Max_rtt_mean',
    'flow_gap_max',
    'Avg_rtt_sum',
    'maxserverburstsize_max',
    'Avg_throughput_ul_sum',
    'Bytes_ul_mean',
    'maxclientburstsize_sum',
    'maxserverburstsize_mean',
    'maxserverbursttime_max',
    'Avg_throughput_ul_mean',
    'Packets_ul_mean',
    'Packets_dl_mean',
    'Packets_ul_sum',
    'maxclientbursttime_mean',
    'maxclientburstsize_mean',
    'flow_gap_mean'
]
feature_stdpercentile_list_exp4_both = [
    'Vid_type_mean',
    'Vid_pltform_ML_mean',
    "Vid_number_mean",

    'Bytes_dl_75%',
    'maxserverburstsize_sum',
    'flow_gap_sum',
    'Bytes_ul_75%',
    'Avg_throughput_dl_min',
    'Bytes_dl_mean',
    'Avg_throughput_dl_50%',
    'Bytes_dl_std',
    'Bytes_dl_sum',
    'flow_gap_25%',
    'maxserverbursttime_75%',
    'maxserverburstsize_max',
    'Avg_throughput_ul_min',
    'Avg_throughput_ul_25%',
    'Max_rtt_std',
    'maxclientbursttime_75%',
    'Avg_throughput_dl_25%',
    'Packets_dl_mean',
    'maxclientburstsize_max',
    'Max_rtt_25%'
]

# when selecting the features before derive statistical values


features_to_select_exp1 = [
    'Vid_type',
    'Vid_pltform',
    "Vid_pltform_ML",
    "Vid_number",
    'Vid_begin',
    'Vid_end',

    'Avg_throughput_uldl',
    'mean_size_frame_uldl_mean',
    'burst_size_uldl_mean',
    'burst_num_of_packets_uldl_mean',

    'Avg_throughput_dl',
    'Avg_throughput_ul',
    'maxserverburstsize',
    'maxserverbursttime',
    "maxserverburstrate",
    "maxserverburstpacket",
    "maxclientburstsize",
    "maxclientbursttime",
    'maxclientburstrate',
    'maxclientburstpacket',

    'burst_duration_ul_mean',
    'burst_gap_ul_mean',
    'burst_sizerate_ul_mean',
    'mean_gap_frame_ul_mean',
    'mean_size_frame_ul_mean',
    'burst_size_ul_mean',
    'burst_num_of_packets_ul_mean',

    'burst_duration_dl_mean',
    'burst_gap_dl_mean',
    'burst_sizerate_dl_mean',
    'mean_gap_frame_dl_mean',
    'mean_size_frame_dl_mean',
    'burst_size_dl_mean',
    'burst_num_of_packets_dl_mean',

    'Max_rtt',
    'Avg_rtt',
    'Packet_loss'
]

features_to_select_exp2 = [
    'Vid_type',
    'Vid_pltform',
    "Vid_pltform_ML",
    "Vid_number",
    'Vid_begin',
    'Vid_end',

    'Avg_throughput_uldl',

    'Avg_throughput_dl',
    'Avg_throughput_ul',
    'maxserverburstsize',
    'maxserverbursttime',
    'maxclientburstsize',
    'maxclientbursttime',
    'Max_rtt',
    'Avg_rtt',
    'Packet_loss'
]

features_to_select_exp3 = [
    'Vid_type',
    'Vid_pltform',
    "Vid_number",
    "Vid_pltform_ML",
    'Vid_begin',
    'Vid_end',

    "Bytes_dl",
    "Bytes_ul",
    "Packets_dl",
    "Packets_ul",

    'Bytes_uldl',
    'Packets_uldl',
    'Avg_throughput_uldl',
    'mean_size_frame_uldl_mean',
    'burst_size_uldl_mean',
    'burst_num_of_packets_uldl_mean',

    'Avg_throughput_dl',
    'Avg_throughput_ul',
    'maxserverburstsize',
    'maxserverbursttime',
    "maxserverburstrate",
    "maxserverburstpacket",
    "maxclientburstsize",
    "maxclientbursttime",
    'maxclientburstrate',
    'maxclientburstpacket',

    'burst_duration_ul_mean',
    'burst_gap_ul_mean',
    'burst_sizerate_ul_mean',
    'mean_gap_frame_ul_mean',
    'mean_size_frame_ul_mean',
    'burst_size_ul_mean',
    'burst_num_of_packets_ul_mean',

    'burst_duration_dl_mean',
    'burst_gap_dl_mean',
    'burst_sizerate_dl_mean',
    'mean_gap_frame_dl_mean',
    'mean_size_frame_dl_mean',
    'burst_size_dl_mean',
    'burst_num_of_packets_dl_mean',

    'Max_rtt',
    'Avg_rtt',
    'Packet_loss'
]

features_to_select_exp4 = [
    'Vid_type',
    'Vid_pltform',
    "Vid_pltform_ML",
    "Vid_number",
    'Vid_begin',
    'Vid_end',

    "Bytes_dl",
    "Bytes_ul",
    "Packets_dl",
    "Packets_ul",

    'Bytes_uldl',
    'Packets_uldl',
    'Avg_throughput_uldl',

    'Avg_throughput_dl',
    'Avg_throughput_ul',
    'maxserverburstsize',
    'maxserverbursttime',
    'maxclientburstsize',
    'maxclientbursttime',
    'Max_rtt',

    'Avg_rtt',
    'Packet_loss'
]

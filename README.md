# 360norvic
This repository holds the artifacts to reproduce the main results in the paper, "360Norvic: 360-Degree Video Classification from Mobile Encrypted Video Traffic" to classify 360-degree videos from mobile encrytped video traffic. There three main evaluations
* Offline classification - DS-pkt
* Offline classification - DS-flw
* Near-realtime classification - DS-pkt

(Despite the slight changes of performance of the classification results, the trends of the result variation are observable).

## Requirements
Following packages are required.

* Numpy				1.18.1
*	Pandas			1.0.3
*	scipy				1.4.1
*	sklearn			0.22.1

## Offline classification - DS-pkt (Section 4.3, Section 5.1 (DS-pkt) in the paper)
Offline evaluation for three traffic types namely YouTube (YT), Facebook (FB) and  BOTH (combining YT and FB) using **packet** level data. 

### Datasets
* processed_data_DS_pkt: processed DS-pkt data for the bins (5s long with 1s stride) in 20, 30, 60, 90 and 120s video durations. Each row of a given .csv file presents the summary statistics of the bins of a given trace.
* clf_results_DS_pkt_main: output of the classification by XGBoost model for different durations and number of different train/test splits of the data.

### Implementation
Run `DS_pkt_main_clf.py` giving the followgin arguments appropriately
* `--t_type`              traffic type
* `--duration`            duration of the trace  (default = 60s)
* `--num_of_iterations`   num of different train/test splits (default = 20)
* `--path`                current working driectory

sample implementation

` python3 DS_pkt_main_clf.py --t_type 'YT'  --num_of_iterations 5 --duration 20 --path <folder path> `

`--help` for further support

## Offline classification - DS-flw (Section 4.3, Section 5.2 (DS-flw) in the paper)
Offline evaluation for three traffic types namely YouTube (YT), Facebook (FB) and  BOTH (combining YT and FB) using **flow** level data. 

### Datasets
* processed_data_DS_flw: processed DS-flow data for the number of flows (1, 2, 4, 6, 8, 10, all) sorted according to the total bytes dl for each trace. Each row of a given .csv file presents the summary statistics of the flows of a given trace.
* clf_results_DS_pkt_main: output of the classification by XGBoost model for different number of flows and number of different train/test splits of the data.

### Implementation
Run `DS_flw_main_clf.py` giving the followgin arguments appropriately
* `--t_type`              traffic type
* `--num_of_flows`        number of flows for each trace. select one value from {1,2,4,6,8,10,100 (represents 'all' scenario)}
* `--num_of_trials`       num of different train/test splits (default = 20)
* `--path`                current working driectory

sample implementation

` python3 DS_flw_main_clf.py --t_type 'FB' --num_of_flows 6 --num_of_trials 5 --path <folder path> `

`--help` for further support

## Near-realtime classificaiton (Section 4.3, Section 5.2 in the paper)
Near-realtime classification for three traffic types YT, FB or BOTH, using **packet** level data. Unlike offline evalutation, first, prediction (360 or Normal video) is  given for every bin of the trace using a XGBoost model. Secondly, majority voting is applied on groups of XGBoost output to get the final decision every 5s with an increasing accuracy. Note that entire near-realtime model can be considered as (XGBoost+MODE).

### Datasets
* processed_data_DS_pkt_near_realtime: binned trace data (bin size = 5s, stride/step size = 1s)
* clf_result_DS_pkt_near_realtime
    * XGBoost_prediction_processed: sample XGBoost ouput
    * MODE_prediction_processed: sample MODE (majority voting) output
    * XGBoost_prediction: XGBoost output after running the related code
    * MODE_prediction: final output after the MODE operation running the related code segment

### implementation
Run `DS_pkt_near_realtime.py` giving the following arguments appropriately. Final output will be given for the entire video duration. 
* `--t_type`                  traffic type
* `--num_of_rounds_xgboost`   num of XGBoost iterations with different train/test splits. Increasing this parameter will generalize the results. 
* `--run_xgboost`             enable running the xgboost
* `--run_mode_operation`      enable running the majority voting operation
* `--already_processed`       run the code with sample output data. Since, XGBoost prediction may take longer time, users can directly run majority voting by enabling this arguement along with `--run_mode_operation`.
* `--path`                  current working driectory

Note: Before running the mode operation, it is essential to run the XGBoost classification for each bin for the considered traffic type. For 'BOTH' traffic type, both YT and FB XGBoost prediction should be taken. You can only run XGBoost operation for either FB or YT, but not for BOTH.

sample implementation
* run the XGBoost operation for FB 

` python3 DS_pkt_near_realtime.py --t_type 'FB' --num_of_rounds_xgboost 10 --run_xgboost --path <folder path> `

* run the XGBoost and MODE operation for FB 

` python3 DS_pkt_near_realtime.py --t_type 'FB' --num_of_rounds_xgboost 10 --run_xgboost --run_mode_operation  --path <folder path> `

* run the MODE operation using sample XGBoost prediction

` python3 DS_pkt_near_realtime.py --t_type 'FB' --run_mode_operation --already_processed  --path <folder path> `

Please cite the our work if you intend to use our dataset.

*Chamara Kattadige, Aravindh Raman, Kanchana Thilakarathna, Andra Lutu, and Diego Perino. 2021.  360NorVic: 360-Degree Video Classification from Mobile Encrypted Video Traffic (in press). In Workshop on Network and Operating System Support for Digital Audio and Video (NOSSDAV ’21).*

Latex bib.

`@inproceedings{360Norivc,`\
  `title={360NorVic: 360-Degree Video Classification from Mobile Encrypted Video Traffic (in press)},`\
  `author={Kattadige, Chamara and Raman, Aravindh  and Thilakarathna, Kanchana  and Lutu, Andra  and Perino, Diego },`\
  `booktitle={Workshop on Network and Operating System Support for Digital Audio and Video (NOSSDAV ’21)},`\
  `year={2021}`
`}`








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

` python3 DS_pkt_main_clf.py --t_type 'YT'  --num_of_iterations 5 --duration 20 --path <desired path> `

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

` python3 DS_flw_main_clf.py --t_type 'FB' --num_of_flows 6 --num_of_trials 5 --path <desired path> `

`--help` for further support

## Near-realtime classificaiton (Section 4.3, Section 5.2 in the paper)
Near-realtime classification for three traffic types YT, FB or BOTH, using **packet** level data. Unlike offline evalutation, prediction (360 or Normal video) is  given for every bin of the trace. 









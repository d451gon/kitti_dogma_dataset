# kitti_dogma_dataset

## Introduction
This dataset contains dynamic occupancy grid (DOGMa) estimations for the KITTI 3D object detection dataset. It was obtained by running the CMCDOT tracking algorithm (https://hal.archives-ouvertes.fr/hal-01205298/) on the KITTI dataset raw sequences and then selecting the samples contained in the 3D object detection dataset.

The dataset is hosted at: https://archive.org/details/kitti_dogma_dataset
As stated in the hosting site (Internet Archive), the usage license is CC BY-NC-SA 4.0.

<img src="/multimedia/state_grids.gif"/>

## Data description
We provide the DOGMa estimations for the training/validation samples of the KITTI 3D object detection dataset. The test samples have no mapping to the raw sequences so their grids could not be obtained.

Out of the 7481 training/validation samples, we provide the corresponding DOGMas for 7275. The missing 206 grids correspond to samples at the beggining of the raw sequences (where the filter had not yet converged), or to a sequence with odometry issues (0093@2011_09_26). The list of missing grids can be found in the following [file](grids_not_found_summary.log).

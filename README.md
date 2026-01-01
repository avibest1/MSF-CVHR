# Multi-Scale Feature Fusion with Cross-View Head Re-Identification Module for Crowd-Counting

---

This repo is the implementation of **Cross-View Head Re-Identification Module for Crowd-Counting**

## Description
The single and cross-view crowd counting in complex scenarios remains challenging due to severe occlusion, perspective distortion, and the problem of avoiding redundant counting across camera views. This paper presents a novel crowd counting network that efficiently addresses these challenges and accurately counts in single and cross-view complex scenes. The model integrates a hybrid attention module to capture precise spatial and channel features, a multi-scale feature fusion module to capture granular features and broader contextual details from highly dense and sparse crowd images, and a cross-view head re-identification module that integrates feature representation with appearance similarity and geometric weighted similarity that transforms the data and prioritize angular similarity over magnitude-based comparison, which is most essential when dealing with diverse camera viewpoints extracted features. By jointly modeling intra-view and inter-view, the model achieves superior capability in handling crowd counting in single-view and cross-view settings. This research conducts extensive experiments on single-view counting using the ShanghaiTech, UCF-CC50, UCF-QNRF, and JHU-Crowd++ benchmark datasets, as well as on cross-view counting using the WildTrack, MVOR, and MultiviewX datasets. The experimental results with ablation studies validate the model’s localization accuracy, robustness, and counting precision for both single-view and cross-view crowd counting. 

## Model Architecture

<p align="center">
  <img src="https://raw.githubusercontent.com/avibest1/MSF-CVHR/fa046fb80b17614fc74efe43674c96be0377938a/figures/Architecture.jpg" width="700"><br>
  <em>Figure: Architecture of the proposed MSF-CVHR framework.</em>
</p>

# Getting Started
## Preparation
-  Prerequisites
    - Python ≥ 3.7
    - PyTorch ≥ 1.6
    - other libs in ```requirements.txt```, run ```pip install -r requirements.txt```.
-  Code
    - Clone this repo in the directory (```Root/MSF-CVHR```):
  
- Datasets
    - Download Wildtrack dataset from this [link](https://www.epfl.ch/labs/cvlab/data/data-wildtrack/).
    - Download MVOR dataset from this [link](https://camma.unistra.fr/datasets/).
    - Download MultiviewX dataset from this [link](https://opendatalab.com/OpenDataLab/MultiviewX/explore/main).
    - Unzip ```*zip``` files in turns and place ```datasets*``` into the folder (```dataset_prepare/Cross-View```). 

 
    - If you want to reproduce the results on Shanghai Tech Part A/B , UCF-QNRF, UCF_CC_50 and JHU-Crowd++ datasets for single view, Just place datasets into the folder (```dataset_prepare/Single-View```)   
  
  - Finally, the folder tree is below:
 ```
  -- ProcessedData
  |-- Cross-View
  |-- Wildtrack
	 |-- image_subsets
            |   |-- C1
			|   |-- 00000000.png
			|   |-- 00000005.png
			|   |-- ...
			|   |-- 00002000.png
            |   |-- C2
			|   |-- 00000000.png
			|   |-- 00000005.png
			|   |-- ...
			|   |-- 00002000.png
            ....................
            ....................
            |   |-- C7
			|   |-- 00000000.png
			|   |-- 00000005.png
			|   |-- ...
			|   |-- 00002000.png

     |-- annotations_positions
			|   |-- 00000000.json
			|   |-- 00000005.json
			|   |-- ...
			|   |-- 00001995.json
			|-- train.txt
			|-- val.txt
			|-- test.txt
			|-- val_gt_loc.txt

 ```

## Training

python train.py \

     --img 400 \
     --batch 16 \
     --epochs 150 \
     --data {dataset.location}/data.yaml \
     --weights MSF-CVHR.pt \
     --name MSF-CVHR_results \
     --cache
  
- The validtion on Wildtrack, the table is shown as follows:

| Methods              | AP   | FPR-95 | P     | R     | ACC   | IPAA-100 | IPAA-90 | IPAA-80 |
|----------------------|------|--------|-------|-------|-------|----------|----------|----------|
| OSNET [46]           | 16.81| 92.08  | 28.27 | 29.67 | 37.55 | 0.00     | 0.48     | 3.21     |
| MvMHAT [47]          | 4.45 | 94.13  | 5.97  | 6.28  | 22.37 | 0.00     | 0.48     | 1.55     |
| OSNET+ESC [48]       | 59.53| 15.33  | 78.12 | 79.08 | 82.12 | 26.43    | 39.40    | 66.68    |
| GNN_CCA [49]         | 4.13 | 93.30  | –     | 0.00  | 36.82 | 0.00     | 2.14     | 14.41    |
| ASNet [50]           | 73.40| 8.30   | –     | –     | –     | 32.10    | –        | –        |
| ViT-P3DE [51]        | 70.45| 5.83   | 86.91 | 87.01 | 89.48 | 35.48    | 53.10    | 84.17    |
| MVA [52]             | 56.68| 11.18  | 92.31 | 94.34 | 91.73 | 54.64    | 65.60    | 86.55    |
| **MSF-CVHR (Ours)**  | **65.40**| **6.24** | **93.12** | **94.82** | **90.84** | **54.62** | **68.30** | **87.36** |



- The sub images are the input image, GT, prediction map,localization result, and pixel-level threshold, respectively:
   ![val_curve](./figures/vis.png)
   
Tips: The training process takes **~50 hours** on NWPU datasets with **two TITAN RTX (48GB Memory)**. 


## Testing and Submitting

- Modify some key parameters in ```test.py```: 
  - ```netName```.  
  -  ```model_path```.  
- Run ```python test.py```. Then the output file (```*_*_test.txt```) will be generated, which can be directly submitted to [CrowdBenchmark](https://www.crowdbenchmark.com/nwpucrowdloc.html)

## Visualization on the val set
- Modify some key parameters in ```test.py```: 
  - ```test_list = 'val.txt'```
  - ```netName```.  
  -  ```model_path```.  
- Run ```python test.py```. Then the output file (```*_*_val.txt```) will be generated.
- Modify some key parameters in ```vis4val.py```: 
  - ```pred_file```.  
- Run  ```python vis4val.py```. 

# Performance

The results (F1, Pre., Rec. under the `sigma_l`) and [pre-trained models](https://mailnwpueducn-my.sharepoint.com/:f:/g/personal/gjy3035_mail_nwpu_edu_cn/EliCeOckaZVBgez6n8ZWvr4BNdwPauFJgbm88MGhHid25w?e=rtogwc) on NWPU val set, UCF-QNRF, SHT A, SHT B, and FDST:

|   Method   |  NWPU val  |  UCF-QNRF  |  SHT A  | 
|------------|-------|-------|--------|
| Paper:  VGG+FPN [2,3]| 77.0/80.2/74.1 | **68.8**/78.2/61.5 | **72.5**/72.6/72.5 | 
| This Repo's Reproduction:  VGG+FPN [2,3]| **77.1**/82.5/72.3| 67.8/75.7/61.5 | 71.6/75.9/67.8 |  
| Paper:  HRNet [1]   | **80.2**/84.1/76.6| **72.0**/79.3/65.9 |  73.9/79.8/68.7  | 
| This Repo's Reproduction:  HRNet [1]   | 79.8/83.4/76.5 |  **72.0**/78.7/66.4  | **76.1**/79.1/73.3 |

|   Method   |  SHT B  |  FDST |  JHU  |
|------------|---------|-------|-------|
| Paper:  VGG+FPN [2,3]|   80.2/84.9/76.0  | 93.1/92.7/93.5 | - |
| This Repo's Reproduction:  VGG+FPN [2,3] |  **81.7**/88.5/75.9 | **93.9**/94.7/93.1| 61.8/73.2/53.5 |
| Paper:  HRNet [1]   | **86.2**/90.7/82.1  |  95.5/95.3/95.8  | 62.5/74.0/54.2 |
| This Repo's Reproduction:  HRNet [1]   | 86.0/91.5/81.0 | **95.7**/96.9 /94.4 | **64.0**/73.3/56.8 |

**References**
1. Deep High-Resolution Representation Learning for Visual Recognition, T-PAMI, 2019.
2. Very Deep Convolutional Networks for Large-scale Image Recognition, arXiv, 2014.
3. Feature Pyramid Networks for Object Detection, CVPR, 2017. 

About the leaderboard on the test set, please visit [Crowd benchmark](https://www.crowdbenchmark.com/nwpucrowdloc.html).  Our submissions are the [IIM(HRNet)](https://www.crowdbenchmark.com/resultldetail.html?rid=11) and [IIM (VGG16)](https://www.crowdbenchmark.com/resultldetail.html?rid=10).



# Video Demo

We test the pretrained HR Net model on the NWPU dataset in a real-world subway scene. Please visit [bilibili](https://www.bilibili.com/video/BV1K541157MK) or [YouTube](https://www.youtube.com/watch?v=GqOMgjUkbsI) to watch the video demonstration.
![val_curve](./figures/vid.png)
# Citation
If you find this project is useful for your research, please cite:
```
@article{gao2020learning,
  title={Learning Independent Instance Maps for Crowd Localization},
  author={Gao, Junyu and Han, Tao and Yuan, Yuan and Wang, Qi},
  journal={arXiv preprint arXiv:2012.04164},
  year={2020}
}
```

Our code borrows a lot from the C^3 Framework, and you may cite:
```
@article{gao2019c,
  title={C$^3$ Framework: An Open-source PyTorch Code for Crowd Counting},
  author={Gao, Junyu and Lin, Wei and Zhao, Bin and Wang, Dong and Gao, Chenyu and Wen, Jun},
  journal={arXiv preprint arXiv:1907.02724},
  year={2019}
}
```
If you use pre-trained models in this repo (HR Net, VGG, and FPN), please cite them. 



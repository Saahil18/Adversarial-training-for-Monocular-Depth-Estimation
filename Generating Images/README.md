# Generating Images

## Overview
This directory contains code and data for generating images used in the adversarial attacks against monocular depth estimation models. The code is a part of the repository for the paper [Physical 3D Adversarial Attacks against Monocular Depth Estimation in Autonomous Driving](http://arxiv.org/abs/2403.17301), accepted at CVPR 2024.

## Abstract
Monocular depth estimation (MDE) is crucial for autonomous driving but is susceptible to adversarial attacks. This repository includes methods to generate adversarial textures and images to test MDE model robustness. The generated images are used to evaluate and improve the resilience of MDE systems against physical 3D adversarial attacks.

## Code
1. **data_loader_mde.py**
   - **Purpose**: Load and prepare the training dataset.
   - **Key Components**:
     - `MyDataset`: Class to load the training set.
     - **Attributes**:
       - `data_dir`: Path to RGB background images.
       - `obj_name`: Path to the car model used.
       - `camou_mask`: Path to the camouflage mask (texture area to attack).
       - `tex_trans_flag`: Flag for texture transformation.
       - `phy_trans_flag`: Flag for physical transformation.
       - `camera_pos`: Camera relative position in Carla simulator.
     - **Methods**:
       - `set_textures(self, camou)`: Sets the camouflage texture based on the given seed.

2. **attack_base.py**
   - **Purpose**: Perform the adversarial attack using generated textures.
   - **Key Components**:
     - `camou_mask`: Path to the camouflage texture mask.
     - `camou_shape`: Shape of the camouflage texture.
     - `obj_name`: Path to the car model.
     - `train_dir`: Path to RGB background images.
     - `log_dir`: Directory to save results.

## Training Dataset
- **BaiduNetdisk Link**: [Training Data](https://pan.baidu.com/s/1IiD0HYRKjoNOx-hIsamHbg?pwd=3D2F)
  - **Contents**:
    - `./rgb/*.jpg`: Background images.
    - `./ann.pkl`: Camera position matrix.

## Acknowledgements
- **Paper**: [Physical 3D Adversarial Attacks against Monocular Depth Estimation in Autonomous Driving](https://openaccess.thecvf.com/content/CVPR2024/papers/Zheng_Physical_3D_Adversarial_Attacks_against_Monocular_Depth_Estimation_in_Autonomous_CVPR_2024_paper.pdf)
- **Source Code**: [3D2Fool GitHub Repository](https://github.com/Gandolfczjh/3D2Fool.git)

## Citation

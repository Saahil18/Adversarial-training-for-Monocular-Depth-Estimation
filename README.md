# Adversarial-Training-for-Monocular-Depth-Estimation

## Overview

This repository contains four primary components: `generating_images`, `densedepth`, `monodepth2`, and `adversarial_patch`. Each component serves a distinct purpose in the workflow for generating images, applying depth estimation, and creating adversarial patches to evaluate and enhance depth prediction models.

## Table of Contents

1. [Folder Structure](#folder-structure)
2. [Generating Images](#generating-images)
3. [DenseDepth](#densedepth)
4. [MonoDepth2](#monodepth2)
5. [Adversarial Patch](#adversarial-patch)
6. [Usage](#usage)
7. [License](#license)
8. [Contact](#contact)

## Folder Structure

- **generating_images/**: Scripts and tools for generating and preparing images used in training and evaluation.
- **densedepth/**: A modified version of the DenseDepth model, adapted for our custom dataset and depth estimation tasks.
- **monodepth2/**: A customized version of the MonoDepth2 model, configured for training with our data and integrated with custom scripts.
- **adversarial_patch/**: Code for generating and applying adversarial patches to assess and improve the robustness of depth estimation models.

# Generating Images

### Purpose

The `generating_images` folder contains scripts designed to create or preprocess images that will be used in depth estimation tasks. This includes generating synthetic images, preprocessing real-world images, and creating specific datasets required for models like DenseDepth and MonoDepth2.

### Key Files

- **data_loader_mde.py**: Contains the `MyDataset` class for loading and preprocessing the training set. 
  - **data_dir**: Path to RGB background images.
  - **obj_name**: Path to the car model.
  - **camou_mask**: Path to the mask for the texture area to attack.
  - **tex_trans_flag**: Texture transformation flag.
  - **phy_trans_flag**: Physical transformation flag.
  - **set_textures**: Method to set textures for camouflage.
  - **camera_pos**: Camera relative position data.

- **attack_base.py**: Main script for setting up and running the adversarial attack.
  - **camou_mask**: Path to the camouflage texture mask.
  - **camou_shape**: Shape of the camouflage texture.
  - **obj_name**: Path to the car model.
  - **train_dir**: Path to RGB background images.
  - **log_dir**: Path to save results.

- **training dataset**: 
  - **[BaiduNetdisk Link](https://pan.baidu.com/s/1IiD0HYRKjoNOx-hIsamHbg?pwd=3D2F)**: Contains background images and camera position matrix.
  - **./rgb/*.jpg**: RGB background images.
  - **./ann.pkl**: Camera position matrix.

### Usage

1. **Generate Images**:
   - Use `data_loader_mde.py` to prepare the dataset for training. Specify paths to the required data and settings for texture and camouflage.

2. **Run Adversarial Attack**:
   - Execute `attack_base.py` to generate adversarial examples based on the camouflage texture and background images.


# Adversarial Patch

### Purpose

The `Patch_augmenttion` folder is focused on generating and applying adversarial patches to test the robustness of depth estimation models. It includes:

- **Object Detection**: Using YOLOv8 to detect vehicles in images.
- **Patch Application**: Augmenting and applying adversarial patches to assess model performance.

### Key Files

- **adversarial_patch_augmentation.ipynb**: Google Colab notebook containing the full workflow for generating and applying adversarial patches. This notebook includes:
  - YOLOv8 object detection for identifying vehicles.
  - Augmentation of the adversarial patch with images.
  - Application of the patch to images and analysis of depth maps.
- **texture_seed.png**: The adversarial patch used in the experiments. This image is applied to the detected vehicles to test the impact on depth estimation.

### Usage

1. **Open and Run the Colab Notebook**:
   - Execute the cells in `adversarial_patch_augmentation.ipynb` to follow the process of detecting objects, applying adversarial patches, and analyzing the results.
2. **Adversarial Patch**:
   - The `texture_seed.png` file is used as the adversarial patch for testing the models.


# MonoDepth2

### Purpose

The `monodepth2` folder includes a customized version of MonoDepth2, a self-supervised depth estimation model that can predict depth from monocular images without requiring ground truth depth data for training.

### Custom Modifications

- **Trainer Updates**: Modified `trainer.py` to integrate with the custom dataset and incorporate additional training options.
- **Options Configuration**: Adjusted `options.py` for easier command-line argument parsing.
- **Custom Dataset Integration**: Included `custom_dataset.py` to handle our specific dataset format.

### Usage

1. Replace the original `trainer.py`, `train.py`, and `options.py` with the custom versions provided.
2. Run the `train.py` script to initiate training on your dataset.
3. Evaluate the trained model using `evaluate_depth.py`.


# DenseDepth

### Purpose

The `densedepth` folder contains a modified version of the DenseDepth model, designed for depth estimation tasks with custom datasets.

### Custom Modifications

- **Normalization Adjustments**: Adapted to fit the normalization standards of our specific dataset.
- **Data Structure Changes**: Customized to work with the image outputs from the `generating_images` folder.
- **Training Script**: Use '`Dense_depth_adversarial_training_and_evaluation` to implement training nd evaluation.

### Usage

1. Place your custom dataset in the appropriate directory.
2. Run `Dense_depth_adversarial_training_and_evaluation` to start the training process.
3. Monitor training progress using graphs.
4. Evaluate the results and find matrices





## License

This project is based on multiple open-source projects. Each folder might have its own license file—please refer to them for more details.

## Contact

For any questions or further assistance, please contact [Saahil Khanna].

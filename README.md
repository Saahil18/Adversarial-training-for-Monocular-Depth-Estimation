# Adversarial-training-for-Monocular-Depth-Estimation

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

## Generating Images

### Purpose

The `generating_images` folder contains scripts designed to create or preprocess images that will be used in the depth estimation tasks. This may include:

- Generating synthetic images.
- Preprocessing real-world images.
- Creating specific image datasets required by DenseDepth and MonoDepth2.

### Key Files

- **image_generator.py**: Script for generating synthetic images with specific characteristics.
- **preprocess_images.py**: A tool to resize, crop, and normalize images to fit the input requirements of the depth models.
- **dataset_splitter.py**: Splits the generated or collected images into training, validation, and test sets.

### Usage

1. Run `image_generator.py` to create the required image set.
2. Use `preprocess_images.py` to ensure all images are in the correct format and resolution.
3. Utilize `dataset_splitter.py` to divide the images into appropriate datasets.

## DenseDepth

### Purpose

The `densedepth` folder contains a modified version of the DenseDepth model. DenseDepth is a state-of-the-art model for depth estimation from a single image, leveraging encoder-decoder architecture and dense connections.

### Custom Modifications

- **Normalization Adjustments**: The model has been adapted to fit the normalization standards of our specific dataset.
- **Data Structure Changes**: Customized to work with the image outputs from the `generating_images` folder.
- **Training Scripts**: Updated `trainer.py`, `train.py`, and `options.py` to accommodate the custom dataset and training regime.

### Usage

1. Place your custom dataset in the appropriate directory.
2. Run `train.py` to start the training process.
3. Monitor training progress using TensorBoard if necessary.

## MonoDepth2

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

## Adversarial Patch

### Purpose

The `adversarial_patch` folder contains code for generating and applying adversarial patches. These patches are used to test the robustness of depth estimation models by introducing perturbations to the input images.

### Key Files

- **generate_patch.py**: Script for generating adversarial patches designed to fool depth estimation models.
- **apply_patch.py**: Tool to apply the generated patches to test images.
- **evaluate_patch.py**: Evaluates the impact of the adversarial patches on model performance.

### Usage

1. Use `generate_patch.py` to create an adversarial patch.
2. Apply the patch to a set of test images using `apply_patch.py`.
3. Evaluate the performance of the patched images using `evaluate_patch.py`.

## Usage

1. **Generate and Preprocess Images**: Use the `generating_images` scripts to create and prepare your dataset.
2. **Train Depth Estimation Models**:
   - Use the `densedepth` folder to train the DenseDepth model.
   - Alternatively, use the `monodepth2` folder to train the MonoDepth2 model.
3. **Generate Adversarial Patches**: Test the trained models using adversarial patches from the `adversarial_patch` folder.
4. **Evaluate and Fine-Tune**: Based on adversarial testing, fine-tune the models to improve their robustness.

## License

This project is based on multiple open-source projects. Each folder might have its own license file—please refer to them for more details.

## Contact

For any questions or further assistance, please contact [Saahil Khanna].

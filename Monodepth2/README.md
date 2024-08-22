# MonoDepth2 Custom Training

## Overview

This repository contains steps to import MonoDepth2 from its official GitHub repository, replace key files with customized versions, and train the model using a custom dataset. MonoDepth2 is a self-supervised depth estimation model that predicts depth maps from single images.

## Table of Contents

1. [Objective](#objective)
2. [Dependencies](#dependencies)
3. [Clone the Repository](#clone-the-repository)
4. [Replace Files with Custom Versions](#replace-files-with-custom-versions)
5. [Prepare Custom Dataset](#prepare-custom-dataset)
6. [Training](#training)
7. [Evaluation](#evaluation)
8. [Troubleshooting](#troubleshooting)
9. [License](#license)
10. [Contact](#contact)

## Objective

- **Import MonoDepth2**: Clone the official MonoDepth2 repository from GitHub.
- **Replace Core Files**: Replace `trainer.py`, `train.py`, and `options.py` with our custom implementations.
- **Custom Dataset Integration**: Use our custom dataset by incorporating `custom_dataset.py` and also use our 'splits/custom/' dataset splits.
- **Train the Model**: Train MonoDepth2 with the custom dataset.

## Dependencies

Ensure you have the following dependencies installed:

- Python 3.x
- PyTorch
- NumPy
- Matplotlib
- OpenCV
- TensorBoard (optional for monitoring)


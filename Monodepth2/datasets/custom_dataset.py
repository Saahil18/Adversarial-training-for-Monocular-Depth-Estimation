# custom_dataset.py

import torch
from PIL import Image
from torchvision import transforms
import os

class CustomDataset(torch.utils.data.Dataset):
    def __init__(self, root_dir, frame_ids, height, width, scales, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.frame_ids = frame_ids
        self.height = height
        self.width = width
        self.scales = scales
        self.image_files = [os.path.join(root_dir, f) for f in os.listdir(root_dir) if f.endswith('png')]

        # Define intrinsic camera parameters
        # Normalize the intrinsics matrix
        self.K = torch.tensor([[0.58, 0, 0.5, 0],
                               [0, 1.92, 0.5, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]], dtype=torch.float32)
        self.K[0, :] *= 1 / self.width
        self.K[1, :] *= 1 / self.height
        self.inv_K = torch.inverse(self.K)

    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, idx):
        img_name = self.image_files[idx]
        image = Image.open(img_name).convert('RGB')  # Ensure image is in RGB format

        print(f"Loading image: {img_name}")

        inputs = {}

        # Generate image for each scale
        for scale in self.scales:
            scaled_image = image.resize((self.width // (2 ** scale), self.height // (2 ** scale)), Image.LANCZOS)
            if self.transform:
                scaled_image = self.transform(scaled_image)
            for i in self.frame_ids:
                inputs[("color", i, scale)] = scaled_image
                inputs[("color_aug", i, scale)] = scaled_image  # Assuming no augmentation is applied

        # Add intrinsic camera parameters
        for scale in self.scales:
            K = self.K.clone()
            inv_K = self.inv_K.clone()
            K[0, :] *= self.width // (2 ** scale)
            K[1, :] *= self.height // (2 ** scale)
            inv_K[0, :] /= self.width // (2 ** scale)
            inv_K[1, :] /= self.height // (2 ** scale)
            inputs[("K", scale)] = K
            inputs[("inv_K", scale)] = inv_K

        return inputs


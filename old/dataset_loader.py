import cv2
import os
import numpy as np

def load_dataset(train_dataset_dir = 'dataset/train',  test_dataset_dir = 'dataset/test'):
    # Set the path to the dataset directory
    # Initialize empty arrays for storing the images and masks
    images = []
    masks = []
    test_images = []
    test_masks = []
    # Loop over the files in the dataset directory
    for filename in os.listdir(train_dataset_dir):
        if filename.endswith('GT.png'): # Check if the file is an image
            mask_path = os.path.join(train_dataset_dir, filename)
            image_path = os.path.join(train_dataset_dir, filename[:-7]+'.png') # Assumes that the mask file is named "mask_<image_filename>.jpg"

            # Load the image and mask using OpenCV
            image = cv2.imread(image_path)
            mask = cv2.imread(mask_path)

            # Convert the mask to a binary image
            mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
            mask = np.where(mask > 0, 1, 0)

            # Append the image and mask to the arrays
            images.append(image)
            masks.append(mask)

    # Loop over the files in the dataset directory
    for filename in os.listdir(test_dataset_dir):
        if filename.endswith('GT.png'): # Check if the file is an image
            mask_path = os.path.join(test_dataset_dir, filename)
            image_path = os.path.join(test_dataset_dir, filename[:-7]+'.png') # Assumes that the mask file is named "mask_<image_filename>.jpg"

            # Load the image and mask using OpenCV
            image = cv2.imread(image_path)
            mask = cv2.imread(mask_path)

            # Convert the mask to a binary image
            mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
            mask = np.where(mask > 0, 1, 0)

            # Append the image and mask to the arrays
            test_images.append(image)
            test_masks.append(mask)


    return zip(images, masks), zip(test_images, test_masks) 

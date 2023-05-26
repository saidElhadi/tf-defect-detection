# augmentation.py
import os
import sys
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array, array_to_img

def augment_images_in_folder(folder_path):
    output_dir = os.path.join(folder_path, 'augmented_images')
    os.makedirs(output_dir, exist_ok=True)

    datagen = ImageDataGenerator(
        # rotation_range=90,
        brightness_range=[0.2, 1.0],
        shear_range=0.2,
        horizontal_flip=True,
        vertical_flip=True,
        fill_mode='nearest'
    )

    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img_path = os.path.join(folder_path, filename)
            img = load_img(img_path)
            x = img_to_array(img)
            x = x.reshape((1,) + x.shape)
            i = 0
            for batch in datagen.flow(x, batch_size=1, save_to_dir=output_dir, save_prefix='aug', save_format='png'):
                i += 1
                if i > no_of_augmentations:
                    break

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Provide directory path as an argument.")
        sys.exit(1)
    folder_path = sys.argv[1]
    no_of_augmentations = 2  # specify the desired number of augmentations per image
    augment_images_in_folder(folder_path)
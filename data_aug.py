from keras.models import Sequential
import keras

data_augmentation = Sequential(
    [
        keras.layers.RandomFlip("horizontal_and_vertical"),
        keras.layers.RandomRotation((0, 0.9), fill_mode="constant"),
        keras.layers.RandomZoom(0.05, fill_mode="constant"),
        keras.layers.RandomContrast(0.25),
        keras.layers.RandomBrightness(0.25),
    ])

def save_augmented_images(data, data_type, path_images):
    """
    Augment an image dataset by performing transformations on the original images.
    Each image is transformed a total of 6 times.
    Note that the training and testing datasets are saved separately to avoid data leakage
    
    Args:
        - data: image dataset as a BatchDataset
        - data_type: string containing type of dataset, i.e. train or test
        - path_images: directory where the user wishes to save the data
    """
    count_ok = 1
    count_def = 1
    for batch in data:
        (images, labels) = batch

        for i in range(images.shape[0]):
            if labels[i].numpy() == 0:
                for j in range(6):
                    augmented_image = data_augmentation(images[i], training=True)
                    img = Image.fromarray(augmented_image.numpy().astype(np.uint8))
                    img.save(
                        os.path.join(
                            path_images
                            + "/"
                            + data_type
                            + "/def_front/"
                            + str(count_def)
                            + ".jpeg"
                        )
                    )
                    count_def += 1

            else:
                for j in range(6):
                    augmented_image = data_augmentation(images[i], training=True)
                    img = Image.fromarray(augmented_image.numpy().astype(np.uint8))
                    img.save(
                        os.path.join(
                            path_images
                            + "/"
                            + data_type
                            + "/ok_front/"
                            + str(count_ok)
                            + ".jpeg"
                        )
                    )
                    count_ok += 1
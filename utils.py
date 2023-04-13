import os
import matplotlib.pyplot as plt

def show_images_with_masks(images, masks, start_index, end_index):
    fig, axs = plt.subplots(nrows=2, ncols=(end_index-start_index), figsize=(20, 20))
    fig.subplots_adjust(hspace=0.3, wspace=0.1)

    for i in range(start_index, end_index):
        image = images[i]
        mask = masks[i]

        axs[0, i-start_index].imshow(image, aspect='auto')
        axs[0, i-start_index].set_title(f"Image {i}")

        axs[1, i-start_index].imshow(mask, cmap='gray', aspect='auto')
        axs[1, i-start_index].set_title(f"Mask {i}")
        
    plt.show()

def get_files_larger_than_threshold(folder_path, threshold):
    """
    Get file paths of files larger than the specified threshold in bytes.

    Args:
        folder_path (str): The path to the folder to check.
        threshold (int): The threshold size in bytes.

    Returns:
        list: A list of file paths for files larger than the threshold.
    """
    large_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            if file_size > threshold:
                large_files.append(file_path)
    return large_files

def find_substing_in_array(array, substring):
    
    matches = []

    for elem in array:
        if substring in elem:
            matches.append(elem)

    return matches

def get_images_with_defects(array):
    
    defectImgs = []
    for elem in array:
        temp = elem.replace("_GT.png", ".png")
        defectImgs.append(temp)

    
    return defectImgs

print(
    get_images_with_defects(
        find_substing_in_array(
        get_files_larger_than_threshold('dataset/train', 250),    
        'GT.png')
    )
)
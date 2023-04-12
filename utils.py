import os

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
            print(elem)
            
    return matches



print(find_substing_in_array(get_files_larger_than_threshold('dataset/train', 250), 'GT.png'))

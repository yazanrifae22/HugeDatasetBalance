import os
import glob

def remove_lines_starting_with(file_path, prefix):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            if not line.startswith(prefix) and line.strip():
                file.write(line)

def delete_lines_with_prefix_in_folder(folder_path, prefix):
    txt_files = glob.glob(os.path.join(folder_path, '*.txt'))

    for file_path in txt_files:
        remove_lines_starting_with(file_path, prefix)

if __name__ == "__main__":
    folder_path = "../empty_plate/train/labels"
    prefix_to_remove = "50 "

    delete_lines_with_prefix_in_folder(folder_path, prefix_to_remove)


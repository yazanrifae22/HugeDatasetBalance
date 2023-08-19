import os
import yaml
from termcolor import colored

def read_list_from_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data['names']

def find_string_index_in_yaml_list(yaml_list, target_string):
    target_lower = target_string.lower()
    for index, element in enumerate(yaml_list):
        if element.lower() == target_lower:
            return index
    return None

def process_labels_folder(labels_folder, yaml_list):
    for filename in os.listdir(labels_folder):
        if filename.endswith('.txt'):
            file_path = os.path.join(labels_folder, filename)
            process_text_file(file_path, yaml_list)

def process_text_file(file_path, yaml_list):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            words = line.strip().split()
            if words:
                first_word = words[0]
                print(first_word)
                index = find_string_index_in_yaml_list(yaml_list, first_word)
                if index is not None:
                    line = line.replace(first_word, str(index),1)
                else:

                    print(file_path,":",colored(f"Error: '{first_word}' is not found in the YAML list.", 'red'))
            file.write(line)


# Read the list named "names" from the YAML file

# Main folder containing the "labels" subfolders
main_folder = "../last data/all_data/train"  # Replace this with the actual path to your main folder
yaml_file_path = os.path.join(main_folder, "data.yaml") # Replace this with the actual YAML file path
yaml_list = read_list_from_yaml(yaml_file_path)

for root, _, _ in os.walk(main_folder):
    labels_folder = os.path.join(root, 'labels')
    if not os.path.isdir(labels_folder):
        print("no file",root)
        continue

    process_labels_folder(labels_folder, yaml_list)

import os
import yaml
def extract_digits_until_space(line):
    first_space_index = line.find(' ')
    if first_space_index != -1:
        digits_part = line[:first_space_index]
        if digits_part.isdigit():
            return digits_part



def read_data_yaml(data_yaml_path):
    with open(data_yaml_path, 'r') as file:
        data = yaml.safe_load(file)
    return data['names']

def replace_int_with_name(file_path, names):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            digits_part = extract_digits_until_space(line)
            if digits_part is not None:
                line = line.replace(digits_part, names[int(digits_part)], 1)  # Replace the first occurrence of digits_part with 'hi'
            file.write(line)


def process_labels_folder(labels_folder, names):
    for filename in os.listdir(labels_folder):
        if filename.endswith('.txt'):
            file_path = os.path.join(labels_folder, filename)
            replace_int_with_name(file_path, names)

def process_subfolder(subfolder_path, names):
    for folder_name in ['']:
        labels_folder = os.path.join(subfolder_path, folder_name, )
       
        process_labels_folder(labels_folder, names)

def main():
    main_folder = "../last data/ksa/test"  # Replace with the actual path to "main_folder"

    for subfolder in os.listdir(main_folder):
        subfolder_path = os.path.join(main_folder, subfolder)
        if os.path.isdir(subfolder_path):
            data_yaml_path = os.path.join(main_folder, 'data.yaml')
            names = read_data_yaml(data_yaml_path)
            process_subfolder(subfolder_path, names)

if __name__ == "__main__":
    main()

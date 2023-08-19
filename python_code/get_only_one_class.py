import os

def process_files_in_folder(folder_path, starting_string):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            process_file(file_path, starting_string)

def process_file(file_path, starting_string):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    filtered_lines = [line for line in lines if line.startswith(starting_string)]
    modified_lines = [line.replace(starting_string, "0 ") for line in filtered_lines]

    with open(file_path, 'w') as file:
        file.writelines(modified_lines)

def main():
    folder_path = "../empty_plate/train/labels"
    starting_string = "57 "
    process_files_in_folder(folder_path, starting_string)

if __name__ == "__main__":
    main()

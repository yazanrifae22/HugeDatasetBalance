import os

def process_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines if '-' not in line]
    cleaned_lines = []

    for line in lines:
        if line:
            cleaned_lines.append(line)

    with open(file_path, 'w') as file:
        file.write('\n'.join(cleaned_lines))

def process_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            process_file(file_path)

if __name__ == '__main__':
    folder_path = '../empty_plate/labels'  # Replace with the path to your folder containing the .txt files
    process_folder(folder_path)

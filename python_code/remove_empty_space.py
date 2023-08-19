import os

def remove_empty_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    lines = [line.strip() for line in lines if line.strip()]
    
    with open(file_path, 'w') as file:
        file.write('\n'.join(lines))

def process_files_in_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                remove_empty_lines(file_path)
                print(f"Processed: {file_path}")

if __name__ == "__main__":
    folder_path = '../empty_plate/labels' # Replace with the path to your folder
    process_files_in_folder(folder_path)
    print("Empty lines removed from all .txt files in the folder.")

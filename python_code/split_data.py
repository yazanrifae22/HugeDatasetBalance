import os
import random
import shutil

# Set the paths to your image and label folders
mm_folder="uae"
image_folder = f'../{mm_folder}/images'
label_folder = f'../{mm_folder}/labels'

# Create train, valid, and test directories if they don't exist
train_folder = f'{mm_folder}/train'
valid_folder = f'{mm_folder}/valid'
test_folder = f'{mm_folder}/test'
train_image_folder = os.path.join(train_folder, 'images')
train_label_folder = os.path.join(train_folder, 'labels')
valid_image_folder = os.path.join(valid_folder, 'images')
valid_label_folder = os.path.join(valid_folder, 'labels')
test_image_folder = os.path.join(test_folder, 'images')
test_label_folder = os.path.join(test_folder, 'labels')
os.makedirs(train_image_folder, exist_ok=True)
os.makedirs(train_label_folder, exist_ok=True)
os.makedirs(valid_image_folder, exist_ok=True)
os.makedirs(valid_label_folder, exist_ok=True)
os.makedirs(test_image_folder, exist_ok=True)
os.makedirs(test_label_folder, exist_ok=True)

# Get the list of image files
image_files = [file for file in os.listdir(image_folder) if file.endswith('.jpg')]

# Shuffle the image files
random.shuffle(image_files)

# Calculate the split points for 70% and 90%
train_split_index = int(0.7 * len(image_files))
valid_split_index = int(0.9 * len(image_files))

# Split image files into train, valid, and test sets
train_image_files = image_files[:train_split_index]
valid_image_files = image_files[train_split_index:valid_split_index]
test_image_files = image_files[valid_split_index:]

# Move train image files and their corresponding labels
for image_file in train_image_files:
    image_path = os.path.join(image_folder, image_file)
    label_file = image_file.replace('.jpg', '.txt')
    label_path = os.path.join(label_folder, label_file)
    
    shutil.move(image_path, os.path.join(train_image_folder, image_file))
    shutil.move(label_path, os.path.join(train_label_folder, label_file))

# Move valid image files and their corresponding labels
for image_file in valid_image_files:
    image_path = os.path.join(image_folder, image_file)
    label_file = image_file.replace('.jpg', '.txt')
    label_path = os.path.join(label_folder, label_file)
    
    shutil.move(image_path, os.path.join(valid_image_folder, image_file))
    shutil.move(label_path, os.path.join(valid_label_folder, label_file))

# Move test image files and their corresponding labels
for image_file in test_image_files:
    image_path = os.path.join(image_folder, image_file)
    label_file = image_file.replace('.jpg', '.txt')
    label_path = os.path.join(label_folder, label_file)
    
    shutil.move(image_path, os.path.join(test_image_folder, image_file))
    shutil.move(label_path, os.path.join(test_label_folder, label_file))

print("Files moved to train, valid, and test folders.")


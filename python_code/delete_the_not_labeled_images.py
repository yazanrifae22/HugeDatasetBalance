import os

# Define the paths to the images and labels folders
images_folder = "../last data/all_data/valid/images"
labels_folder = "../last data/all_data/valid/labels"

# Get a list of all image files in the images folder
image_files = [f for f in os.listdir(images_folder) if f.endswith(".jpg")]

# Iterate through the image files
deleted_count = 0
for image_file in image_files:
    # Remove the extension to get the base filename
    base_filename = image_file.rsplit(".", 1)[0]
    
    # Construct the corresponding label file name
    label_file = base_filename + ".txt"
    
    # Check if the label file exists in the labels folder
    if not os.path.exists(os.path.join(labels_folder, label_file)):
        # If the label file doesn't exist, delete the image file
        image_path = os.path.join(images_folder, image_file)
        os.remove(image_path)
        deleted_count += 1
        print(f"Deleted: {image_file}")

print(f"Deleted {deleted_count} files.")

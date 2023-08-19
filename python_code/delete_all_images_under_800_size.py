import os
from PIL import Image

def delete_small_images(directory, size_threshold=800):
    for root, dirs, files in os.walk(directory):
        if "cropped" in dirs and "images" in os.listdir(os.path.join(root, "cropped")):
            images_folder = os.path.join(root, "cropped", "images")
            for filename in os.listdir(images_folder):
                # Check if the file is an image
                if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                    filepath = os.path.join(images_folder, filename)
                    try:
                        # Get the image size in bytes
                        image = Image.open(filepath)
                        image_size = os.path.getsize(filepath)
                        image.close()

                        # Delete the image if it's smaller than the size_threshold
                        if image_size < size_threshold:
                            os.remove(filepath)
                            print(f"Deleted: {filepath}")
                    except Exception as e:
                        print(f"Error processing {filepath}: {e}")

if __name__ == "__main__":
    # Replace '/path/to/main_folder' with the actual path of the main folder containing subdirectories
    delete_small_images('../crop', size_threshold=800)

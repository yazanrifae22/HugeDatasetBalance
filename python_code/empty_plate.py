import os
import cv2
from PIL import Image, ImageDraw
import threading



def draw_white_box_on_image(image_path, x, y, w, h):
    # Open the image
    image = Image.open(image_path)

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Define white color
    white = (255, 255, 255)

    # Draw the white box on the image
    draw.rectangle([x-w, y-h,  x+w, y+ h], fill=white)

    # Save the modified image
    
    image.save(image_path)


def normalizing(x, y, w, h, jpg_filepath):
    # Open the image using OpenCV
    image = cv2.imread(jpg_filepath)
    if image is None:
        print(f"Failed to read the image from {jpg_filepath}")
        return

    # Get the image width and height
    image_height, image_width, _ = image.shape

    # Perform normalization
    x_normalized = x * image_width
    y_normalized = y * image_height
    w_normalized = w * image_width
    h_normalized = h * image_height
    print(jpg_filepath, int(x_normalized), int(y_normalized), w_normalized/2, h_normalized/2)
    draw_white_box_on_image(jpg_filepath, x_normalized, y_normalized,w_normalized/2, h_normalized/2)

    return x_normalized, y_normalized, w_normalized, h_normalized

def process_txt_files_in_folder(txt_files):
    for txt_filepath, jpg_filepath in txt_files:
        try:
            with open(txt_filepath, "r") as file:
                for line in file:
                    name, x, y, w, h = line.strip().split(' ')
                    x, y, w, h = float(x), float(y), float(w), float(h)

                    x_normalized, y_normalized, w_normalized, h_normalized = normalizing(x, y, w, h, jpg_filepath)

                    # Process normalized data as needed
                    # print(name, x_normalized, y_normalized, w_normalized, h_normalized, jpg_filepath)
        except Exception as e:
            print(f"Error processing {txt_filepath}: {e}")
# Example usage: Process all txt files in the "folder_path" directory
def split_list_into_chunks(lst, chunk_size):
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]
def main():
    folder_path = "../empty_plate/labels"
    all_txt_files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]

    txt_filepaths = [os.path.join(folder_path, txt_filename) for txt_filename in all_txt_files]
    jpg_filepaths = [txt_filepath.replace("labels", "images").replace(".txt", ".jpg") for txt_filepath in txt_filepaths]

    txt_and_jpg_filepaths = list(zip(txt_filepaths, jpg_filepaths))

    num_threads = 1
    txt_files_per_thread = len(txt_and_jpg_filepaths) // num_threads

    txt_file_chunks = list(split_list_into_chunks(txt_and_jpg_filepaths, txt_files_per_thread))

    threads = []
    for i, chunk in enumerate(txt_file_chunks):
        thread = threading.Thread(target=process_txt_files_in_folder, args=(chunk,))
        thread.name = f"Thread-{i}"
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
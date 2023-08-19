import os
import random
import cv2
import uuid

# Function to count the occurrences of integers in text files inside a specified folder.
def count_integers_in_files(folder_path):
    integer_counts = {}  # A dictionary to store the counts of each integer encountered in the files.
    integers_below_3000 = {}  # A dictionary to store the integers and their counts below 12000.

    # Check if the specified folder exists.
    if not os.path.exists(folder_path):
        print("Error: The specified 'labels' folder does not exist.")
        return None, None

    # Loop through the files in the folder.
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if the item in the folder is a file with '.txt' extension.
        if os.path.isfile(file_path) and filename.endswith('.txt'):
            with open(file_path, 'r') as file:
                # Read each line in the file.
                for line in file:
                    try:
                        print(file_path)
                        # Split the line and extract the first integer in it.
                        print(line.split())
                        if not line.split():
                            continue

                        integer = int(line.split()[0])

                        # Increment the count of the integer in the dictionary.
                        integer_counts[integer] = integer_counts.get(integer, 0) + 1
                    except ValueError:
                        # If the line does not start with an integer, continue to the next line.
                        continue

    # Filter the integers that have a count below 12000.
    for integer, count in integer_counts.items():
        if count < 12000:
            integers_below_3000[integer] = count

    # Return the dictionaries containing all integer counts and integers with counts below 12000.
    return integer_counts, integers_below_3000


# Function to balance the data based on integers with counts below 12000.
def data_balance(integers_below_3000):
    char_class = list(range(55))  # A list of integers representing the characters from 0 to 9 and A to Z.
    new_uae = list(range(99,100))   # A list of integers representing certain characters (36 to 41).
    old_uae = list(range(55,58))   # A list of integers representing certain characters (42 to 48).

    folder_path = '../empty_plate/labels'  # Path to the folder containing the text label files.
    save_folder_path = "../balancing_data/images"  # Path to save the balanced image files.
    save_labels_path = "../balancing_data/labels"  # Path to save the balanced label files.

    # Check if the 'labels' folder exists.
    if not os.path.exists(folder_path):
        print("Error: The specified 'labels' folder does not exist.")
        return

    # Get a list of all text files in the 'labels' folder.
    text_files = [filename for filename in os.listdir(folder_path) if filename.endswith('.txt')]

    # Check if there are any text files in the 'labels' folder.
    if not text_files:
        print("Error: The 'labels' folder is empty or does not contain any text files.")
        return

    # Create the 'images' and 'labels' folders to save the balanced data.
    os.makedirs(save_folder_path, exist_ok=True)
    os.makedirs(save_labels_path, exist_ok=True)

    # Continue the data balancing process until there are integers below 12000.
    while any(key in char_class for key in integers_below_3000.keys()):
        try:
            # Print the number of integers below 12000.
            print(len(integers_below_3000.keys()))

            # Choose a random text file from the 'labels' folder.
            random_img_path = random.choice(text_files)
            random_file_path = os.path.join(folder_path, random_img_path)
            random_img_path = random_file_path.replace("labels", "images").replace(".txt", ".jpg")

            # Read the image corresponding to the selected text file.
            img = cv2.imread(random_img_path)

            # Get the width and height of the image.
            img_width, img_height = img.shape[1], img.shape[0]

            # Count the number of lines in the selected text file.
            line_count = sum(1 for _ in open(random_file_path))

            # Check if the text file is empty.
            if line_count == 0:
                print(f"The selected text file '{random_img_path}' is empty.")
                continue

            # Check if there are any integers below 12000 to balance.
            if not integers_below_3000:
                print("The 'integers_below_3000' list is empty.")
                return

            # Generate a unique filename ID for the balanced image and label files.
            filename_id = str(uuid.uuid4())
            save_path = os.path.join(save_folder_path, f"{filename_id}.jpg")
            txt_path = os.path.join(save_labels_path, f"{filename_id}.txt")

            # Open the random text file and process each line.
            with open(random_file_path, 'r') as file:
                for line in file:
                    try:
                        # Extract information from each line in the text file.
                        line_info = line.strip().split()
                        if len(line_info) == 5:
                            name, nx, ny, nwidth, nheight = map(float, line_info)

                        # Determine the valid keys based on the character class of the current line.
                        if int(name) in char_class:
                            valid_keys = [key for key in integers_below_3000.keys() if key in char_class]
                        elif int(name) in new_uae:
                            valid_keys = [key for key in integers_below_3000.keys() if key in new_uae]
                        elif int(name) in old_uae:
                            valid_keys = [key for key in integers_below_3000.keys() if key in old_uae]

                        # Check if there are any valid keys for the current character class.
                        if not valid_keys:
                            print(f"Error: No valid keys found in 'integers_below_3000' for character class '{name}'.")
                            continue

                        # Choose a random key from the valid keys list.
                        random_key = random.choice(valid_keys)

                        # Get the folder path containing cropped images for the selected key.
                        image_folder_path = f"../crop/{random_key}/cropped/images"

                        # Get a list of image files in the folder.
                        image_files = [filename for filename in os.listdir(image_folder_path) if filename.lower().endswith((".jpg", ".jpeg", ".png"))]

                        # Check if there are any images in the folder.
                        if not image_files:
                            print(f"No images found in the folder '{image_folder_path}'.")
                            continue

                        # Write the new label information to the balanced label file.
                        with open(txt_path, 'a') as file:
                            file.write(f"{random_key} {nx} {ny} {nwidth} {nheight}\n")

                        # Choose a random image file from the folder.
                        random_image_file = random.choice(image_files)
                        random_image_path = os.path.join(image_folder_path, random_image_file)

                        # Calculate the width and height of the cropped image.
                        width, height = int(nwidth * img_width), int(nheight * img_height)
                        x, y = int(nx * img_width - width / 2), int(ny * img_height - height / 2)

                        # Read and resize the cropped image.
                        cropped_image = cv2.imread(random_image_path)
                        cropped_image = cv2.resize(cropped_image, (width, height))

                        # Replace the corresponding region in the original image with the cropped image.
                        img[y:y+cropped_image.shape[0], x:x+cropped_image.shape[1]] = cropped_image

                        # Increment the count of the chosen key in the 'integers_below_3000' dictionary.
                        integers_below_3000[random_key] += 1

                        # If the count of the chosen key exceeds 12000, remove it from the dictionary.
                        if integers_below_3000[random_key] > 12000:
                            del integers_below_3000[random_key]
                    except Exception as e:
                        try:
                            if os.path.exists(save_path):
                                os.remove(txt_path)
                        except Exception as e:
                            print(f"Error processing {save_path}: {e}")
                        break

            # Save the balanced image.
            cv2.imwrite(save_path, img)
        except Exception as e:
            try:
                if os.path.exists(save_path):
                    os.remove(save_path)

                # Check if the balanced label file exists and remove it if it does.
                if os.path.exists(txt_path):
                    os.remove(txt_path)
            except Exception as e:
                print(f"Error processing {save_path}: {e}")

            print("An error occurred:", e)
            continue

    # Data balancing process completed successfully.
    print("Data balancing completed successfully.")


# Main part of the script starts here.

# Set the path to the 'labels' folder.
folder_path_here = '../empty_plate/labels'

# Call the function to count integers in the text files and get the results.
result_map, integers_below_3000 = count_integers_in_files(folder_path_here)

# Check if the result is not None and there are integers with counts below 12000.
if result_map is not None and integers_below_3000 is not None:
    # Print all the integer counts encountered in the text files.
    print("All integer counts:")
    print(result_map)

    # Print the integers and their counts that are below 12000.
    print("Integers and their counts below 12000:")
    print(integers_below_3000)

    # Call the data balancing function with the list of integers below 12000.
    data_balance(integers_below_3000)

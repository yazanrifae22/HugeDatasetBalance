import cv2
import random
import os
import shutil
import numpy as np
from classes import *
 
def blur_outside_rectangle(image_path, center_x, center_y, width, height,path,name, blur_strength=1):
    try:
        destination_path_image = os.path.join(path, name)





        image = cv2.imread(image_path)
        image_height, image_width = image.shape[:2]
        center_x=center_x*image_width
        width=width*image_width
        center_y=center_y*image_height
        height=height*image_height

        # Calculate the coordinates for cropping
        left = center_x - width // 2
        upper = center_y - height // 2
        right = left + width
        lower = upper + height

        # Crop the photo
        cropped_image = image[int(upper):int(lower), int(left):int(right)]
        if cropped_image is not None and cropped_image.size > 0:
            # print(cropped_image)
            cv2.imwrite(destination_path_image, cropped_image)
    except:
        return

        # Save the cropped photo as "cropped.jpg" in JPG format
    


# Exampl
# Example usage
# blur_outside_rectangle("C:/Users/User/Desktop/make_better_dataset/images/a (21).jpg", center_x=250, center_y=200, width=300, height=200)
def replace_file_extension(file_path):
    if file_path.endswith(".txt"):
        new_file_path = file_path.replace(".txt", ".jpg")
        return new_file_path
    else:
        return file_path
def crop_images(directory,img_dir,prefixes):
    # Create the "20" folder if it doesn't exist
    destination_folder = "../crop/"+str(prefixes)+"/cropped/label"
    destination_folder_img ="../crop/"+ str(prefixes)+"/cropped/images"

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    if not os.path.exists(destination_folder_img):
        os.makedirs(destination_folder_img)




    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            file_path_img = os.path.join(img_dir, replace_file_extension(filename))


            # Read the file content and filter lines
            with open(file_path, "r") as file:
                x=random.randrange(3, 90000)

                lines = file.readlines()
                filtered_lines = [line for line in lines if line.startswith(str(prefixes)+" ")]

            for i in range(len(filtered_lines)):
                name, cen_x, cen_y, wid, hei = [float(value) if index != 0 else value for index, value in enumerate(filtered_lines[i].split())]

                # Print the name of the file
                print("Found:", cen_y)
                destination_path_image = os.path.join(destination_folder_img, replace_file_extension(filename))
                print(destination_path_image)
                try:
                    # shutil.copy(file_path_img, destination_path_image)
                    blur_outside_rectangle(file_path_img, center_x=cen_x, center_y=cen_y, width=wid, height=hei,path=destination_folder_img,name=str(x)+".jpg")
                    
                except PermissionError as e:
                    continue
                    print(f"Unable to move file: {e}")


                # Write the filtered lines back to the file
                destination_path = os.path.join(destination_folder, str(x)+".txt")
                with open(destination_path, "w") as new_file:
                    new_file.writelines(filtered_lines[i])






for i in range(len(clases)):
   
    crop_images("../empty_plate/labels",'../empty_plate/images',clases[i])

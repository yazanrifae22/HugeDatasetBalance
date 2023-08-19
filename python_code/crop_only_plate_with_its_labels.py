import cv2
import random
import os
import shutil
import numpy as np
import uuid
import threading

# from classes import clases

def blur_outside_rectangle(image_path, center_x, center_y, width, height,path,name, blur_strength=1):
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

    # Save the cropped photo as "cropped.jpg" in JPG format
    cv2.imwrite(destination_path_image, cropped_image)


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
    destination_folder = "../empty_plate/"+str(prefixes)+"/cropped/labels"
    destination_folder_img = "../empty_plate/"+str(prefixes)+"/cropped/images"

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    if not os.path.exists(destination_folder_img):
        os.makedirs(destination_folder_img)


    file_count=0
    line_count=0
    for filename in (directory):
        line_count=0

        if filename.endswith(".txt"):

            file_path ="../empty_plate/train/labels/"+directory[file_count]
            file_count=file_count+1

            file_path_img = os.path.join(img_dir, replace_file_extension(filename))

            with open(file_path, 'r') as file:
                for _ in file:
                    line_count += 1
            if line_count>101:
                continue

            # Read the file content and filter lines
            print(line_count,"lkjlkjl lkj lk jlk jlkj lk jlk jlk jlk jlkj lk jlkj lkj lk jlk jlk j")
            with open(file_path, "r") as file:

                lines = file.readlines()
                filtered_lines = [line for line in lines if line.startswith(str(prefixes)+" ")]
                

            for i in range(len(filtered_lines)):
                name, cen_x, cen_y, wid, hei = [float(value) if index != 0 else value for index, value in enumerate(filtered_lines[i].split())]

                # Print the name of the file
                destination_path_image = os.path.join(destination_folder_img, replace_file_extension(filename))
                # print(destination_path_image)
                try:
                    x=str(uuid.uuid4())

                    # shutil.copy(file_path_img, destination_path_image)
                    blur_outside_rectangle(file_path_img, center_x=cen_x, center_y=cen_y, width=wid, height=hei,path=destination_folder_img,name=str(x)+".jpg")
                    
                except PermissionError as e:
                    print(f"Unable to move file: {e}")


                # Write the filtered lines back to the file
                destination_path = os.path.join(destination_folder, str(x)+".txt")
                filtered_linesw = [line for line in lines if not line.startswith(str(prefixes)+" ")]
                count=0
                for i in range(len(filtered_linesw)):
                    namec, ccen_x, ccen_y, cwid, chei = [float(value) if index != 0 else value for index, value in enumerate(filtered_linesw[i].split())]
                    main_image=cv2.imread(file_path_img)
                    imh,imw,_=main_image.shape
                    plate_x, plate_y, plate_wid, plate_hig = cen_x * imw, cen_y * imh, wid * imw, hei * imh
                    char_x, char_y, char_wid, char_hig = ccen_x * imw, ccen_y * imh, cwid * imw, chei * imh
                    if plate_x - plate_wid/2 < char_x+char_wid < plate_x + plate_wid/2 +50:
                        count=count+1
                        destination_path_image = os.path.join(destination_folder_img, str(x)+".jpg")
                        croped_image=cv2.imread(destination_path_image)
                        croped_imh,croped_imw,_=croped_image.shape
                        z=(plate_x- plate_wid/2)
                        new_x=char_x-z
                        new_x=new_x/croped_imw
                        new_y=char_y-(plate_y- plate_hig/2)
                        new_y=new_y/croped_imh
                        new_h=char_hig/croped_imh
                        new_w=char_wid/croped_imw
                        # print(namec+" "+str(new_x)+" "+str(new_y)+" "+str(new_w)+" "+str(new_h))
                        
                        
                        with open(destination_path, "a") as new_file:
                            new_file.writelines(namec+" "+str(new_x)+" "+str(new_y)+" "+str(new_w)+" "+str(new_h)+"\n")
                if count==0:
                    try:
                        destination_path_image = os.path.join(destination_folder_img, str(x)+".jpg")

                        os.remove(destination_path_image)
                    except Exception as e:
                        print(f"Error processing {destination_path_image}: {e}")
                else:
                    count=0
                
                        





# for i in range(1):
# directory="../empty_plate/train/labels"
# file_list = os.listdir(directory)
# number_of_files = len(file_list)
# crop_images(directory,'../empty_plate/train/images',57)

directory = "../empty_plate/train/labels/"
file_list = os.listdir(directory)
split_size = 50
threads = []
for start_idx in range(0, len(file_list), split_size):
    end_idx = start_idx + split_size
    file_range = file_list[start_idx:end_idx]
    
    thread = threading.Thread(target=crop_images, args=(file_range,'../empty_plate/train/images',50,))
    thread.start()
    
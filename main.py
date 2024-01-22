import cv2 as cv
import numpy as np
import os

def print_ascii(image_path, max_side, mode):
    # Init palette and image
    palette = [
    ' ', '-', ':', '=', '+', '#', '%', '@'
    ]
    if (mode == 0):
        # Light mode, invert palette
        palette = palette[::-1]
    image = cv.imread(image_path)
    if image is None:
        print(f"Error: Unable to read the image file at '{image_path}'.")
        return

    # Reize image to proper scaling
    height = int(image.shape[0])
    width = int(image.shape[1])
    scale_ratio = max_side / max(width, height)  # Use regular division for floating-point value
    new_width = int(width * scale_ratio)
    new_height = int(height * scale_ratio)
    image = cv.resize(image, (new_width, new_height))

    # Loop through each pixel of resized image
    for y in range(new_height):
        for x in range(new_width):
            b, g, r = image[y, x]  # Get RGB values
            px_mono = ((b / 255) + (g / 255) + (r / 255)) / 3  # Calculate 0-1 float of mono
            character_index = int(px_mono * (len(palette) - 1))
            character = palette[character_index]  # Assign character from palette shader using mono
            print(character * 2, end="")
        print("")


# Get the directory of the current script
script_directory = os.path.dirname(os.path.realpath(__file__))

# Construct the path to the /images/ directory
images_directory = os.path.join(script_directory, 'images')
files = os.listdir(images_directory)

image_file = -1
while (image_file != 0):
    # Print all files in the /images/ directory
    print("Images:")
    for i in range(len(files)):
        print(f"{i + 1}. {files[i]}")
    
    # Spacer
    print("====================================================")
    # Print quit message
    print("Type '0' to exit the program")
    # Ask user to select a file
    print("Enter the number of the file you would like to print")
    image_file = int(input())
    if (image_file == 0):
        continue
    elif (image_file > len(files) or image_file <= 0):
        print("Invalid selection")
        continue
    # Ask user what the max side length should be
    print("Enter the maximum side length of your ASCII print")
    max_side = int(input())
    if (max_side <= 0):
        print("Invalid resolution")
        continue

    print("Enter 0 if you are on light mode, 1 if you are on dark mode")
    mode = int(input())
    if (mode != 0 and mode != 1):
        print("Invalid selection")
        continue
    
    print("Printing your image...")
    image_path = images_directory
    image_path = os.path.join(image_path, files[image_file - 1])
    print_ascii(image_path, int(max_side), mode)
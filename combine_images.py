from PIL import Image
import os
import cv2
import numpy as np
import os
from PIL import Image
 
# Get smallest image size
def get_smallest_image_size(file_path):
    small_width = 0
    small_height = 0
    for filename in os.listdir(file_path):
        with Image.open(f'{file_path}/{filename}') as img:
            width, height = img.size
            # Set small compared to already found images
            if small_width == 0 or width < small_width:
                small_width = width
            if small_height == 0 or height < small_height:
                small_height = height
    return small_width, small_height
 
# Resize all images
def resize_all_images(file_path, small_width, small_height):
    images = []
    # Loop through each image and resize them
    for filename in os.listdir(file_path):
        with Image.open(f'{file_path}/{filename}') as img:
            images.append(img.resize((small_width, small_height)))
    return images

# Construct the quilt shape
def construct_quilt_shape(width, height, images):
    # A list of all the x and y pixel locations of the quilt
    x_coords = []
    y_coords = []
    x = 0
    while x < width:
        x_coords.append(x)
        x += images[0].width
        
    y = 0
    while y < height:
        y_coords.append(y)
        y += images[0].height
 
    # Now let's put them into the bigger picture by pasting
    quilt_border = Image.new('RGB', (width, height))
    for x in x_coords:
        for y in y_coords:
            quilt_border.paste(images.pop(), (x, y))
    return quilt_border

# Main function - Driver program
def photo_quilt(file_path, width, height):
    small_width, small_height = get_smallest_image_size(file_path)
    images = resize_all_images(file_path, small_width, small_height)
    quilt = construct_quilt_shape(width, height, images)
    quilt.save('my_quilt.png')







if __name__ == '__main__':
    file_path = "data/cat-images/"
    width = 1000
    height = 1000
    photo_quilt(file_path, width, height)
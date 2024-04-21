# start code

# import libraries
import os
from PIL import Image

# define all ctss
PATH_INPUT = "05-Professional-Section/Day-085 - Image Watermarking Desktop App - [GUI]/input"
PATH_OUTPUT = ""

# get input images from input folder
def get_input_images(path: str):
    image_files = os.listdir(path)
    images = []
    for image_file in image_files:
        if image_file.endswith((".png", ".jpg", "jpeg")):
            image_path = os.path.join(PATH_INPUT, image_file)
            image = Image.open(image_path)
            images.append(image)
    return images

# process the images
images = get_input_images(PATH_INPUT)

for _ in images:
    _.show()

print(len(images))
# write the result in the output folder

# other functionalities

# main function

# start code

# import libraries
import os
from PIL import Image

# define all ctss
PATH_INPUT = "05-Professional-Section/Day-085 - Image Watermarking Desktop App - [GUI]/input"
PATH_OUTPUT = "05-Professional-Section/Day-085 - Image Watermarking Desktop App - [GUI]/output"

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
def watermark_images(images: list):
    pass

# write the result in the output folder
def save_output_images(image: Image, path: str, image_name: str): # type: ignore
    dest_path = os.path.join(path, f"{image_name}.jpeg")
    image.save(dest_path) # type: ignore

# other functionalities

# main function
images = get_input_images(PATH_INPUT)

for _ in images:
    # _.show()
    save_output_images(_, PATH_OUTPUT, f"output_{images.index(_)}")

print(len(images))
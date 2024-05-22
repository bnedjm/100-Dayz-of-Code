import os
from PIL import Image

PATH_INPUT = "05-Professional-Section/Day-085 - Image Watermarking Desktop App - [GUI]/input"
PATH_OUTPUT = "05-Professional-Section/Day-085 - Image Watermarking Desktop App - [GUI]/output"
PATH_WM = "05-Professional-Section/Day-085 - Image Watermarking Desktop App - [GUI]/wm"

# get input images from input dir
def get_input_images(path: str):
    image_files = os.listdir(path)
    images = []
    for image_file in image_files:
        if image_file.endswith((".png", ".jpg", "jpeg")):
            image_path = os.path.join(PATH_INPUT, image_file)
            image = Image.open(image_path)
            images.append(image)
    return images

# watermark an image
def watermark_image(image: Image, watermark: Image): # type: ignore\
    image_width, image_height = image.size # type: ignore
    wm_width, wm_height = watermark.size # type: ignore
    new_width = image_width*.15
    new_height = wm_height*new_width/wm_width
    size = (int(new_width), int(new_height))
    watermark = watermark.resize(size) # type: ignore
    image.paste(watermark, (10, 10), watermark.convert("RGBA")) # type: ignore
    return image

# write image in the destination dir
def save_output_image(image: Image, path: str, image_name: str): # type: ignore
    dest_path = os.path.join(path, f"{image_name}.jpeg")
    image.save(dest_path) # type: ignore

# other functionalities

# main function
images = get_input_images(PATH_INPUT)
wm_path = os.path.join(PATH_WM, "wm.png")
watermark = Image.open(wm_path)

for _ in images:
    # _.show()
    _ = watermark_image(_, watermark) # type: ignore
    save_output_image(_, PATH_OUTPUT, f"wm_output_{images.index(_)}")

print(len(images))
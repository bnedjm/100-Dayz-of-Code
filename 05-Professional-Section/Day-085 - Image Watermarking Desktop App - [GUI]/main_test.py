import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw

class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Watermark App")

        self.images = []
        self.watermark = None

        self.create_widgets()

    def create_widgets(self):
        # Buttons
        self.select_images_button = tk.Button(self.root, text="Select Images", command=self.select_images)
        self.select_images_button.pack(pady=10)

        self.select_watermark_button = tk.Button(self.root, text="Select Watermark", command=self.select_watermark)
        self.select_watermark_button.pack(pady=5)

        self.apply_button = tk.Button(self.root, text="Apply Watermark", command=self.apply_watermark)
        self.apply_button.pack(pady=5)

    def select_images(self):
        file_paths = filedialog.askopenfilenames(title="Select Images", filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        self.images = [Image.open(file) for file in file_paths]

    def select_watermark(self):
        file_path = filedialog.askopenfilename(title="Select Watermark", filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        self.watermark = Image.open(file_path)

    def apply_watermark(self):
        if not self.images or not self.watermark:
            return

        for image in self.images:
            watermark_size = (image.width // 3, image.height // 3)
            watermark_resized = self.watermark.resize(watermark_size, Image.ANTIALIAS)

            image.paste(watermark_resized, (image.width - watermark_resized.width, image.height - watermark_resized.height), watermark_resized)

            image.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()

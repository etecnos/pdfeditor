
import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog


def photo():
    # Open file explorer
    root = tk.Tk()
    root.withdraw()
    file = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png")]
    )

    # Check if a valid file was selected
    if file:
        print(f"Selected file path: {file}")

    else:
        print("No file selected")





    image = Image.open(os.path.join(file))
    con_image = image.convert('RGB')
    name = file.split('.')
    con_image.save(os.path.join(name[0] + '.pdf'))



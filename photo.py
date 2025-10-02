
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
        return

    try:
        image = Image.open(os.path.join(file))
        con_image = image.convert('RGB')
        name = file.split('.')
        output_path = os.path.join(name[0] + '.pdf')
        con_image.save(output_path)
        print(f"PDF created successfully: {output_path}")
    except FileNotFoundError:
        print(f"Error: File not found - {file}")
    except PermissionError:
        print(f"Error: Permission denied when accessing - {file}")
    except Exception as e:
        print(f"Error converting image to PDF: {str(e)}")


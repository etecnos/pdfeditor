
from PyPDF2 import PdfReader,PdfWriter
import os
import tkinter as tk
from tkinter import filedialog



def split():
    # Open file explorer
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select a PDF file",
        filetypes=[("PDF files", "*.pdf")]
    )

    # Check if a valid file was selected
    if file_path:
        print(f"Selected file path: {file_path}")

    else:
        print("No file selected")



    file = open(file_path, "rb")

    reader = PdfReader(file)

    # Split pages
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        writer = PdfWriter()
        writer.add_page(page)
        # Create the name of the new files
        filename = os.path.splitext(file_path)[0]
        out = str(filename) + "_page_" + str(i+1) + ".pdf"
        writer.write(out)

        print("Created " + str(out))
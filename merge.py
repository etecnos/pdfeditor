
from PyPDF2 import PdfMerger
import tkinter as tk
from tkinter import filedialog


# This function is used to help the user select the files of his choice
def merge(times):
    # Open file explorer
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select the " + str(times + 1) + " file",
        filetypes=[("PDF files", "*.pdf")]
    )

    # Check if a valid file was selected
    if file_path:
        print(f"Selected file path: {file_path}")

    else:
        print("No file selected")

    return file_path

# execute function is used to merge the selected files together
def execute(files_list):
    merger = PdfMerger()

    for file in files_list:
        merger.append(file)


    merger.write("merged.pdf")


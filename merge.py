
from PyPDF2 import PdfMerger
import os
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
    try:
        merger = PdfMerger()

        for file in files_list:
            if file and os.path.exists(file):
                merger.append(file)
            else:
                print(f"Warning: Skipping invalid or non-existent file - {file}")

        merger.write("merged.pdf")
        merger.close()
        print("PDF files merged successfully: merged.pdf")
    except FileNotFoundError as e:
        print(f"Error: File not found - {str(e)}")
    except PermissionError:
        print("Error: Permission denied when creating merged PDF")
    except Exception as e:
        print(f"Error merging PDF files: {str(e)}")


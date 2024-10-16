
import tabula
import tkinter as tk
from tkinter import filedialog

def tables():
    # Open file explorer
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select the a PDF file",
        filetypes=[("PDF files", "*.pdf")]
    )

    # Check if a valid file was selected
    if file_path:
        print(f"Selected file path: {file_path}")

    else:
        print("No file selected")







    error = False
    # Check weather the file given includes tables (beta)
    try:
        tables = tabula.read_pdf(file_path, pages="all")

        # Load the tables inside a txt file
        with open("tables.txt", 'w') as file:
            for i in range(len(tables)):
                file.write(str(tables[i]) + "\n\n\n\n\n")

    except:
        print("error")
        error = True

    return error





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
        return True

    error = False
    # Check weather the file given includes tables (beta)
    try:
        tables = tabula.read_pdf(file_path, pages="all")

        # Check if tables were actually found
        if not tables or len(tables) == 0:
            print("No tables found in PDF")
            error = True
        else:
            # Load the tables inside a txt file
            with open("tables.txt", 'w') as file:
                for i in range(len(tables)):
                    file.write(str(tables[i]) + "\n\n\n\n\n")
            print(f"Successfully extracted {len(tables)} table(s) to tables.txt")
    except FileNotFoundError:
        print(f"Error: PDF file not found - {file_path}")
        error = True
    except PermissionError:
        print(f"Error: Permission denied when accessing - {file_path}")
        error = True
    except Exception as e:
        print(f"Error extracting tables from PDF: {str(e)}")
        error = True

    return error




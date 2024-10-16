from PyPDF2 import PdfReader
import tkinter as tk
from tkinter import filedialog
import string

# This function is used to help the user select the file of his choice
def give():
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

    return file_path


# detect function is used to detect the word given
def detect(path,word):
    file = open(path, "rb")
    reader = PdfReader(file)
    b = 0
    c = 0
    times = 0
    text = ""
    lines = []
    # Collect each page and its text
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        text = text + page.extract_text()

    # Line splitter
    text3 = text.splitlines()
    # Remove Punctuation
    for i in range(len(text3)):
        for j in text3[i]:
            if j in string.punctuation:
                text3[i] = text3[i].replace(j, "")

    for i in text3:
        # text2 variable hold each line word the file
        text2 = text3[c].split()
        for j in text2:
            if word == text2[b]:
                times += 1
                lines.append(str(c + 1))
            b += 1
        c += 1
        b = 0

    # Create the txt file with the results
    with open("lines.txt", 'w') as file:
        file.write("It was detected in: \n")
        for i in lines:
            file.write(f"Line {i}\n")




    return times


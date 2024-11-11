# PDF Editor

PDF editor is a Python project that is used to edit PDF files through various ways, by using graphics (pygame) and various other python libraries to access the PDFs.

## Features

By using PDF editor you will be able to:
- Convert an image to PDF
- Split a PDF file into its pages
- Merge two or more PDF files into one new file
- Detect words inside a PDF file
- Extract tables from PDF files (beta)

## Setup

### Prerequisites

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/etecnos/pdfeditor.git
    cd pdfeditor
    ```

2. Install the required Python libraries:
    ```sh
    pip install PyPDF2 Pillow tabula-py pygame tkinter string keyboard
    ```

3. Run the main program:
    ```sh
    python main.py
    ```

## Usage

1. **Convert an Image to PDF**:
    - Select the first image to convert an image to a PDF.

2. **Split a PDF File**:
    - Select the second image to split a PDF file into its pages.

3. **Merge PDF Files**:
    - Select the third image to merge multiple PDF files into one.

4. **Detect Words in a PDF**:
    - Select the fourth image to search for specific words in a PDF.

5. **Extract Tables from PDF**:
    - Select the fifth image to extract tables from a PDF (beta).

## Showcase

The following window will open while running main.py:

![monitor](https://github.com/etecnos/pdfeditor/blob/main/output/monitor.png?raw=true)

Each image corresponds to a certain function executed by the program. After finishing an operation you can close the window and have your PDF ready!

## Update
You can now go back after conducting an operation:

![back](https://github.com/etecnos/pdfeditor/blob/main/output/back.png?raw=true)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

Massive thanks to [Jimvar](https://github.com/Jimvar)

~eTecnos

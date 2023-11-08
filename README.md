# PDF Color Inverter

PDF Color Inverter is a simple yet powerful tool that helps to convert PDF files with dark backgrounds to a lighter scheme (also can from light to dark, it is decided by the file's original scheme), making them more suitable for printing. It utilizes PyMuPDF, PIL, and FPDF libraries to process PDFs and invert the colors for an optimized print-friendly version.

## Steps

- Convert PDF pages to images
- Invert colors of each image
- Reassemble images back into a single PDF

## Installation

To use PDF Color Inverter, you need to have Python installed on your machine along with the following dependencies:

- PyMuPDF
- Pillow
- FPDF

You can install these packages using pip:

```sh
pip install PyMuPDF Pillow fpdf
```

## Usage

Using PDF Color Inverter is simple. Import the main function from the script and provide it with the input and output PDF paths:

```python
from pdf_color_inverter import main

input_pdf_path = 'path_to_your_input.pdf'
output_pdf_path = 'path_to_your_output.pdf'
main(input_pdf_path, output_pdf_path)
```

Or you can just modify the paths in `pdf_color_inverter` and run it.

You can adjust **`dpi`** in `pdf_to_images(pdf_path, dpi=300)` and **`quality`** in `img.save(temp_img_file.name, format='JPEG', quality=95)` to adjust the quality of the output. Output with better quality will take longer to process.

## How It Works

1. **Converting PDF to Images**: The `pdf_to_images` function opens a PDF and converts each page into an image at a specified DPI.
2. **Inverting Image Colors**: The `invert_colors` function takes the list of images and inverts their colors to a negative.
3. **Saving Images to PDF**: The `save_images_to_pdf` function takes the inverted images and saves them back into a single PDF document.

Remember to replace `input.pdf` and `output.pdf` with the actual names of your PDF files or implement a method for users to specify their file names. Also, don't forget to include a `LICENSE` file in your repository with the open source license you choose to use.

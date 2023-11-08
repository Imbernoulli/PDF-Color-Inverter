import fitz
from PIL import Image, ImageOps
from fpdf import FPDF
import io
import tempfile


def pdf_to_images(pdf_path, dpi=300):
    doc = fitz.open(pdf_path)
    images = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        pix = page.get_pixmap(dpi=dpi, colorspace="RGB")
        img_data = pix.tobytes()
        img = Image.open(io.BytesIO(img_data))
        images.append(img)
    doc.close()
    return images


def invert_colors(images):
    inverted_images = []
    for img in images:
        inverted_img = ImageOps.invert(img.convert("RGB"))
        inverted_images.append(inverted_img)
    return inverted_images


def save_images_to_pdf(images, output_pdf_path):
    pdf = FPDF(unit="pt", format=[images[0].width, images[0].height])
    for img in images:
        pdf.add_page()
        with tempfile.NamedTemporaryFile(suffix=".jpg") as temp_img_file:
            img.save(temp_img_file.name, format='JPEG', quality=95)
            pdf.image(temp_img_file.name, 0, 0)
    pdf.output(output_pdf_path)


def main(pdf_path, output_pdf_path):
    images = pdf_to_images(pdf_path)
    inverted_images = invert_colors(images)
    save_images_to_pdf(inverted_images, output_pdf_path)

# Change the following paths to your input and output pdf paths
input_pdf_path = 'path_to_your_input.pdf'
output_pdf_path = 'path_to_your_output.pdf'
main(input_pdf_path, output_pdf_path)

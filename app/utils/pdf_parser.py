import pdfplumber


def extract_text(path):

    text = ""

    with pdfplumber.open(path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text

    return text
import PyPDF2

def extract_text(pdf_path):

    text = ""

    with open(pdf_path,"rb") as file:
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            text += page.extract_text()

    return text
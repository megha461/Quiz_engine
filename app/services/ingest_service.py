import os
from ..utils.pdf_parser import extract_text
from ..utils.chunker import chunk_text
UPLOAD_DIR = "data/pdfs"
def ingest_pdf(file):
    path = os.path.join(UPLOAD_DIR, file.filename)
    with open(path, "wb") as f:
        f.write(file.file.read())

    text = extract_text(path)

    chunks = chunk_text(text)

    return {
        "message": "PDF processed",
        "chunks_created": len(chunks)
    }
from ..utils.pdf_parser import extract_text

def ingest_pdf():

    text = extract_text("data/pdfs/sample.pdf")

    return {
        "message": "PDF processed",
        "characters": len(text)
    }
import pdfplumber

async def ingest_pdf(file):
    text = ""

    with pdfplumber.open(file.file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()

    chunks = text.split(".")[:5]  # simple chunking

    return chunks
from pathlib import Path

from chunking import create_chunks
from pdf_parser import extract_pages


def ingest_pdf(pdf_path: str) -> list[dict]:
    """Parse a single PDF and return chunks with document + page metadata."""
    doc_name = Path(pdf_path).name
    pages = extract_pages(pdf_path)
    return create_chunks(pages, document=doc_name)


def ingest_upload(file) -> list[dict]:
    """Parse an uploaded file object and return chunks."""
    doc_name = getattr(file, "name", "uploaded.pdf")
    pages = extract_pages(file)
    return create_chunks(pages, document=doc_name)


def ingest_directory(dir_path: str) -> list[dict]:
    """Parse all PDFs in a directory (recursive) and return combined chunks."""
    root = Path(dir_path)
    if not root.is_dir():
        raise NotADirectoryError(f"Not a directory: {dir_path}")

    pdfs = sorted(root.glob("**/*.pdf"))
    if not pdfs:
        raise FileNotFoundError(f"No PDF files found in {dir_path}")

    chunks = []
    for pdf in pdfs:
        chunks.extend(ingest_pdf(str(pdf)))
    return chunks

import fitz


def _open_pdf(pdf_source):
    if hasattr(pdf_source, "read"):
        return fitz.open(stream=pdf_source.read(), filetype="pdf")
    return fitz.open(pdf_source)


def extract_pages(pdf_source):
    """Return a list of {page, text} dicts (1-based page numbers)."""
    doc = _open_pdf(pdf_source)
    try:
        pages = []
        for page_num, page in enumerate(doc):
            pages.append({"page": page_num + 1, "text": page.get_text()})
        return pages
    finally:
        doc.close()



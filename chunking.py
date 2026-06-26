from langchain_text_splitters import RecursiveCharacterTextSplitter

_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)


def create_chunks(pages, document: str = "document.pdf"):
    """Split page text into chunks, preserving document name and page numbers."""
    chunks = []
    for page in pages:
        if not page["text"].strip():
            continue
        for text in _splitter.split_text(page["text"]):
            chunks.append(
                {
                    "text": text,
                    "page": page["page"],
                    "document": document,
                }
            )
    return chunks

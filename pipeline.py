"""
MediComind RAG pipeline orchestrator.
"""

from generator import generate_answer
from ingestion import ingest_directory, ingest_pdf, ingest_upload
from library import register_document, remove_document
from prompt_builder import format_annotated_answer
from vector_store import delete_document, retrieve_chunks, store_chunks


def _doc_stats(chunks: list[dict]) -> dict:
    if not chunks:
        return {"pages": 0, "chunks": 0, "document": ""}
    doc = chunks[0]["document"]
    pages = max(c["page"] for c in chunks)
    return {"document": doc, "pages": pages, "chunks": len(chunks)}


def index_from_upload(file, reset: bool = False) -> list[dict]:
    chunks = ingest_upload(file)
    store_chunks(chunks, reset=reset)
    stats = _doc_stats(chunks)
    size = getattr(file, "size", 0) or 0
    register_document(stats["document"], stats["chunks"], stats["pages"], size)
    return chunks


def index_from_path(pdf_path: str, reset: bool = True) -> list[dict]:
    chunks = ingest_pdf(pdf_path)
    store_chunks(chunks, reset=reset)
    stats = _doc_stats(chunks)
    register_document(stats["document"], stats["chunks"], stats["pages"])
    return chunks


def index_from_directory(dir_path: str) -> list[dict]:
    chunks = ingest_directory(dir_path)
    store_chunks(chunks, reset=True)
    by_doc: dict[str, list] = {}
    for chunk in chunks:
        by_doc.setdefault(chunk["document"], []).append(chunk)
    for doc, doc_chunks in by_doc.items():
        pages = max(c["page"] for c in doc_chunks)
        register_document(doc, len(doc_chunks), pages)
    return chunks


def remove_from_library(document: str):
    delete_document(document)
    remove_document(document)


def query(question: str, n_results: int = 3, document: str | None = None) -> dict:
    retrieved = retrieve_chunks(question, n_results=n_results, document=document)
    answer = generate_answer(question, retrieved)
    annotated = format_annotated_answer(answer, retrieved)
    return {
        "answer": answer,
        "annotated": annotated,
        "sources": retrieved,
    }

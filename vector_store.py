import hashlib

import chromadb
import ollama

EMBED_MODEL = "nomic-embed-text"
COLLECTION_NAME = "papers"

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name=COLLECTION_NAME)


def generate_embedding(text):
    response = ollama.embeddings(model=EMBED_MODEL, prompt=text)
    return response["embedding"]


def clear_collection():
    global collection
    client.delete_collection(COLLECTION_NAME)
    collection = client.get_or_create_collection(name=COLLECTION_NAME)


def store_chunks(chunks, reset: bool = False):
    if reset:
        clear_collection()
    else:
        docs = {c["document"] for c in chunks}
        for doc in docs:
            try:
                collection.delete(where={"document": doc})
            except Exception:
                pass

    for chunk in chunks:
        text = chunk["text"]
        page = chunk["page"]
        document = chunk["document"]
        doc_id = hashlib.md5(f"{document}:{page}:{text}".encode()).hexdigest()
        embedding = generate_embedding(text)
        collection.add(
            ids=[doc_id],
            embeddings=[embedding],
            documents=[text],
            metadatas=[{"page": page, "document": document}],
        )


def delete_document(document: str):
    try:
        collection.delete(where={"document": document})
    except Exception:
        pass


def get_index_stats() -> dict:
    count = collection.count()
    if count == 0:
        return {"chunks": 0, "documents": []}

    results = collection.get(include=["metadatas"])
    documents = sorted({m["document"] for m in results["metadatas"]})
    return {"chunks": count, "documents": documents}


def get_library_details() -> list[dict]:
    if collection.count() == 0:
        return []

    results = collection.get(include=["metadatas"])
    by_doc: dict[str, dict] = {}
    for meta in results["metadatas"]:
        doc = meta["document"]
        page = meta["page"]
        if doc not in by_doc:
            by_doc[doc] = {"chunks": 0, "pages": set()}
        by_doc[doc]["chunks"] += 1
        by_doc[doc]["pages"].add(page)

    return [
        {
            "document": doc,
            "chunks": info["chunks"],
            "pages": max(info["pages"]),
        }
        for doc, info in sorted(by_doc.items())
    ]


def retrieve_chunks(question, n_results=3, document: str | None = None):
    if collection.count() == 0:
        return []

    question_embedding = generate_embedding(question)
    kwargs = {
        "query_embeddings": [question_embedding],
        "n_results": min(n_results, collection.count()),
    }
    if document and document != "All papers":
        kwargs["where"] = {"document": document}

    results = collection.query(**kwargs)
    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    return [
        {
            "text": doc,
            "page": meta["page"],
            "document": meta["document"],
        }
        for doc, meta in zip(documents, metadatas)
    ]

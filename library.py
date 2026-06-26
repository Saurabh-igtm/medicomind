import json
from datetime import datetime, timezone
from pathlib import Path

LIBRARY_DIR = Path("./data")
LIBRARY_FILE = LIBRARY_DIR / "library.json"


def _ensure_dir():
    LIBRARY_DIR.mkdir(parents=True, exist_ok=True)


def load_library() -> dict:
    _ensure_dir()
    if not LIBRARY_FILE.exists():
        return {}
    with LIBRARY_FILE.open(encoding="utf-8") as f:
        return json.load(f)


def save_library(library: dict):
    _ensure_dir()
    with LIBRARY_FILE.open("w", encoding="utf-8") as f:
        json.dump(library, f, indent=2, ensure_ascii=False)


def register_document(name: str, chunks: int, pages: int, size_bytes: int = 0):
    library = load_library()
    library[name] = {
        "chunks": chunks,
        "pages": pages,
        "size_bytes": size_bytes,
        "indexed_at": datetime.now(timezone.utc).isoformat(),
    }
    save_library(library)


def remove_document(name: str):
    library = load_library()
    library.pop(name, None)
    save_library(library)


def get_recent_documents(limit: int = 5) -> list[dict]:
    library = load_library()
    items = [
        {"document": name, **meta}
        for name, meta in library.items()
    ]
    items.sort(key=lambda x: x.get("indexed_at", ""), reverse=True)
    return items[:limit]

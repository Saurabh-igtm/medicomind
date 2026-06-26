import json
from datetime import datetime, timezone
from pathlib import Path

HISTORY_DIR = Path("./data")
HISTORY_FILE = HISTORY_DIR / "chat_history.json"


def _ensure_data_dir():
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)


def load_history(limit: int | None = 50) -> list[dict]:
    _ensure_data_dir()
    if not HISTORY_FILE.exists():
        return []

    with HISTORY_FILE.open(encoding="utf-8") as f:
        history = json.load(f)

    if limit is not None:
        return history[-limit:]
    return history


def save_turn(question: str, answer: str, sources: list[dict]) -> dict:
    _ensure_data_dir()
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "question": question,
        "answer": answer,
        "sources": sources,
    }

    history = load_history(limit=None)
    history.append(entry)

    with HISTORY_FILE.open("w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

    return entry


def clear_history():
    _ensure_data_dir()
    with HISTORY_FILE.open("w", encoding="utf-8") as f:
        json.dump([], f)

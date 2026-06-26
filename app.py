import sys

from chat_history import load_history
from pipeline import index_from_directory, index_from_path, query


if __name__ == "__main__":
  if len(sys.argv) > 1 and sys.argv[1] == "--dir":
    path = sys.argv[2] if len(sys.argv) > 2 else "./papers"
    chunks = index_from_directory(path)
    print(f"Indexed {len(chunks)} chunks from {path}")
  else:
    chunks = index_from_path("sample.pdf")
    print(f"Indexed {len(chunks)} chunks from sample.pdf")

  while True:
    question = input("\nAsk Question (or 'quit' / 'history'): ").strip()
    if question.lower() in {"quit", "exit", "q"}:
      break
    if question.lower() == "history":
      for entry in load_history():
        print(f"\n[{entry['timestamp']}] Q: {entry['question']}")
        print(f"A: {entry['answer'][:200]}...")
      continue
    if not question:
      continue

    result = query(question)
    print("\nAnswer:")
    print(result["answer"])
    print("\nSources:")
    for i, src in enumerate(result["sources"], start=1):
      print(
        f"  [{i}] {src['document']} p.{src['page']}: "
        f"{src['text'][:120]}..."
      )

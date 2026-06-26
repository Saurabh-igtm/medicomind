"""Local LLM inference via Ollama (llama3.2:1b)."""

import ollama

from prompt_builder import build_prompt

CHAT_MODEL = "llama3.2:1b"


def run_inference(prompt: str) -> str:
    response = ollama.chat(
        model=CHAT_MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    return response["message"]["content"]


def generate_answer(question: str, retrieved_chunks: list[dict]) -> str:
    if not retrieved_chunks:
        return "I could not find this in the uploaded document."

    prompt = build_prompt(question, retrieved_chunks)
    return run_inference(prompt)

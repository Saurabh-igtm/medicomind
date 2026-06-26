"""Prompt Builder — assembles context + citation rules for the local LLM."""


def format_context(chunks):
    parts = []
    for i, chunk in enumerate(chunks, start=1):
        parts.append(
            f"[Source {i} | {chunk['document']} | Page {chunk['page']}]\n"
            f"{chunk['text']}"
        )
    return "\n\n".join(parts)


def build_prompt(question: str, retrieved_chunks: list[dict]) -> str:
    context = format_context(retrieved_chunks)
    citations = sorted(
        {(c["document"], c["page"]) for c in retrieved_chunks},
        key=lambda x: (x[0], x[1]),
    )
    citation_hint = ", ".join(f"[{doc}, p.{page}]" for doc, page in citations)

    return f"""You are MediComind, a medical study assistant for students.

Answer using ONLY the provided context from uploaded research documents.
If the answer is not in the context, say: "I could not find this in the uploaded document."

Rules:
- Be accurate and concise, suitable for medical students.
- Every factual claim MUST end with an inline citation in exactly this format: [filename.pdf, p.X]
- Example answer style: "Type 2 diabetes involves insulin resistance [sample.pdf, p.1]."
- Use ONLY these valid citations: {citation_hint}
- Never write [Source 1], [1], or [Page 1] — only [document.pdf, p.X].

Context:
{context}

Question:
{question}
"""


def format_annotated_answer(answer: str, sources: list[dict]) -> str:
    """Render final Markdown answer with a citations footer."""
    if not sources:
        return answer

    lines = [answer, "", "---", "**Citations**"]
    for i, src in enumerate(sources, start=1):
        lines.append(
            f"{i}. **{src['document']}**, p.{src['page']}  \n"
            f"> {src['text'][:300]}{'…' if len(src['text']) > 300 else ''}"
        )
    return "\n".join(lines)

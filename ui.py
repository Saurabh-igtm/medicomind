import streamlit as st

from chat_history import clear_history, load_history, save_turn
from library import get_recent_documents, load_library
from pipeline import index_from_upload, query, remove_from_library
from ui_styles import CUSTOM_CSS
from vector_store import get_index_stats, get_library_details

st.set_page_config(
    page_title="MediComind",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.markdown(f"<style>{CUSTOM_CSS}</style>", unsafe_allow_html=True)

NAV = [
    ("🏠  Home", "Home"),
    ("💬  Ask a Question", "Ask a Question"),
    ("📤  Upload Papers", "Upload Papers"),
    ("📚  My Library", "My Library"),
    ("⭐  Saved Chats", "Saved Chats"),
    ("ℹ️  About", "About"),
]

EXAMPLES = [
    "What are the diagnostic criteria for diabetes?",
    "Summarize this paper.",
    "What is the first-line treatment?",
]

for key, default in [
    ("page", "Home"),
    ("messages", []),
    ("pending_question", ""),
    ("selected_paper", "All papers"),
]:
    if key not in st.session_state:
        st.session_state[key] = default


# ── Helpers ───────────────────────────────────────────────────────────────────

def has_index() -> bool:
    return get_index_stats()["chunks"] > 0


def fmt_size(n: int) -> str:
    return f"{n / (1024 * 1024):.1f} MB" if n > 0 else ""


def fmt_time(iso: str) -> str:
    return iso[:19].replace("T", " ") if iso else ""


def paper_options() -> list[str]:
    docs = get_index_stats()["documents"]
    return ["All papers"] + docs if docs else ["All papers"]


def page_title(icon: str, title: str, subtitle: str = ""):
    sub = f"<p>{subtitle}</p>" if subtitle else ""
    st.markdown(
        f'<div class="page-header"><h1>{icon} {title}</h1>{sub}</div>',
        unsafe_allow_html=True,
    )


def paper_card_html(name: str, meta_parts: list[str]) -> str:
    tags = "".join(f"<span>{p}</span>" for p in meta_parts)
    return f"""
    <div class="paper-card">
        <div class="paper-icon">📄</div>
        <div style="min-width:0;flex:1;">
            <div class="paper-name">{name}</div>
            <div class="paper-meta">{tags}</div>
        </div>
    </div>"""


def empty_state(icon: str, title: str, desc: str) -> str:
    return f"""
    <div class="empty-state">
        <div class="icon">{icon}</div>
        <h3>{title}</h3>
        <p>{desc}</p>
    </div>"""


# ── Fixed sidebar ─────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        """
        <div class="brand-wrap">
            <div class="brand-logo">🩺</div>
            <div>
                <div class="brand-name">MediComind</div>
                <div class="brand-tag">AI Medical Research Assistant</div>
            </div>
        </div>
        <div class="sidebar-body">
        """,
        unsafe_allow_html=True,
    )

    labels = [n[0] for n in NAV]
    keys = [n[1] for n in NAV]
    idx = keys.index(st.session_state.page) if st.session_state.page in keys else 0
    choice = st.radio("nav", labels, index=idx, label_visibility="collapsed")
    st.session_state.page = keys[labels.index(choice)]

    stats = get_index_stats()
    if stats["chunks"]:
        st.markdown(
            f"""
            <div class="sidebar-stat">
                <div class="num">{stats['chunks']}</div>
                <div class="lbl">chunks · {len(stats['documents'])} papers indexed</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="sidebar-bottom">
            <div class="sidebar-footer">
                Made with ❤️ by MediComind
                <div class="offline-pill">🔒 100% Offline · Edge Ready</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ── Home ──────────────────────────────────────────────────────────────────────
def page_home():
    st.markdown(
        """
        <div class="hero-banner">
            <div class="hero-emoji">🩺</div>
            <p class="hero-title">Welcome to MediComind</p>
            <p class="hero-desc">
                Ask questions, get cited insights, and explore medical research papers —
                powered by local AI on your device.
            </p>
            <div class="hero-badges">
                <span class="badge">🔒 100% Offline</span>
                <span class="badge">⚡ Edge Optimized</span>
                <span class="badge">📌 Cited Answers</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    stats = get_index_stats()
    st.markdown(
        f"""
        <div class="stat-row">
            <div class="stat-card blue">
                <div class="icon">📚</div>
                <div class="value">{len(stats['documents'])}</div>
                <div class="label">Papers Indexed</div>
            </div>
            <div class="stat-card teal">
                <div class="icon">🧩</div>
                <div class="value">{stats['chunks']}</div>
                <div class="label">Text Chunks</div>
            </div>
            <div class="stat-card violet">
                <div class="icon">🤖</div>
                <div class="value">Local</div>
                <div class="label">Ollama + ChromaDB</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="search-card"><div class="search-label">Ask anything about your research</div></div>', unsafe_allow_html=True)
    c1, c2 = st.columns([4, 1])
    with c1:
        q = st.text_input(
            "home_q",
            value=st.session_state.pending_question,
            placeholder="e.g. What are the diagnostic criteria for diabetes?",
            label_visibility="collapsed",
        )
    with c2:
        ask_btn = st.button("✨ Ask", type="primary", use_container_width=True)

    if ask_btn and q.strip():
        st.session_state.pending_question = q.strip()
        st.session_state.page = "Ask a Question"
        st.rerun()

    st.markdown('<p class="section-title">💡 Try an example</p>', unsafe_allow_html=True)
    ex1, ex2, ex3 = st.columns(3)
    for col, example, i in zip([ex1, ex2, ex3], EXAMPLES, range(3)):
        with col:
            if st.button(example, key=f"ex_{i}", use_container_width=True):
                st.session_state.pending_question = example
                st.session_state.page = "Ask a Question"
                st.rerun()

    st.markdown('<p class="section-title">📄 Recent Papers</p>', unsafe_allow_html=True)
    recent = get_recent_documents()
    if not recent:
        st.markdown(
            empty_state("📂", "No papers yet", "Upload a medical PDF from Upload Papers to get started."),
            unsafe_allow_html=True,
        )
    else:
        for item in recent:
            parts = [f"{item['pages']} pages", f"{item['chunks']} chunks"]
            size = fmt_size(item.get("size_bytes", 0))
            if size:
                parts.append(size)
            if item.get("indexed_at"):
                parts.append(fmt_time(item["indexed_at"]))
            st.markdown(paper_card_html(item["document"], parts), unsafe_allow_html=True)


# ── Ask ───────────────────────────────────────────────────────────────────────
def page_ask():
    page_title("💬", "Ask a Question", "Semantic search + local LLM — every answer includes citations.")

    if not has_index():
        st.markdown(
            empty_state("📤", "No papers indexed", "Head to Upload Papers and index a PDF first."),
            unsafe_allow_html=True,
        )
        if st.button("Go to Upload Papers", type="primary", use_container_width=True):
            st.session_state.page = "Upload Papers"
            st.rerun()
        return

    st.markdown('<div class="toolbar-card">', unsafe_allow_html=True)
    t1, t2 = st.columns([3, 1])
    papers = paper_options()
    pidx = papers.index(st.session_state.selected_paper) if st.session_state.selected_paper in papers else 0
    with t1:
        st.markdown('<p style="font-size:0.75rem;font-weight:600;color:#64748b;margin:0 0 0.35rem;">TARGET PAPER</p>', unsafe_allow_html=True)
        selected = st.selectbox("Target paper", papers, index=pidx, label_visibility="collapsed")
        st.session_state.selected_paper = selected
    with t2:
        st.markdown('<p style="font-size:0.75rem;font-weight:600;color:#64748b;margin:0 0 0.35rem;">&nbsp;</p>', unsafe_allow_html=True)
        if st.button("📋 Summarize", use_container_width=True):
            st.session_state.pending_question = "Summarize this paper."
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="chat-panel">', unsafe_allow_html=True)
    if not st.session_state.messages:
        st.markdown(
            '<p class="chat-empty">Start a conversation — answers include inline citations and page references.</p>',
            unsafe_allow_html=True,
        )
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"], avatar="🧑‍⚕️" if msg["role"] == "user" else "🩺"):
            st.markdown(msg["content"])
    st.markdown("</div>", unsafe_allow_html=True)

    default_q = st.session_state.pending_question
    if default_q:
        st.session_state.pending_question = ""

    question = st.chat_input("Ask about your medical documents…")
    if not question and default_q:
        question = default_q

    if question:
        st.session_state.messages.append({"role": "user", "content": question})
        doc_filter = None if selected == "All papers" else selected
        with st.spinner("🔍 Retrieving passages → generating answer…"):
            result = query(question.strip(), document=doc_filter)
        st.session_state.messages.append({"role": "assistant", "content": result["annotated"]})
        save_turn(question, result["answer"], result["sources"])
        st.rerun()


# ── Upload ────────────────────────────────────────────────────────────────────
def page_upload():
    page_title("📤", "Upload Papers", "PDFs are parsed, chunked, and embedded locally. Nothing leaves your device.")

    st.markdown('<div class="upload-wrap">', unsafe_allow_html=True)
    uploaded_files = st.file_uploader(
        "Drop PDF files here",
        type=["pdf"],
        accept_multiple_files=True,
        label_visibility="collapsed",
    )
    st.markdown("</div>", unsafe_allow_html=True)

    if uploaded_files:
        for f in uploaded_files:
            size = fmt_size(f.size or 0)
            st.markdown(paper_card_html(f.name, [size] if size else ["Ready to index"]), unsafe_allow_html=True)

        if st.button("🚀 Index Papers", type="primary", use_container_width=True):
            lib = load_library()
            for f in uploaded_files:
                if f.name in lib:
                    st.info(f"ℹ️ **{f.name}** is already in your library — re-indexing…")
                with st.spinner(f"Indexing {f.name}…"):
                    chunks = index_from_upload(f, reset=False)
                    pages = max(c["page"] for c in chunks) if chunks else 0
                    st.success(f"✅ **{f.name}** — {pages} pages · {len(chunks)} chunks indexed!")

    st.markdown('<p class="section-title">📚 Indexed Papers</p>', unsafe_allow_html=True)
    _render_library(show_delete=True)


# ── Library ───────────────────────────────────────────────────────────────────
def page_library():
    page_title("📚", "My Library", "All papers in your local ChromaDB vector store.")
    _render_library(show_delete=True)


def _render_library(show_delete: bool = False):
    details = get_library_details()
    lib_meta = load_library()

    if not details:
        st.markdown(
            empty_state("📚", "Library is empty", "Upload research PDFs to build your local knowledge base."),
            unsafe_allow_html=True,
        )
        return

    for item in details:
        meta = lib_meta.get(item["document"], {})
        parts = [f"{item['pages']} pages", f"{item['chunks']} chunks"]
        size = fmt_size(meta.get("size_bytes", 0))
        if size:
            parts.append(size)
        if meta.get("indexed_at"):
            parts.append(fmt_time(meta["indexed_at"]))

        if show_delete:
            c1, c2 = st.columns([8, 1])
            with c1:
                st.markdown(paper_card_html(item["document"], parts), unsafe_allow_html=True)
            with c2:
                st.markdown("<div style='padding-top:1.2rem;'>", unsafe_allow_html=True)
                if st.button("🗑️", key=f"del_{item['document']}", help="Remove"):
                    remove_from_library(item["document"])
                    st.rerun()
                st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.markdown(paper_card_html(item["document"], parts), unsafe_allow_html=True)


# ── Saved Chats ───────────────────────────────────────────────────────────────
def page_saved():
    page_title("⭐", "Saved Chats", "Conversations stored locally on your device.")

    history = load_history(limit=None)
    if not history:
        st.markdown(
            empty_state("💬", "No saved chats", "Ask a question and your conversation will appear here."),
            unsafe_allow_html=True,
        )
        return

    if st.button("🗑️ Clear all history", use_container_width=True):
        clear_history()
        st.session_state.messages = []
        st.rerun()

    for entry in reversed(history):
        ts = fmt_time(entry["timestamp"])
        label = entry["question"][:70] + ("…" if len(entry["question"]) > 70 else "")
        with st.expander(f"🕐 {ts}  ·  {label}"):
            st.markdown(f"**Question**  \n{entry['question']}")
            st.markdown("---")
            st.markdown(f"**Answer**  \n{entry['answer']}")
            if entry.get("sources"):
                st.markdown("**Sources**")
                tags = "".join(
                    f'<span class="citation-tag">{s["document"]} · p.{s["page"]}</span>'
                    for s in entry["sources"]
                )
                st.markdown(tags, unsafe_allow_html=True)


# ── About ─────────────────────────────────────────────────────────────────────
def page_about():
    page_title("ℹ️", "About — Project & RAG Pipeline")

    st.markdown(
        """
        <div class="info-card">
            <h2>📘 About the Project</h2>
            <p>
                MediComind is a <span class="hl-blue">Retrieval-Augmented Generation (RAG)</span>
                assistant for medical students. Upload research papers, index them into a local
                vector database, and query them in natural language — with inline citations and
                page references. Everything runs <strong>completely offline</strong>.
            </p>
            <div class="tech-bar">
                Built for edge AI deployment using
                <span class="hl-teal">NVIDIA Jetson</span> +
                <span class="hl-blue">Ollama</span>
            </div>
        </div>
        <div class="info-card">
            <h2>🧠 How It Works</h2>
            <div class="step-grid">
                <div class="step-card s-upload"><div class="si">📄</div><div class="st">Upload</div><div class="ss">Drop your PDF</div></div>
                <div class="step-card s-extract"><div class="si">📝</div><div class="st">Extract</div><div class="ss">Parse text & pages</div></div>
                <div class="step-card s-chunk"><div class="si">✂️</div><div class="st">Chunk</div><div class="ss">Split passages</div></div>
                <div class="step-card s-embed"><div class="si">🧮</div><div class="st">Embed</div><div class="ss">Generate vectors</div></div>
                <div class="step-card s-store"><div class="si">💾</div><div class="st">Store</div><div class="ss">Index ChromaDB</div></div>
                <div class="step-card s-retrieve"><div class="si">🔍</div><div class="st">Retrieve</div><div class="ss">Semantic search</div></div>
                <div class="step-card s-generate"><div class="si">🤖</div><div class="st">Generate</div><div class="ss">LLM via Ollama</div></div>
                <div class="step-card s-answer"><div class="si">✅</div><div class="st">Answer</div><div class="ss">Cited response</div></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ── Router ────────────────────────────────────────────────────────────────────
{
    "Home": page_home,
    "Ask a Question": page_ask,
    "Upload Papers": page_upload,
    "My Library": page_library,
    "Saved Chats": page_saved,
    "About": page_about,
}[st.session_state.page]()

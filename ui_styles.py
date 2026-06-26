"""MediComind — responsive UI styles."""

CUSTOM_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

/* ── Variables ─────────────────────────────────────────────── */
:root {
    --sidebar-w: 272px;
    --blue: #2563eb;
    --blue-dark: #1d4ed8;
    --slate-900: #0f172a;
    --slate-600: #475569;
    --slate-400: #94a3b8;
    --border: #e2e8f0;
    --bg: #f1f5f9;
    --card: #ffffff;
    --radius: 14px;
    --shadow: 0 4px 24px rgba(15, 23, 42, 0.06);
}

/* ── Base ──────────────────────────────────────────────────── */
html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
    -webkit-font-smoothing: antialiased;
}
#MainMenu, footer, header { visibility: hidden; height: 0 !important; }

/* App background */
[data-testid="stAppViewContainer"] {
    background: var(--bg) !important;
}

/* ── SIDEBAR (visual only — Streamlit handles positioning) ─── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%) !important;
    border-right: 1px solid var(--border) !important;
    box-shadow: 2px 0 16px rgba(15, 23, 42, 0.06) !important;
}

[data-testid="stSidebar"] > div:first-child {
    padding: 1.5rem 1rem 1rem 1rem !important;
    display: flex !important;
    flex-direction: column !important;
    scrollbar-width: thin;
    scrollbar-color: #cbd5e1 transparent;
}
[data-testid="stSidebar"] > div:first-child::-webkit-scrollbar { width: 4px; }
[data-testid="stSidebar"] > div:first-child::-webkit-scrollbar-thumb {
    background: #cbd5e1; border-radius: 4px;
}

/* ── MAIN CONTENT ────────────────────────────────────── */
section[data-testid="stMain"] {
    background: var(--bg) !important;
    min-height: 100vh !important;
    width: 100% !important;
    min-width: 0 !important;
}

/* Target both old and new Streamlit block container testids */
section[data-testid="stMain"] .block-container,
[data-testid="stMainBlockContainer"] {
    max-width: none !important;
    width: 100% !important;
    padding-top: 2rem !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
    padding-bottom: 3rem !important;
    box-sizing: border-box !important;
}

/* Prevent internal Streamlit elements from overflowing */
[data-testid="stHorizontalBlock"],
[data-testid="column"],
[data-testid="stVerticalBlock"] {
    max-width: 100% !important;
    min-width: 0 !important;
    box-sizing: border-box !important;
}

/* Sidebar collapse button */
[data-testid="collapsedControl"] {
    background: var(--card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    box-shadow: var(--shadow) !important;
}

/* ── Sidebar nav ───────────────────────────────────────────── */
[data-testid="stSidebar"] [data-testid="stRadio"] > div {
    gap: 3px !important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] label {
    background: transparent !important;
    border: 1px solid transparent !important;
    border-radius: 11px !important;
    padding: 0.62rem 0.9rem !important;
    font-weight: 500 !important;
    font-size: 0.875rem !important;
    color: var(--slate-600) !important;
    transition: all 0.18s ease !important;
    width: 100% !important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
    background: #f1f5f9 !important;
    color: var(--slate-900) !important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] label[data-checked="true"] {
    background: linear-gradient(135deg, #eff6ff, #dbeafe) !important;
    border-color: #bfdbfe !important;
    color: var(--blue-dark) !important;
    font-weight: 700 !important;
    box-shadow: 0 2px 10px rgba(37, 99, 235, 0.14) !important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] div[role="radiogroup"] > label > div:first-child {
    display: none !important;
}

.sidebar-body { flex: 1 1 auto; }
.sidebar-bottom {
    margin-top: auto;
    padding-top: 1rem;
    border-top: 1px solid var(--border);
}

/* ── Brand ─────────────────────────────────────────────────── */
.brand-wrap {
    display: flex; align-items: center; gap: 12px;
    padding-bottom: 1.25rem;
    margin-bottom: 0.5rem;
    border-bottom: 1px solid var(--border);
}
.brand-logo {
    width: 42px; height: 42px; flex-shrink: 0;
    background: linear-gradient(135deg, #0ea5e9, var(--blue));
    border-radius: 13px;
    display: flex; align-items: center; justify-content: center;
    font-size: 20px;
    box-shadow: 0 4px 16px rgba(37, 99, 235, 0.3);
}
.brand-name {
    font-size: 1.05rem; font-weight: 800;
    color: var(--slate-900); letter-spacing: -0.02em; line-height: 1.2;
}
.brand-tag {
    font-size: 0.68rem; font-weight: 500; color: #64748b; margin-top: 2px;
}
.sidebar-stat {
    background: linear-gradient(135deg, #eff6ff, #f0f9ff);
    border: 1px solid #bfdbfe;
    border-radius: 12px;
    padding: 0.8rem 1rem;
    margin: 0.75rem 0;
}
.sidebar-stat .num { font-size: 1.35rem; font-weight: 800; color: var(--blue); }
.sidebar-stat .lbl { font-size: 0.72rem; color: #64748b; font-weight: 500; margin-top: 2px; }
.sidebar-footer {
    font-size: 0.7rem; color: var(--slate-400);
    text-align: center; line-height: 1.6;
}
.offline-pill {
    display: inline-flex; align-items: center; gap: 5px;
    background: #f0fdf4; color: #15803d;
    border: 1px solid #bbf7d0;
    font-size: 0.65rem; font-weight: 700;
    padding: 3px 10px; border-radius: 999px;
    margin-top: 8px;
}

/* ── Page header ───────────────────────────────────────────── */
.page-header { margin-bottom: 1.5rem; }
.page-header h1 {
    font-size: clamp(1.4rem, 3vw, 1.85rem);
    font-weight: 800; color: var(--slate-900);
    letter-spacing: -0.03em; margin: 0 0 0.3rem;
}
.page-header p {
    color: #64748b; font-size: clamp(0.85rem, 2vw, 0.95rem);
    margin: 0; line-height: 1.55;
}

/* ── Hero ──────────────────────────────────────────────────── */
.hero-banner {
    background: linear-gradient(135deg, #0f172a 0%, #1e3a5f 55%, var(--blue) 100%);
    border-radius: clamp(16px, 3vw, 24px);
    padding: clamp(2rem, 5vw, 3rem) clamp(1.25rem, 4vw, 2.5rem);
    text-align: center; margin-bottom: 1.75rem;
    position: relative; overflow: hidden;
    box-shadow: 0 20px 50px rgba(29, 78, 216, 0.22);
}
.hero-banner::before {
    content: ''; position: absolute; top: -40%; right: -15%;
    width: min(400px, 80vw); height: min(400px, 80vw);
    background: radial-gradient(circle, rgba(14,165,233,0.28) 0%, transparent 70%);
    border-radius: 50%; pointer-events: none;
}
.hero-emoji { font-size: clamp(2.5rem, 6vw, 3.5rem); margin-bottom: 0.5rem; position: relative; }
.hero-title {
    font-size: clamp(1.5rem, 4vw, 2.2rem); font-weight: 800; color: #fff;
    letter-spacing: -0.03em; margin: 0; position: relative;
}
.hero-desc {
    color: #94a3b8; font-size: clamp(0.9rem, 2.5vw, 1.05rem);
    margin: 0.65rem auto 0; max-width: 520px; line-height: 1.6; position: relative;
}
.hero-badges {
    display: flex; justify-content: center; gap: 8px;
    margin-top: 1.1rem; flex-wrap: wrap; position: relative;
}
.badge {
    background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.18);
    color: #e2e8f0; font-size: clamp(0.65rem, 1.8vw, 0.75rem); font-weight: 600;
    padding: 0.3rem 0.75rem; border-radius: 999px;
}

/* ── Stats ─────────────────────────────────────────────────── */
.stat-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: clamp(10px, 2vw, 14px);
    margin-bottom: 1.75rem;
}
.stat-card {
    background: var(--card); border: 1px solid var(--border);
    border-radius: var(--radius); padding: clamp(1rem, 2.5vw, 1.25rem);
    text-align: center;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
}
.stat-card:hover { transform: translateY(-2px); box-shadow: var(--shadow); }
.stat-card .icon { font-size: clamp(1.2rem, 3vw, 1.5rem); margin-bottom: 0.3rem; }
.stat-card .value {
    font-size: clamp(1.3rem, 3.5vw, 1.75rem);
    font-weight: 800; color: var(--slate-900);
}
.stat-card .label { font-size: 0.75rem; color: #64748b; font-weight: 500; margin-top: 0.1rem; }
.stat-card.blue .value { color: var(--blue); }
.stat-card.teal .value { color: #0d9488; }
.stat-card.violet .value { color: #7c3aed; }

/* ── Cards ─────────────────────────────────────────────────── */
.search-card {
    background: var(--card); border: 1px solid var(--border);
    border-radius: clamp(14px, 2vw, 20px);
    padding: clamp(1rem, 3vw, 1.5rem);
    box-shadow: var(--shadow); margin-bottom: 1.5rem;
}
.search-label {
    font-size: 0.75rem; font-weight: 700; color: #64748b;
    text-transform: uppercase; letter-spacing: 0.07em; margin-bottom: 0.65rem;
}
.section-title {
    font-size: clamp(0.9rem, 2vw, 1rem); font-weight: 700;
    color: var(--slate-900); margin: 0 0 0.85rem;
}
.paper-card {
    background: var(--card); border: 1px solid var(--border);
    border-left: 4px solid var(--blue); border-radius: var(--radius);
    padding: clamp(0.85rem, 2vw, 1.1rem) clamp(1rem, 2.5vw, 1.35rem);
    margin-bottom: 0.65rem;
    display: flex; align-items: flex-start; gap: 12px;
    transition: box-shadow 0.15s ease;
    overflow: hidden; word-break: break-word;
}
.paper-card:hover { box-shadow: var(--shadow); border-left-color: #0ea5e9; }
.paper-icon {
    width: 40px; height: 40px; flex-shrink: 0;
    background: linear-gradient(135deg, #eff6ff, #dbeafe);
    border-radius: 11px;
    display: flex; align-items: center; justify-content: center; font-size: 1.1rem;
}
.paper-name { font-weight: 700; color: var(--slate-900); font-size: 0.92rem; }
.paper-meta { font-size: 0.75rem; color: #64748b; margin-top: 4px; display: flex; flex-wrap: wrap; gap: 5px; }
.paper-meta span {
    background: #f1f5f9; padding: 2px 8px; border-radius: 6px; font-weight: 500;
    white-space: nowrap;
}

/* ── Empty state ───────────────────────────────────────────── */
.empty-state {
    text-align: center; padding: clamp(2rem, 5vw, 3rem) clamp(1rem, 3vw, 2rem);
    background: var(--card); border: 2px dashed #cbd5e1;
    border-radius: clamp(14px, 2vw, 20px); color: #64748b;
}
.empty-state .icon { font-size: clamp(2rem, 5vw, 3rem); margin-bottom: 0.6rem; opacity: 0.65; }
.empty-state h3 { color: #334155; font-weight: 700; margin: 0 0 0.4rem; font-size: 1.05rem; }
.empty-state p { margin: 0; font-size: 0.88rem; line-height: 1.55; }

/* ── About ─────────────────────────────────────────────────── */
.info-card {
    background: var(--card); border: 1px solid var(--border);
    border-radius: clamp(14px, 2vw, 20px);
    padding: clamp(1.25rem, 3vw, 1.75rem);
    margin-bottom: 1rem; box-shadow: 0 2px 12px rgba(15,23,42,0.04);
}
.info-card h2 {
    font-size: clamp(1rem, 2.5vw, 1.15rem); font-weight: 700;
    color: var(--slate-900); margin: 0 0 0.85rem;
}
.info-card p { color: var(--slate-600); line-height: 1.75; margin: 0; font-size: 0.92rem; }
.hl-blue { color: var(--blue); font-weight: 600; }
.hl-teal { color: #0d9488; font-weight: 600; }
.tech-bar {
    margin-top: 1rem; padding-top: 1rem;
    border-top: 1px solid var(--border); font-size: 0.85rem; color: #64748b;
}
.step-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: clamp(8px, 1.5vw, 12px);
}
.step-card {
    border-radius: 12px; padding: clamp(0.75rem, 2vw, 1.1rem) 0.5rem;
    text-align: center; border: 1px solid;
    transition: transform 0.15s ease;
}
.step-card:hover { transform: translateY(-2px); }
.step-card .si { font-size: clamp(1.3rem, 3vw, 1.75rem); }
.step-card .st { font-weight: 700; font-size: 0.82rem; margin: 0.35rem 0 0.05rem; color: var(--slate-900); }
.step-card .ss { font-size: 0.68rem; color: #64748b; }
.s-upload  { background:#eff6ff; border-color:#bfdbfe; }
.s-extract { background:#f0fdf4; border-color:#bbf7d0; }
.s-chunk   { background:#fff7ed; border-color:#fed7aa; }
.s-embed   { background:#fdf2f8; border-color:#fbcfe8; }
.s-store   { background:#f5f3ff; border-color:#ddd6fe; }
.s-retrieve{ background:#f0fdfa; border-color:#99f6e4; }
.s-generate{ background:#eff6ff; border-color:#bfdbfe; }
.s-answer  { background:#f0fdf4; border-color:#bbf7d0; }

/* ── Chat ──────────────────────────────────────────────────── */
.chat-panel {
    background: var(--card); border: 1px solid var(--border);
    border-radius: clamp(14px, 2vw, 20px);
    padding: clamp(1rem, 2.5vw, 1.5rem);
    min-height: 180px; box-shadow: 0 2px 12px rgba(15,23,42,0.04);
    margin-bottom: 0.75rem;
}
.chat-empty {
    color: #94a3b8; text-align: center;
    padding: clamp(1.5rem, 4vw, 2.5rem) 1rem;
    font-size: 0.9rem;
}
.toolbar-card {
    background: var(--card); border: 1px solid var(--border);
    border-radius: var(--radius); padding: 0.85rem 1rem;
    margin-bottom: 1rem;
}

/* ── Upload ────────────────────────────────────────────────── */
.upload-wrap {
    background: linear-gradient(135deg, #f8fafc, #eff6ff);
    border: 2px dashed #93c5fd;
    border-radius: clamp(14px, 2vw, 20px);
    padding: 0.35rem; margin-bottom: 1.25rem;
}
div[data-testid="stFileUploader"] { background: transparent !important; border: none !important; }
div[data-testid="stFileUploader"] section { padding: clamp(1.25rem, 3vw, 2rem) !important; }

/* ── Buttons & inputs ──────────────────────────────────────── */
.stButton > button {
    border-radius: 11px !important;
    font-weight: 600 !important;
    transition: all 0.15s ease !important;
    white-space: normal !important;
    word-break: break-word !important;
}
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, var(--blue), var(--blue-dark)) !important;
    border: none !important;
    box-shadow: 0 4px 14px rgba(37, 99, 235, 0.3) !important;
}
.stButton > button[kind="primary"]:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 18px rgba(37, 99, 235, 0.4) !important;
}
.stTextInput > div > div > input,
.stSelectbox > div > div,
[data-testid="stChatInput"] textarea {
    border-radius: 11px !important;
    border-color: var(--border) !important;
    font-size: 0.9rem !important;
}
.stTextInput > div > div > input:focus {
    border-color: var(--blue) !important;
    box-shadow: 0 0 0 3px rgba(37,99,235,0.1) !important;
}
[data-testid="stAlert"] { border-radius: 11px !important; }
[data-testid="stChatMessage"] {
    border-radius: 14px !important;
    border: 1px solid var(--border) !important;
    margin-bottom: 0.65rem !important;
}
.streamlit-expanderHeader { border-radius: 11px !important; font-weight: 600 !important; }

.citation-tag {
    display: inline-block; background: #eff6ff; color: var(--blue-dark);
    padding: 3px 10px; border-radius: 8px;
    font-size: 0.78rem; font-weight: 600; margin: 3px 4px 3px 0;
}

/* ── RESPONSIVE ──────────────────────────────────────────────── */

/* Tablet */
@media (max-width: 1024px) {
    :root { --sidebar-w: 240px; }
    section[data-testid="stMain"] .block-container {
        padding-left: 1.5rem !important;
        padding-right: 1.5rem !important;
    }
    .step-grid { grid-template-columns: repeat(4, 1fr); }
}

/* Small tablet / large phone */
@media (max-width: 768px) {
    :root { --sidebar-w: 220px; }
    .stat-row { grid-template-columns: repeat(3, 1fr); }
    .step-grid { grid-template-columns: repeat(2, 1fr); }
    section[data-testid="stMain"] .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }
    /* Stack streamlit columns */
    [data-testid="stHorizontalBlock"] {
        flex-wrap: wrap !important;
        gap: 0.5rem !important;
    }
    [data-testid="stHorizontalBlock"] > [data-testid="column"] {
        min-width: calc(50% - 0.5rem) !important;
        flex: 1 1 calc(50% - 0.5rem) !important;
    }
    .search-row [data-testid="column"]:first-child {
        min-width: 100% !important; flex: 1 1 100% !important;
    }
    .search-row [data-testid="column"]:last-child {
        min-width: 100% !important; flex: 1 1 100% !important;
    }
    .toolbar-row [data-testid="column"] {
        min-width: 100% !important; flex: 1 1 100% !important;
    }
}

/* Mobile */
@media (max-width: 640px) {
    section[data-testid="stMain"] .block-container {
        padding-left: 0.85rem !important;
        padding-right: 0.85rem !important;
    }
    .stat-row { grid-template-columns: 1fr !important; }
    .step-grid { grid-template-columns: repeat(2, 1fr) !important; }
    [data-testid="stHorizontalBlock"] > [data-testid="column"] {
        min-width: 100% !important;
        flex: 1 1 100% !important;
    }
    .paper-card { flex-direction: row; align-items: center; }
    .hero-banner { margin-bottom: 1.25rem; }
    [data-testid="stSidebar"] [data-testid="stRadio"] label {
        padding: 0.55rem 0.75rem !important;
        font-size: 0.82rem !important;
    }
}

/* Very small phones */
@media (max-width: 380px) {
    .step-grid { grid-template-columns: 1fr 1fr !important; }
    .hero-badges { gap: 5px; }
    .badge { font-size: 0.62rem; padding: 0.25rem 0.55rem; }
}
"""

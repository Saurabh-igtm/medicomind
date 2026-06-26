


> Offline AI-Powered Medical Research Assistant using Retrieval-Augmented Generation (RAG)
## 📖 Overview

**MedicoMind** is an offline AI-powered Medical Research Assistant that allows users to upload medical research papers in PDF format and ask questions using natural language.

The application uses a **Retrieval-Augmented Generation (RAG)** pipeline to retrieve relevant information from uploaded documents and generate accurate, context-aware answers using a locally running Large Language Model (LLM).

Since everything runs locally with Ollama, no external APIs or cloud services are required, ensuring complete privacy and data security.

---

# ✨ Features (Version 1.0)

- 📄 Upload medical research paper PDFs
- 📚 Extract text using PyMuPDF
- ✂️ Intelligent text chunking
- 🧠 Generate embeddings using `nomic-embed-text`
- 💾 Store vectors locally with ChromaDB
- 🔍 Semantic document retrieval
- 💬 Ask questions in natural language
- 🤖 Generate answers using `llama3.2:1b`
- 🔒 Fully Offline (No Internet Required)
- 🖥️ Streamlit Web Interface

---

# 🏗️ System Architecture

```text
                Medical PDF
                     │
                     ▼
            PDF Text Extraction
                (PyMuPDF)
                     │
                     ▼
        Recursive Text Chunking
                     │
                     ▼
     Embedding Generation (Ollama)
      nomic-embed-text Model
                     │
                     ▼
         ChromaDB Vector Database
                     │
                     ▼
              User Question
                     │
                     ▼
          Semantic Similarity Search
                     │
                     ▼
        Retrieved Context Chunks
                     │
                     ▼
      Local LLM (llama3.2:1b via Ollama)
                     │
                     ▼
          Context-Aware AI Response
```

---

# 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| Programming Language | Python |
| Frontend | Streamlit |
| PDF Processing | PyMuPDF |
| Text Chunking | LangChain |
| Embeddings | nomic-embed-text |
| Vector Database | ChromaDB |
| Local LLM Runtime | Ollama |
| Language Model | llama3.2:1b |

---

# 📂 Project Structure

```text
MedicoMind/
│
├── .venv/                      # Python virtual environment
│
├── chroma_db/                  # Local ChromaDB vector database
│
├── data/                       # Application data
│
├── papers/                     # Sample research papers
│   └── sample.pdf
│
├── uploads/                    # User uploaded PDFs
│
├── app.py                      # Command-line entry point
├── ui.py                       # Streamlit web application
├── ui_styles.py                # Custom Streamlit styles
│
├── pdf_parser.py               # Extract text from PDF files
├── chunking.py                 # Split documents into chunks
├── vector_store.py             # ChromaDB indexing & retrieval
├── ingestion.py                # PDF ingestion pipeline
├── library.py                  # Manage uploaded document library
├── prompt_builder.py           # Build prompts for the LLM
├── generator.py                # Generate answers using Ollama
├── pipeline.py                 # Complete RAG workflow
│
├── requirements.txt            # Python dependencies
├── sample.pdf                  # Example PDF
│
├── README.md                   # Project documentation
└── LICENSE                     # MIT License
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/medicomind.git

cd medicomind
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🤖 Install Ollama

Download and install Ollama.

Then pull the required models:

```bash
ollama pull llama3.2:1b

ollama pull nomic-embed-text
```

---

# ▶️ Run the Application

Start the Streamlit server:

```bash
streamlit run ui.py
```

Open your browser:

```
http://localhost:8501
```

---

# 📋 Workflow

1. Upload a medical research paper (PDF).
2. Extract text using PyMuPDF.
3. Split text into semantic chunks.
4. Generate embeddings with Ollama.
5. Store vectors in ChromaDB.
6. Ask a medical question.
7. Retrieve the most relevant document chunks.
8. Generate a context-aware answer using the local LLM.

---

# 📸 Screenshots

## 🏠 Home

<img width="1004" height="1000" alt="image" src="https://github.com/user-attachments/assets/121685c0-1d6e-447e-8bae-f33c2556ac54" />



---

## 📄 Upload PDF

<img width="1287" height="1031" alt="image" src="https://github.com/user-attachments/assets/b14fb53f-9ae4-4858-a6e7-af6db29e7505" />


---

## 💬 Chat Interface

<img width="1601" height="1031" alt="image" src="https://github.com/user-attachments/assets/bd4242ac-956c-43b2-88b5-e4513d90efd3" />


---

# 🚀 Roadmap

## Version 1.1

- ✅ Source citations
- ✅ Page references

---

## Version 1.2

- ✅ Multiple PDF support
- ✅ Research paper library

---

## Version 1.3

- ✅ Chat history
- ✅ Persistent vector indexing

---

## Version 2.0

- 📑 Research paper summarization
- 📊 Literature review generation
- 🔬 Compare multiple research papers

---

## Version 3.0

- 🏥 Medical Research Assistant
- 🎙️ Voice interaction
- 📈 Knowledge Graph
- 🤖 AI Research Agents
- 💻 NVIDIA Jetson deployment
- 🔐 Role-based authentication

---

# 📦 Requirements

- Python 3.10+
- Ollama
- Streamlit
- ChromaDB
- PyMuPDF

---

# 📄 License

This project is licensed under the MIT License.

---

# 🙏 Acknowledgements

Special thanks to the open-source community and the developers of:

- Ollama
- LangChain
- ChromaDB
- Streamlit
- PyMuPDF

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

Your support helps improve the project and encourages future development.

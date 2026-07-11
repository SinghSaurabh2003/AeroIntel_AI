# ✈️ AeroIntel AI
### Intelligent Aviation Investigation Report Analysis using RAG, LangGraph & Knowledge Graph

![Python](https://img.shields.io/badge/Python-3.10-blue)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![LangGraph](https://img.shields.io/badge/LangGraph-Agentic-orange)
![FAISS](https://img.shields.io/badge/VectorDB-FAISS-red)
![Neo4j](https://img.shields.io/badge/KnowledgeGraph-Neo4j-blue)
![Groq](https://img.shields.io/badge/LLM-Groq-purple)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)

---

## 📖 Overview

**AeroIntel AI** is an AI-powered Document Intelligence platform designed for aviation investigation reports.

The system combines:

- 📚 Retrieval-Augmented Generation (RAG)
- 🧠 LangGraph Agentic Workflow
- 🔎 Hybrid Retrieval
- 🗂 Metadata Search
- 🕸 Neo4j Knowledge Graph
- 📄 PDF Upload & Incremental Indexing

to provide accurate, source-grounded answers from aviation investigation documents.

---

# 🚀 Features

### ✅ Retrieval-Augmented Generation (RAG)

- FAISS Vector Database
- SentenceTransformer Embeddings
- MMR Retrieval
- Source Grounding
- Page-level Citations

---

### ✅ LangGraph Workflow

Agentic routing automatically selects the best retrieval strategy:

```
                User Query
                     │
                     ▼
              LangGraph Router
         ┌────────┼────────┐
         ▼        ▼        ▼
   Metadata   Knowledge   Vector
    Search      Graph     Search
```

---

### ✅ Dual Search Modes

Users can search:

- Aviation Database
- Uploaded Documents
- Both

---

### ✅ Upload New PDFs

Upload any aviation report through Streamlit.

The system:

- Saves PDF
- Splits into chunks
- Generates embeddings
- Updates FAISS incrementally

No rebuilding required.

---

### ✅ Metadata Search

Fast structured lookup using

```
data/metadata/reports.json
```

Supports queries such as

- Report ID
- Airline
- Aircraft
- PDF Name

---

### ✅ Knowledge Graph

Neo4j stores structured aviation relationships.

Example:

```
Report
   │
   ├── Airline
   ├── Aircraft
   ├── Keywords
   └── Registration
```

Supports relationship-based queries.

---

# 🏗 Project Architecture

```
                     User
                      │
                      ▼
                Streamlit UI
                      │
                      ▼
                LangGraph Router
        ┌─────────┼───────────┐
        ▼         ▼           ▼
 Metadata      Neo4j KG     FAISS
 Search                     Search
        │                     │
        └──────────┬──────────┘
                   ▼
              Groq LLM
                   ▼
               Final Answer
```

---

# 📂 Project Structure

```
AeroIntel_AI
│
├── app/
│   ├── langgraph/
│   ├── rag/
│   ├── retrieval/
│   ├── upload/
│   ├── knowledge_graph/
│   ├── llm/
│   └── ui/
│
├── data/
│   ├── raw/
│   ├── metadata/
│   ├── uploaded/
│   └── vector_store/
│
├── build_graph.py
├── build_index.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

Clone repository

```bash
git clone https://github.com/yourusername/AeroIntel_AI.git

cd AeroIntel_AI
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a file named

```
.env
```

Example

```env
GROQ_API_KEY=your_groq_api_key
```

> **Note:** The `.env` file is **not included** in the repository. Use your own Groq API key.

---

# ▶ Running the Application

```bash
streamlit run app/ui/streamlit_app.py
```

---

# 📄 Adding New Aviation Reports

Place new investigation reports inside

```
data/raw/
```

Then rebuild the aviation search index

```bash
python build_index.py
```

This recreates the FAISS index using all reports inside `data/raw`.

---

# 📤 Uploading Custom PDFs

Users can upload PDFs directly through the Streamlit interface.

Uploaded reports are:

- Stored locally
- Chunked
- Embedded
- Indexed incrementally

No manual indexing is required.

---

# 🗂 Updating Metadata

Metadata is maintained manually.

Update

```
data/metadata/reports.json
```

Example

```json
{
    "report_id":"AIR2504",
    "title":"In-Flight Separation of Left Mid Exit Door Plug",
    "airline":"Alaska Airlines",
    "aircraft":"Boeing 737-9",
    "registration":"N704AL",
    "keywords":[
        "door plug",
        "rapid depressurization"
    ],
    "pdf":"AIR2504.pdf"
}
```

---

# 🕸 Updating Knowledge Graph

After modifying `reports.json`, rebuild the Neo4j graph

```bash
python build_graph.py
```

---

# ⚙ Neo4j Configuration

Currently Neo4j connection details are configured manually inside

```
app/knowledge_graph/neo4j_service.py
```

Update the following values

```python
URI = "bolt://127.0.0.1:7687"

USERNAME = "neo4j"

PASSWORD = "your_password"
```

After configuring Neo4j, execute

```bash
python build_graph.py
```

---

# 🧠 Technologies Used

- Python
- LangChain
- LangGraph
- FAISS
- Neo4j
- Sentence Transformers
- HuggingFace Embeddings
- Groq API
- Streamlit
- PyMuPDF

---

# 📌 Current Limitations

- Metadata is manually maintained.
- Knowledge Graph requires manual graph rebuild.
- Neo4j credentials are configured manually.
- Follow-up conversational memory is not implemented.
- Knowledge Graph currently supports limited relationship queries.

---

# 🚀 Future Improvements

- Automatic metadata extraction using LLMs
- Neo4j configuration through `.env`
- Conversational memory
- GraphRAG integration
- Multi-document comparison
- Automatic report downloader
- Metadata management interface

---

# 👨‍💻 Author

**Saurabh Singh Chhonkar**

M.Tech Computer Science & Engineering

Motilal Nehru National Institute of Technology (MNNIT), Prayagraj

---

⭐ If you found this project useful, consider giving it a Star!

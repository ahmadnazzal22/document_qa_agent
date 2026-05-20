
# 📄 DocAI Agent 🐍
### Intelligent Document Question Answering System powered by Groq + LangChain

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Dark_UI-red.svg)
![LLM](https://img.shields.io/badge/Groq-Accelerated-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 🚀 Overview

DocAI Agent is a **smart document assistant** that allows users to upload files and ask questions in natural language.

It reads, understands, and extracts answers from documents using **AI-powered semantic search + LLM reasoning**.

> ⚡ Built for speed.  
> 🧠 Designed for intelligence.  
> 🎨 Styled with a dark developer UI.

---

## 🧠 How It Works (AI Pipeline)

```python
# 1. Load Document
docs = load_pdf("file.pdf")

# 2. Split into chunks
chunks = text_splitter.split_documents(docs)

# 3. Create embeddings
vectors = embedding_model.embed(chunks)

# 4. Store in vector DB
db = FAISS.from_documents(chunks, vectors)

# 5. Ask question
query = "What is this document about?"

# 6. Retrieve context
context = db.similarity_search(query)

# 7. Generate answer (Groq LLM)
answer = llm.generate(context + query)
````

---

## ✨ Features

* ⚡ Ultra-fast responses using **Groq API**
* 🧠 Context-aware semantic search
* 📄 Supports PDF & TXT files
* 🔍 Intelligent chunk retrieval system
* 🎨 Dark-mode Streamlit UI (developer style)
* 📊 Visual breakdown of document processing
* 🔐 Safe environment variable handling

---

## 🏗️ Tech Stack

```text
🐍 Python 3.10+
🧠 LangChain
⚡ Groq Cloud API
📦 FAISS / ChromaDB
🎨 Streamlit (Dark UI)
```

---

## 📁 Project Structure

```bash
document-qa-agent/
│
├── app.py               # Main Streamlit app
├── chains/              # LLM chains (LangChain logic)
├── utils/               # Helpers (loaders, splitters)
├── embeddings/         # Vector DB handling
├── data/               # Sample documents
├── .env                # API keys (hidden 🔐)
└── requirements.txt
```

---

## ⚙️ Setup Guide

### 1️⃣ Clone Repo

```bash
git clone https://github.com/your-username/docai-agent.git
cd docai-agent
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Add API Key 🔐

```env
GROQ_API_KEY=your_key_here
```

### 4️⃣ Run App 🚀

```bash
streamlit run app.py
```

---

## 🛡️ Security Notes

* 🔐 API keys are stored in `.env`
* 🚫 `.env` is excluded from Git tracking
* 🧠 No user data is permanently stored
* ⚡ Requests handled in real-time only

---

## 🎯 Use Cases

* 📚 Research paper analysis
* ⚖️ Legal document Q&A
* 🏢 Company knowledge base
* 🎓 Student study assistant
* 📊 Data extraction from reports

---

## 🎨 UI Preview

> A dark, minimal, hacker-style interface built for focus and productivity.

```
┌──────────────────────────────┐
│  📄 Upload Document          │
│  💬 Ask Question             │
│  ⚡ Get Instant Answer        │
└──────────────────────────────┘
```

---

## 🤝 Contributing

```python
if you_like_project:
    fork_repo()
    create_branch()
    improve_code()
    submit_pull_request()
```

---

## 🧠 Final Note

> “This project is not just a tool — it's an AI experience.”

---

## 📜 License

MIT License © 2026

```

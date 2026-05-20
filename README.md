

````markdown id="a9p2k1"
# 📄 DocAI Agent 🐍
### Intelligent Document Question Answering System powered by Groq + LangChain

---

🚀 **Developed by:** **Ahmed Nazzal**  
🧠 **Role:** AI Engineer & Python Developer  
🌐 **Live Demo:** https://docai-agent.streamlit.app  
📦 **GitHub Repo:** https://github.com/your-username/docai-agent  

---

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Dark_UI-black.svg)
![Groq](https://img.shields.io/badge/Groq-LLM-orange.svg)
![LangChain](https://img.shields.io/badge/LangChain-Orchestration-green.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

---

## 🧠 Overview

**DocAI Agent** is an AI-powered document assistant that allows users to upload documents and ask natural language questions to instantly extract accurate answers.

Built with a focus on:
- ⚡ Speed (Groq inference)
- 🧠 Intelligence (LangChain reasoning)
- 🎨 UX (Dark-themed Streamlit interface)

---

## 🚀 Features

- ⚡ Ultra-fast AI responses using Groq API  
- 🧠 Semantic document understanding  
- 📄 PDF / TXT document support  
- 🔍 Context-aware retrieval system  
- 🎨 Clean Dark UI for developers  
- 📊 Transparent chunking & processing view  
- 🔐 Secure API key handling  

---

## 🧠 AI Architecture

```python id="ai_flow"
# Load document
docs = load_document(file)

# Split into chunks
chunks = text_splitter.split(docs)

# Create embeddings
vectors = embed_model.encode(chunks)

# Store in vector DB
db = FAISS.from_texts(chunks, vectors)

# User question
query = "What is this document about?"

# Retrieve context
context = db.search(query)

# Generate answer
response = groq_llm.generate(context + query)
````

---

## 🏗️ Tech Stack

```text id="stack"
🐍 Python 3.10+
🧠 LangChain
⚡ Groq API
📦 FAISS / ChromaDB
🎨 Streamlit (Dark UI)
```

---

## 📁 Project Structure

```bash id="structure"
document-qa-agent/
│
├── app.py
├── chains/
├── utils/
├── embeddings/
├── data/
├── .env
└── requirements.txt
```

---

## ⚙️ Setup Instructions

```bash id="setup1"
git clone https://github.com/your-username/docai-agent.git
cd docai-agent
pip install -r requirements.txt
```

```env id="env1"
GROQ_API_KEY=your_api_key_here
```

```bash id="run1"
streamlit run app.py
```

---

## 🌐 Live Demo

👉 **Try it here:** [https://docai-agent.streamlit.app](https://docai-agent.streamlit.app)

---

## 🛡️ Security

* 🔐 API keys stored securely in `.env`
* 🚫 `.env` excluded from version control
* ⚡ No persistent user data storage
* 🧠 Real-time processing only

---

## 🎯 Use Cases

* 📚 Academic research assistant
* ⚖️ Legal document analysis
* 🏢 Company knowledge base
* 🎓 Student study companion
* 📊 Report summarization tool

---

## 👨‍💻 About the Developer

```text id="dev"
Ahmed Nazzal
AI Engineer | Python Developer | LLM Enthusiast

Passionate about building intelligent systems using:
LangChain • LLMs • Vector Databases • AI Agents
```

---

## 🤝 Contributing

```python id="contrib"
if interested:
    fork_repo()
    create_branch()
    improve_project()
    submit_PR()
```

---

## 📜 License

MIT License © 2026 — Ahmed Nazzal
 شخصي قوي؟**
```

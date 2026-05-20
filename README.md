# 📄 DocAI Agent

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?style=for-the-badge\&logo=streamlit\&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-LLM-FF6B00?style=for-the-badge)
![LangChain](https://img.shields.io/badge/LangChain-AI-2E8B57?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

## 🧠 AI-Powered Document Q&A System

> Upload your documents (PDF/TXT) and ask questions — get instant intelligent answers using LLM + semantic search.

🚀 **Built by:** Ahmed Nazzal
⚡ **Powered by:** Groq + LangChain + Vector Search

---

## 🌐 Tech Stack (Language & Tools Cards)

<div align="center">

### 👨‍💻 Core Languages

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge\&logo=python)

---

### ⚙️ Backend & AI

![LangChain](https://img.shields.io/badge/LangChain-Orchestration-000000?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-Inference-FF6B00?style=for-the-badge)

---

### 🎨 UI Layer

![Streamlit](https://img.shields.io/badge/Streamlit-Dark_UI-FF4B4B?style=for-the-badge\&logo=streamlit)

---

### 🧠 Vector DB

![FAISS](https://img.shields.io/badge/FAISS-Vector_Search-1E90FF?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Embeddings-8A2BE2?style=for-the-badge)

</div>

---

## ✨ Features

🔥 Ultra-fast AI responses (Groq optimized)
🧠 Smart semantic retrieval (vector embeddings)
📄 PDF + TXT document support
🎨 Modern dark Streamlit UI
🔍 Transparent AI reasoning pipeline
⚡ Chunk-based document understanding

---

## 📁 Project Structure

```bash
docai-agent/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
│
├── chains/
│   ├── __init__.py
│   └── qa_chain.py
│
├── utils/
│   ├── __init__.py
│   ├── loader.py
│   └── splitter.py
│
├── embeddings/
│   ├── __init__.py
│   └── vector_store.py
│
├── templates/
│   └── index.html
│
├── data/
│   └── sample.pdf
│
├── assets/
│   ├── logo.png
│   └── style.css
│
└── .gitignore
```

---

## 🚀 Installation

```bash
git clone https://github.com/your-username/docai-agent.git
cd docai-agent

python -m venv venv
source venv/bin/activate   # or Windows venv\Scripts\activate

pip install -r requirements.txt
```

---

## 🔑 Environment

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run App

```bash
streamlit run app.py
```

---

## 🧠 AI Pipeline

📄 Document Upload
⬇️
✂️ Chunking (Text Splitter)
⬇️
🧠 Embeddings (Vector Store)
⬇️
🔍 Semantic Search
⬇️
⚡ Groq LLM Answer
⬇️
💬 Final Response

---

## 🧪 Example

**Q:** What is this document about?
**A:** It describes artificial intelligence systems and their real-world applications...

---

## 🚀 Future Upgrades

* 💬 Chat memory system
* 📚 Multi-document Q&A
* 🌍 Multi-language support
* 📊 Analytics dashboard
* ☁️ Cloud deployment
* 🔐 Authentication system

---

## 🐳 Docker

```dockerfile
FROM python:3.11

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---

## 👨‍💻 Developer

<div align="center">

**Ahmed Nazzal**
🐍 Python Developer | 🧠 AI Engineer | ⚡ LLM Builder

</div>

---

## ⭐ Support

⭐ Star the repo
🍴 Fork it
📢 Share it

---

<div align="center">

🔥 Built with Python + LangChain + Groq 🔥

</div>

---

# 📄 DocAI — AI-Powered Document Q&A

### Ask Questions. Retrieve Information. Get AI-Powered Answers.

DocAI is an AI-powered application that allows users to upload PDF and TXT documents and ask questions about their content using semantic search and Large Language Models (LLMs).

Built with Python, Streamlit, LangChain, and Groq, the application processes documents, retrieves relevant information, and generates contextual answers based on the uploaded content.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📄 Document Upload | Upload PDF and TXT documents |
| 💬 Question Answering | Ask natural-language questions about document content |
| 🧠 Semantic Search | Retrieve relevant content based on meaning |
| ✂️ Text Chunking | Split documents into smaller sections for processing |
| 🔍 Context Retrieval | Find relevant document sections for each question |
| ⚡ LLM Integration | Generate answers using the Groq API |
| 🎨 Interactive Interface | Use a simple Streamlit-based interface |

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.10+ | Core programming language |
| Streamlit | User interface |
| LangChain | Document processing and application workflow |
| Groq API | Language model inference |
| FAISS / ChromaDB | Vector storage and semantic retrieval, depending on implementation |

> Make sure the listed vector database matches the actual implementation. Keep both FAISS and ChromaDB only if the project genuinely uses both.

---

## 🧠 How It Works

DocAI follows a Retrieval-Augmented Generation (RAG) workflow to answer questions using information from uploaded documents.

```text
       Document Upload
              |
              v
    Document Text Extraction
              |
              v
         Text Chunking
              |
              v
      Generate Embeddings
              |
              v
       Vector Storage
              |
              v
      Semantic Retrieval
              |
              v
     Relevant Context
              |
              v
     Groq Language Model
              |
              v
      Generate Answer
              |
              v
       Display Result
```

The retrieval process helps the language model generate answers using relevant information from the uploaded documents.

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ahmadnazzal22/document_qa_agent.git
cd document_qa_agent
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

**Windows:**

```powershell
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your API key from the [Groq Console](https://console.groq.com/).

**Security reminder:**
- Never share your API key publicly.
- Do not upload your `.env` file to GitHub.
- Add `.env` to your `.gitignore`.
- Consider providing a `.env.example` file for other developers.

### 5. Run the Application

```bash
streamlit run app.py
```

Streamlit will display a local URL in the terminal. Open it in your browser to access DocAI.

---

## 🧪 Example Usage

1. Start the application.
2. Upload

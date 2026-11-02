# 📄 DocAI — AI-Powered Document Q&A

An AI-powered application that allows users to upload PDF and TXT documents and ask questions about their content using language models and semantic search.

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-LLM-FF6B00?style=for-the-badge)
![LangChain](https://img.shields.io/badge/LangChain-AI-1C3C3C?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

## ✨ Features

- 📄 **Document Upload** — Supports PDF and TXT documents.
- 💬 **Question Answering** — Ask questions about uploaded document content.
- 🧠 **Semantic Search** — Retrieves relevant information based on meaning.
- ✂️ **Text Chunking** — Splits documents into smaller sections for processing.
- ⚡ **LLM Integration** — Uses the Groq API to generate answers.
- 🎨 **Streamlit Interface** — Provides a user-friendly application interface.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.10+ | Core programming language |
| Streamlit | User interface |
| LangChain | Document processing and application workflow |
| Groq API | Language model inference |
| FAISS / ChromaDB | Vector search, depending on the configured implementation |

> Keep FAISS and ChromaDB in this list only if both are actually implemented in your code. Otherwise, list only the vector store you use.

---

## 🧠 How It Works

```text
       Document Upload
              ↓
      Document Text Extraction
              ↓
         Text Chunking
              ↓
       Generate Embeddings
              ↓
       Store Vector Data
              ↓
       Semantic Retrieval
              ↓
        Groq Language Model
              ↓
       Generate an Answer
              ↓
        Display the Result
```

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

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

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

Keep your API key private and do not upload your `.env` file.

### 5. Run the Application

```bash
streamlit run app.py
```

Streamlit will provide a local URL. Open that URL in your browser to use the application.

---

## 🧪 Example Usage

1. Launch the application.
2. Upload a PDF or TXT document.
3. Wait for the document to be processed.
4. Enter a question about its content.
5. Review the generated answer.

**Example question:**

> What is this document about?

**Example answer:**

> The answer is generated using information retrieved from the uploaded document.

---

## 🚀 Future Improvements

Potential improvements for future versions include:

- 💬 Conversation memory.
- 📚 Support for multiple documents.
- 🌍 Improved multilingual support.
- 📊 Usage and retrieval analytics.
- ☁️ Cloud deployment.
- 🔐 User authentication.

---

## 👨‍💻 Developer

**Ahmad Nazzal**

Python Developer | Exploring AI & Automation

- GitHub: [ahmadnazzal22](https://github.com/ahmadnazzal22)
- Project: [DocAI Agent](https://github.com/ahmadnazzal22/document_qa_agent)

---

## 📄 License

This project is licensed under the MIT License.

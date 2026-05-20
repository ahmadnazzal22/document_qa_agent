from flask import Flask, request, jsonify, render_template
from groq import Groq
from utils import extract_text, split_chunks, build_index, search
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

chunks = []
index = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    global chunks, index
    file = request.files['pdf']
    text = extract_text(file)
    chunks = split_chunks(text)
    index, _ = build_index(chunks)
    return jsonify({"message": f"✅ تم رفع الملف — {len(chunks)} chunk"})

@app.route('/ask', methods=['POST'])
def ask():
    global chunks, index
    if not chunks:
        return jsonify({"answer": "⚠️ ارفع PDF أول"})
    
    data = request.json
    question = data.get('question', '')
    context = search(question, chunks, index)
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
    {
        "role": "system",
        "content": """أنت مساعد ذكي متخصص في تحليل المستندات.
أجب على السؤال بناءً على النص المرفق فقط.
قواعد الإجابة:
- اكتب بشكل واضح ومنظم
- استخدم نقاط أو أرقام إذا كان الجواب يحتوي معلومات متعددة
- لا تستخدم رموز غريبة أو HTML
- أجب بنفس لغة السؤال (عربي أو إنجليزي)
- إذا المعلومة مش موجودة في النص قل ذلك بوضوح

النص:
""" + context
    },
    {"role": "user", "content": question}
] 
        
    )
    
    answer = response.choices[0].message.content
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
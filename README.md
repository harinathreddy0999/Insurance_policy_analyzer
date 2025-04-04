# 🚀 Insurance Policy Analyzer

A powerful AI-driven tool to **analyze insurance policy documents** and extract meaningful insights.

---

## 🧠 Key Features

✅ Upload and process **insurance policy documents** in **PDF**, **JPG**, or **PNG** formats  
✅ Choose the **insurance policy type** (Auto, Health, Home, etc.)  
✅ Perform **OCR** to extract text from images and scanned PDFs  
✅ Use **NLP** to extract and structure policy data  
✅ **Validate** extracted policy data for consistency and completeness

---

## 🧰 Tech Stack & Dependencies

- 🔥 **Flask** — Backend API
- 🖼️ **Pillow** — Image processing
- 📄 **PyPDF2** — PDF parsing
- 🔐 **python-dotenv** — Environment variable management
- 🧠 **pytesseract** — OCR (Optical Character Recognition)
- 🧬 **spaCy** — NLP information extraction
- 🌐 **flask-cors** — CORS support for API
- ⚡ **Streamlit** — Interactive frontend for document analysis

---

## ⚙️ Installation Guide

### 1️⃣ Clone the repository
```bash
git clone <repository_url>
```

### 2️⃣ Navigate into the project directory
```bash
cd insurance_policy_analyzer
```

### 3️⃣ Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4️⃣ Install all dependencies
```bash
pip install -r requirements.txt
```

---

## 🚦 How to Use

### 1. Launch the app
```bash
streamlit run streamlit_app.py
```

### 2. Open your browser to view the app  
Usually: [http://localhost:8501](http://localhost:8501)

### 3. Upload a policy document  
📄 PDF or 📸 Image (JPG/PNG)

### 4. Select policy type  
(e.g., Auto, Health, Life, Home)

### 5. View the analysis  
✔ Extracted text  
✔ Key information  
✔ Validated results

---

## 💡 Tip

You can enhance this with:
- LangChain or LLM integration for smarter data extraction.
- Voice input (via Whisper or SpeechRecognition).
- Saving analysis to a database or downloadable PDF report.


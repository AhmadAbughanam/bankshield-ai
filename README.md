# 🛡️ BankShield AI

**BankShield AI** is a portfolio-grade, AI-powered cybersecurity and financial fraud monitoring tool built with Python, Flask, and `llama-cpp-python`. It analyzes access logs and transaction data for suspicious patterns, generates risk summaries using a local LLM (LLaMA 3), and visualizes behavioral trends.

---

## 🚀 Features

### 🧠 AI Insight Generation

- Uses a local LLaMA-3-based model to analyze risk flags
- Summarizes suspicious logins and transactions

### 🔍 Cybersecurity Access Log Monitor

- Detects:
  - Login during off-hours
  - Suspicious IPs
  - Brute-force-like activity
- Visualizes login hours via Plotly charts

### 💸 Financial Transaction Analyzer

- Flags:
  - High-amount transactions
  - Self-transfers
  - Off-hour or irregular timing
- AI-generated summaries and risk patterns

### 📤 Export & Reports

- Export flagged results as CSV
- View risk summaries inline
- Upload multiple datasets

---

## 🛠 Tech Stack

- **Backend:** Flask + Pandas
- **AI:** `llama-cpp-python` (LLaMA 3 GGUF local inference)
- **Visualization:** Plotly
- **Frontend:** Bootstrap 4 (simple HTML templates)

---

## 🗂 Directory Structure

bankshield-ai/
│
├── app/
│ ├── routes.py
│ ├── llm_engine.py
│ ├── log_utils.py
│ └── templates/
│ ├── home.html
│ ├── upload.html
│ ├── view_data.html
│ ├── upload_log.html
│ └── view_log.html
├── models/
│ └── Llama-3.2-3B-Instruct-Q4_0.gguf
├── static/
├── uploads/
├── requirements.txt
└── run.py

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/bankshield-ai.git
cd bankshield-ai
2. Create Virtual Environment
bash
Copy code
python -m venv venv
venv\Scripts\activate    # on Windows
pip install -r requirements.txt
3. Add Model
Download Llama-3.2-3B-Instruct-Q4_0.gguf from TheBloke on Hugging Face
Place it in the models/ folder.

4. Run the App
bash
Copy code
python run.py
Then go to: http://127.0.0.1:5000

📸 Screenshots
(Add screenshots of the transaction upload view, log analysis, AI summaries, and charts)

💡 Future Ideas
Dockerize the app for deployment

Add streamlit or mobile-friendly UI

Integrate anomaly detection models

Extend to real-time log processing

👤 Author
Ahmad (XZOTECHX)
LinkedIn • Portfolio • GitHub

📄 License
MIT License
```

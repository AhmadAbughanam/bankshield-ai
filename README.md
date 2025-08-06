
---

# 🛡️ **BankShield AI**  
**AI-Powered Cybersecurity & Financial Fraud Monitoring Tool**

BankShield AI is a portfolio-grade application built with **Python**, **Flask**, and **LLaMA 3** via `llama-cpp-python`. It analyzes access logs and transaction data to detect suspicious patterns, generate AI-driven risk summaries, and visualize behavioral trends.

---

## 🚀 **Key Features**

### 🧠 AI Insight Generation
- Local **LLaMA 3** model for risk analysis
- Summarizes suspicious logins and transactions
- Generates contextual risk narratives

### 🔍 Cybersecurity Access Log Monitor
- Detects:
  - ⏰ Off-hour logins
  - 🌐 Suspicious IP addresses
  - 🔐 Brute-force-like login attempts
- 📊 Visualizes login patterns with Plotly

### 💸 Financial Transaction Analyzer
- Flags:
  - 💰 High-value transactions
  - 🔁 Self-transfers
  - ⏱️ Irregular transaction timing
- 🧠 AI-generated summaries and behavioral patterns

### 📤 Export & Reporting
- 📁 Export flagged results as CSV
- 🧾 Inline risk summaries
- 📂 Upload multiple datasets for analysis

---

## 🛠️ Tech Stack

| Layer        | Technology                          |
|--------------|--------------------------------------|
| **Backend**  | Flask, Pandas                        |
| **AI Engine**| `llama-cpp-python` (LLaMA 3 GGUF)    |
| **Frontend** | Bootstrap 4, HTML Templates          |
| **Charts**   | Plotly                               |

---

## 📁 Project Structure

```
bankshield-ai/
│
├── app/
│   ├── routes.py
│   ├── llm_engine.py
│   ├── log_utils.py
│   └── templates/
│       ├── home.html
│       ├── upload.html
│       ├── view_data.html
│       ├── upload_log.html
│       └── view_log.html
├── models/
│   └── Llama-3.2-3B-Instruct-Q4_0.gguf
├── static/
├── uploads/
├── requirements.txt
└── run.py
```

---

## ⚙️ Setup Instructions

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/bankshield-ai.git
cd bankshield-ai
```

### 🧪 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate # macOS/Linux
pip install -r requirements.txt
```

### 📥 3. Add the Model

- Download `Llama-3.2-3B-Instruct-Q4_0.gguf` from [TheBloke on Hugging Face](https://huggingface.co/TheBloke)
- Place it in the `models/` directory

### ▶️ 4. Run the App

```bash
python run.py
```

- Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📸 Screenshots

> _Add screenshots of:_
- Transaction upload view
- Log analysis dashboard
- AI-generated summaries
- Plotly visualizations

---

## 💡 Future Enhancements

- 🐳 Dockerize for deployment
- 📱 Mobile-friendly UI or Streamlit integration
- 🧠 Integrate anomaly detection models
- 🔄 Real-time log processing

---

## 👤 Author

**Ahmad (XZOTECHX)**  
[LinkedIn](#) • [Portfolio](#) • [GitHub](#)

---

## 📄 License

This project is licensed under the **MIT License**.

---

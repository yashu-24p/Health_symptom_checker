# 🩺 Healthcare Symptom Checker

### 🎯 Objective
A simple AI-powered tool that takes user symptoms and suggests possible health conditions and next steps.  
⚠️ For educational purposes only — not a medical diagnosis.

---

## 🧰 Tech Stack
- *Language:* Python
- *Framework:* Flask
- *LLM API:* OpenAI GPT
- *Frontend:* HTML (optional)
- *Hosting:* Local / Render

---

## ⚙️ Setup Instructions


   git clone https://github.com/yashu-24p/Healthcare-Symptom-Checker.git
   cd Healthcare-Symptom-Checker
pip install -r requirements.txt
python app.py
POST http://127.0.0.1:5000/check
Body: {"symptoms": "fever, sore throat"}
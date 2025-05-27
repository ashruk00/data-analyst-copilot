# 🧠 LLM-Powered Data Analyst Copilot

A smart Streamlit app that lets you upload any CSV and ask data questions in plain English. It uses GPT to generate and run Python code on your data, returning results instantly — making data analysis accessible, fast, and powerful.

---

## 🚀 Features

- 📁 Upload CSV files
- 💬 Ask questions in plain English
- 🧠 GPT-3.5 generates Pandas code
- 🧪 Code executes safely and returns answers
- 📊 (Coming Soon) Auto-generated charts and summaries
- 📤 (Coming Soon) Export analysis as CSV/PDF

---

## 🔧 Tech Stack

- Python 3.11
- Streamlit
- OpenAI GPT-3.5 Turbo
- Pandas
- dotenv
- Git + GitHub
- (Optional) Docker + Streamlit Cloud

---

## 💻 Installation

```bash
git clone https://github.com/ashruk00/data-analyst-copilot.git
cd data-analyst-copilot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Create a .env file with your OpenAI key:

ini
Copy
Edit
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
▶️ Run the App
bash
Copy
Edit
streamlit run streamlit_app.py
Visit http://localhost:8501



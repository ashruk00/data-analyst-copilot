import streamlit as st
import pandas as pd
from app.gpt_agent import generate_pandas_code
from app.code_executor import run_code

st.set_page_config(page_title="🧠 Data Analyst Copilot", layout="wide")
st.title("🧠 LLM-Powered Data Analyst Copilot")
st.markdown("Upload a CSV and ask questions. GPT will generate code and get you insights!")

# Upload CSV
uploaded_file = st.file_uploader("📁 Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Preview of Uploaded Data")
    st.dataframe(df.head())

    question = st.text_input("❓ Ask a question about your data:")

    if st.button("Run Analysis") and question:
        with st.spinner("🔍 Asking GPT..."):
            # Call GPT to get code
            code = generate_pandas_code(question, df.columns.tolist())
            st.code(code, language="python")

            # Execute the code
            result, error = run_code(code, df)

            if error:
                st.error(f"❌ Error running code:\n{error}")
            elif result is not None:
                st.success("✅ Here's your result:")
                st.dataframe(result)
            else:
                st.warning("⚠️ No result returned. Make sure your GPT prompt outputs a 'result'.")
else:
    st.info("👈 Upload a CSV file to begin.")


# app/gpt_agent.py
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_pandas_code(prompt, columns):
    system_prompt = (
        f"You are a data analyst. Given the user's question and these columns: {columns}, "
        "generate valid Python Pandas code (no imports) to answer the question. "
        "The DataFrame is named 'df'. End the code by assigning the final output to a variable called 'result'."
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


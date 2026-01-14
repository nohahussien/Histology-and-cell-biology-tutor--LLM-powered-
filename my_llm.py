from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = """
You are an expert tutor in Histology and Cell Biology.
ONLY answer questions related to histology, cell biology, tissues, microscopy,
cell organelles, and molecular cell biology.

If the question is outside this domain, respond with:
"Sorry, I can only answer questions related to Histology and Cell Biology."
"""

def ask_llm(question: str) -> str:
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question}
        ],
        temperature=0.3
    )
    return completion.choices[0].message.content




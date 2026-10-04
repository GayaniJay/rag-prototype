from openai import OpenAI
from config import *

client = OpenAI(api_key=OPENAI_API_KEY)

def build_prompt(query, docs):
    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
Answer the question based only on the context below.

Context:
{context}

Question:
{query}
"""
    return prompt

def generate_answer(query, docs):
    prompt = build_prompt(query, docs)

    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content
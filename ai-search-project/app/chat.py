from google import genai
from app.config import GEMINI_API_KEY
from app.search import search

client = genai.Client(api_key=GEMINI_API_KEY)

def ask_question(query):
    print("🔍 Retrieving context...")
    results = search(query)

    context = "\n".join([r["text"] if isinstance(r, dict) else r for r in results])

    print("🤖 Generating answer...")

    response = client.models.generate_content(
        model="gemini-1.5-pro",   # ✅ FIXED
        contents=f"""
Answer the question based on the context below.

Context:
{context}

Question:
{query}
"""
    )

    return response.text
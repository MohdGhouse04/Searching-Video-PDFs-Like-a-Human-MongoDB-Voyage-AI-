import voyageai
from app.config import VOYAGE_API_KEY

# Initialize Voyage client
vo = voyageai.Client(api_key=VOYAGE_API_KEY)

# ✅ Chunking function
def chunk_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return chunks

# ✅ Embedding function
def get_embeddings(text_chunks):
    result = vo.embed(
        text_chunks,
        model="voyage-2"
    )
    return result.embeddings
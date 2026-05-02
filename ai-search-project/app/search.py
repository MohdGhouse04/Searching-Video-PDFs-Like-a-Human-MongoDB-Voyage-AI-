from app.db import collection
from app.embedding import get_embeddings

def search(query, top_k=3):
    print("🔍 Searching...")

    # Convert query to embedding
    query_embedding = get_embeddings([query])[0]

    # MongoDB vector search
    results = collection.aggregate([
        {
            "$vectorSearch": {
                "queryVector": query_embedding,
                "path": "embedding",
                "numCandidates": 100,
                "limit": top_k,
                "index": "vector_index"
            }
        }
    ])

    output = []
    for doc in results:
        output.append(doc["text"])  # ✅ return text only

    return output
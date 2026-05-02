from app.db import collection
from app.pdf_reader import extract_text_from_pdf
from app.embedding import chunk_text, get_embeddings

# ✅ Batching function (VERY IMPORTANT)
import time

def generate_embeddings_in_batches(chunks, batch_size=1):
    all_embeddings = []

    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i + batch_size]
        print(f"⚡ Processing batch {i//batch_size + 1}")

        batch_embeddings = get_embeddings(batch)
        all_embeddings.extend(batch_embeddings)

        # 🛑 IMPORTANT: wait to avoid rate limit
        time.sleep(25)  # wait ~25 seconds

    return all_embeddings


def index_pdf(file_path):
    print("📄 Reading PDF...")
    text = extract_text_from_pdf(file_path)

    print("✂️ Chunking text...")
    chunks = chunk_text(text)

    # ✅ Limit for testing (optional but recommended)
    chunks = chunks[:5]

    print("🧠 Generating embeddings...")
    embeddings = generate_embeddings_in_batches(chunks)

    print("💾 Storing in MongoDB...")

    docs = []
    for i in range(len(chunks)):
        docs.append({
            "text": chunks[i],
            "embedding": embeddings[i]
        })

    # Optional: clear old data
    collection.delete_many({})

    collection.insert_many(docs)

    print("✅ Data indexed successfully!")
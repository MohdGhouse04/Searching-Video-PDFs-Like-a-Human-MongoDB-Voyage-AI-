from pymongo import MongoClient
from app.config import MONGO_URI, DB_NAME, COLLECTION_NAME

client = MongoClient(MONGO_URI)

db = client[DB_NAME]
collection = db[COLLECTION_NAME]

def test_connection():
    try:
        client.admin.command('ping')
        print("✅ MongoDB connected successfully!")
    except Exception as e:
        print("❌ Connection failed:", e)
def insert_sample_data():
    sample_docs = [
        {"text": "Machine learning is a subset of AI"},
        {"text": "Deep learning uses neural networks"},
        {"text": "MongoDB is a NoSQL database"}
    ]

    collection.insert_many(sample_docs)
    print("✅ Sample data inserted!")


def fetch_all_data():
    docs = collection.find()

    print("\n📄 Documents in DB:")
    for doc in docs:
        print(doc)
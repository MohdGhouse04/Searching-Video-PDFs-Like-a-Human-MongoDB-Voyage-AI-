import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

# ✅ ADD THIS LINE
VOYAGE_API_KEY = os.getenv("VOYAGE_API_KEY")

# Debug (temporary)
print("VOYAGE API KEY:", VOYAGE_API_KEY)
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# print("OPENAI API KEY:", OPENAI_API_KEY)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
print("GEMINI API KEY:", GEMINI_API_KEY)
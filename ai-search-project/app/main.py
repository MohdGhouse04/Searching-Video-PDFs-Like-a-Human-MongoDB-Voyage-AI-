# from app.db import test_connection, insert_sample_data, fetch_all_data


# if __name__ == "__main__":
#     test_connection()
#     insert_sample_data()
#     fetch_all_data()

from app.pdf_reader import extract_text_from_pdf

text = extract_text_from_pdf("sample.pdf")
print(text[:500])
from app.pdf_reader import extract_text_from_pdf
from app.embedding import chunk_text

text = extract_text_from_pdf("sample.pdf")
chunks = chunk_text(text)

print("Total chunks:", len(chunks))
print(chunks[0])

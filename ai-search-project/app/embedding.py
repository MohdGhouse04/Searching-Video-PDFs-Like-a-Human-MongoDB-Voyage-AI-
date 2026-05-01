import voyageai

vo = voyageai.Client()

def get_embeddings(text_chunks):
    embeddings = vo.embed(
        text_chunks,
        model="voyage-2"
    ).embeddings

    return embeddings
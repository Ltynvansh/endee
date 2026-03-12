import numpy as np
from embedding import get_embedding

documents = open("dataset.txt").read().split("\n\n")

doc_embeddings = [get_embedding(doc) for doc in documents]

def search(query):
    query_embedding = get_embedding(query)

    scores = []

    for emb in doc_embeddings:
        score = np.dot(query_embedding, emb)
        scores.append(score)

    best_index = np.argmax(scores)

    return documents[best_index]

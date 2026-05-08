from sentence_transformers import SentenceTransformer
import numpy as np
import json
import faiss
docIdx_file_path = r"data/index_document.faiss"
chunks_file_path = r"data/chunks_copy.json"
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_query(user_input: str) -> np.ndarray:
    vector = model.encode(user_input)
    vector = vector.astype(np.float32)
    vector = vector.reshape(1, -1)  # reshape to 2D [1, 384] before normalize
    faiss.normalize_L2(vector)  # normalize since in document index we also already normalize all vectors
    return vector

def search_similar(index_document, query_vector, top_k=5):
    # use cosine similarity here:
    distances, indices = index_document.search(query_vector, k=top_k)
    return distances[0], indices[0] # get flat list 


def main():
    # load index document that contain all vector represent text
    index = faiss.read_index(docIdx_file_path)

    # load chunks.json
    with open(chunks_file_path, encoding="utf-8") as f:
        chunks = json.load(f)

    # test a query
    query = "open house"
    query_vector = embed_query(query)
    distances, indices = search_similar(index, query_vector, top_k=5)


    for i, actual_idx in enumerate(indices):
        print("COSINE SIMILARITY SCORE: ", distances[i])
        print(chunks[actual_idx]["chunk_text"])
        print("\n------------------------------------------------------------------------------------------\n")



if __name__ == "__main__":
    main()



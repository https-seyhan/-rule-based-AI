from sentence_transformers import SentenceTransformer, util

# Load pre-trained SBERT model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')  # You can choose a larger model like 'paraphrase-MPNet-base-v2'

def semantic_phrase_matching(phrase1, phrase2):
    """
    Calculate the semantic similarity between two phrases using SBERT.
    """
    # Encode both phrases into embedding vectors
    embeddings1 = model.encode(phrase1, convert_to_tensor=True)
    embeddings2 = model.encode(phrase2, convert_to_tensor=True)

    # Compute cosine similarity between the embeddings
    cosine_similarity = util.pytorch_cos_sim(embeddings1, embeddings2)
    
    return cosine_similarity.item()

# Example usage:
phrase1 = "How to train a neural network?"
phrase2 = "Ways to learn deep learning models."

similarity_score = semantic_phrase_matching(phrase1, phrase2)
print(f"Similarity Score: {similarity_score}")


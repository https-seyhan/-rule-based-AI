from sentence_transformers import SentenceTransformer, util
import torch

# Load pre-trained SBERT model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')  # You can choose other variants like 'all-MiniLM-L6-v2' or 'stsb-roberta-large'

# Define two lists of phrases
phrases1 = [
    "I love machine learning.",
    "Python is a great programming language.",
    "The weather is nice today."
]

phrases2 = [
    "Machine learning is fascinating.",
    "Python is popular for data science.",
    "It's a sunny day."
]

# Encode phrases into dense embeddings
embeddings1 = model.encode(phrases1, convert_to_tensor=True)
embeddings2 = model.encode(phrases2, convert_to_tensor=True)

# Compute cosine similarity between each pair of phrases
cosine_scores = util.pytorch_cos_sim(embeddings1, embeddings2)

# Print cosine similarity matrix
print("Cosine Similarity Matrix:")
print(cosine_scores)

# Optionally: Convert cosine similarity to a readable format
for i, phrase1 in enumerate(phrases1):
    for j, phrase2 in enumerate(phrases2):
        print(f"Similarity between \"{phrase1}\" and \"{phrase2}\": {cosine_scores[i][j]:.4f}")


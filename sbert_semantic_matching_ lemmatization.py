import spacy
from sentence_transformers import SentenceTransformer, util

# Load pre-trained SBERT model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Load SpaCy model for lemmatization
nlp = spacy.load('en_core_web_sm')

def lemmatize_phrase(phrase):
    """
    Lemmatize the input phrase using SpaCy.
    """
    doc = nlp(phrase)
    return " ".join([token.lemma_ for token in doc])

def check_substring(phrase1, phrase2):
    """
    Check if one lemmatized phrase is a substring of the other.
    """
    phrase1_lower = phrase1.lower()
    phrase2_lower = phrase2.lower()

    # Check if either lemmatized phrase is a substring of the other
    if phrase1_lower in phrase2_lower or phrase2_lower in phrase1_lower:
        return True
    return False

def semantic_phrase_matching(phrase_list1, phrase_list2):
    """
    Calculate the semantic similarity between two lists of phrases using SBERT.
    If one phrase is a substring of the other after lemmatization, assign a similarity score of 1.
    """
    similarity_scores = []

    for phrase1 in phrase_list1:
        lemmatized_phrase1 = lemmatize_phrase(phrase1)

        for phrase2 in phrase_list2:
            lemmatized_phrase2 = lemmatize_phrase(phrase2)

            # Check for substring condition after lemmatization
            if check_substring(lemmatized_phrase1, lemmatized_phrase2):
                similarity_scores.append(1.0)
            else:
                # Encode both phrases into embedding vectors
                embeddings1 = model.encode(phrase1, convert_to_tensor=True)
                embeddings2 = model.encode(phrase2, convert_to_tensor=True)

                # Compute cosine similarity between the embeddings
                cosine_similarity = util.pytorch_cos_sim(embeddings1, embeddings2)
                similarity_scores.append(cosine_similarity.item())

    return similarity_scores

# Example usage:
phrase_list1 = ["How to train a neural network?", "Deep learning tutorials", "Understanding AI"]
phrase_list2 = ["Training neural networks", "Learn deep learning from scratch", "AI understanding"]

similarity_scores = semantic_phrase_matching(phrase_list1, phrase_list2)

for score in similarity_scores:
    print(f"Similarity Score: {score}")


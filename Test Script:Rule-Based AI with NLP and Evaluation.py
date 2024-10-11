import nltk
from sklearn.metrics import confusion_matrix, classification_report, f1_score, precision_score, recall_score
import numpy as np

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Sample dataset
texts = [
    "The construction work is progressing well.",  # Class 1: Positive
    "There are delays in the project schedule.",    # Class 0: Negative
    "The team completed the task on time.",         # Class 1: Positive
    "We are behind the planned timeline.",          # Class 0: Negative
    "The foundation work has started successfully.",# Class 1: Positive
    "The project is experiencing issues with supplies." # Class 0: Negative
]

# Ground truth labels (binary classification: 1 = positive, 0 = negative)
y_true = [1, 0, 1, 0, 1, 0]

# Rule-based classification function
def rule_based_classifier(text):
    # Simple rule-based model
    positive_keywords = ['well', 'completed', 'successfully', 'on time', 'progressing']
    negative_keywords = ['delays', 'issues', 'behind', 'problem', 'difficult']
    
    # Tokenize the text
    tokens = nltk.word_tokenize(text.lower())
    
    # Rule-based classification based on keywords
    if any(word in tokens for word in positive_keywords):
        return 1  # Positive
    elif any(word in tokens for word in negative_keywords):
        return 0  # Negative
    else:
        return np.random.choice([0, 1])  # Random if no keywords are found

# Apply the classifier to predict the labels
y_pred = [rule_based_classifier(text) for text in texts]

# Evaluation Metrics
conf_matrix = confusion_matrix(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
report = classification_report(y_true, y_pred)

# Print the results
print("Confusion Matrix:")
print(conf_matrix)
print("\nF1-Score: {:.2f}".format(f1))
print("Precision: {:.2f}".format(precision))
print("Recall: {:.2f}".format(recall))
print("\nClassification Report:\n", report)


# Import necessary libraries
from sklearn.feature_extraction.text import TfidfVectorizer

"""
TF-IDF is an advanced version of Bag of Words (BoW). It adjusts the word count feature by considering the frequency of words across the entire corpus, 
giving less weight to commonly used words and more weight to rare but important words.

Term Frequency (TF): How frequently a word appears in a document.
Inverse Document Frequency (IDF): How unique or rare a word is across all documents.
"""

# Sample corpus
corpus = [
    "Arsenal won the match against Chelsea.",
    "Chelsea played well, but Arsenal secured the victory.",
    "The game was intense, and Arsenal's performance was outstanding.",
]

# Step 1: Initialize the TfidfVectorizer
# This vectorizer computes the TF-IDF score for each word in the corpus.
tfidf_vectorizer = TfidfVectorizer()

# Step 2: Fit and transform the corpus
X_tfidf = tfidf_vectorizer.fit_transform(corpus)

# Step 3: Convert the result into an array and display feature names (words)
print("Feature Names (Words):", tfidf_vectorizer.get_feature_names_out())
print("TF-IDF Representation (Matrix):\n", X_tfidf.toarray())

# Feature Names (Words): Each column corresponds to a word in the vocabulary.
# TF-IDF Matrix: The numbers represent the importance of each word in each document. 
# A higher value means the word is more important in that document relative to others in the corpus.
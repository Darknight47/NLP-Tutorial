"""
N-Grams represent sequences of N consecutive words in a text. They capture local context and word dependencies that can be important 
for understanding phrases, as opposed to individual words.

Unigrams: Single words (1-gram).
Bigrams: Sequences of two consecutive words (2-gram).
Trigrams: Sequences of three consecutive words (3-gram).

N-Grams are useful when you need to capture dependencies between words in text, 
such as identifying common phrases or word sequences that can provide better context than individual words.
"""

# Import necessary libraries
from sklearn.feature_extraction.text import CountVectorizer

# Sample corpus
corpus = [
    "Arsenal won the match against Chelsea.",
    "Chelsea played well, but Arsenal secured the victory.",
    "The game was intense, and Arsenal's performance was outstanding.",
]

# Step 1: Initialize the CountVectorizer with n-gram range (e.g., bigrams and trigrams)
vectorizer = CountVectorizer(ngram_range=(2, 3))  # You can adjust the range (2,2) for only bigrams, (3,3) for only trigrams
#ngram_range: This parameter controls the range of n-grams. For example:
# ngram_range=(2, 2) captures only bigrams (2 consecutive words).
# ngram_range=(3, 3) captures only trigrams (3 consecutive words).
# ngram_range=(2, 3) captures both bigrams and trigrams.

# Step 2: Fit and transform the corpus to get the n-grams
# This function learns the vocabulary of n-grams and transforms the text into an n-grams matrix.
X_ngrams = vectorizer.fit_transform(corpus)

# Step 3: Convert the result into an array and display n-gram features
print("N-Gram Features (Bigrams and Trigrams):", vectorizer.get_feature_names_out())
print("N-Grams Representation (Matrix):\n", X_ngrams.toarray())

# N-Gram Features: The extracted bigrams and trigrams (like "against chelsea", "arsenal secured").
# N-Grams Matrix: Each row represents a document (sentence), and each column corresponds to an n-gram. 
# The values represent how many times each n-gram appears in the respective document.
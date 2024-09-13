# Import necessary libraries
from sklearn.feature_extraction.text import CountVectorizer

# Sample corpus
corpus = [
    "Arsenal won the match against Chelsea.",
    "Chelsea played well, but Arsenal secured the victory.",
    "The game was intense, and Arsenal's performance was outstanding.",
]

# Step 1: Initialize the CountVectorizer
vectorizer = CountVectorizer()

# Step 2: Fit and transform the corpus
X = vectorizer.fit_transform(corpus)

# Step 3: Convert the result into an array and display feature names (words)
print("Feature Names (Words):", vectorizer.get_feature_names_out())
print("Bag of Words Representation (Matrix):\n", X.toarray())
"""
Instead of representing text as individual words (like BoW), it groups semantically related words into "concepts." 
Concepts can be entities, topics, or any meaningful clusters of words that convey a specific meaning or theme in the text.
"""

# Import necessary libraries
from collections import Counter
import re

# Sample corpus (you can replace these sentences with any text)
corpus = [
    "Arsenal won the match against Chelsea.",
    "Chelsea played well, but Arsenal secured the victory.",
    "The game was intense, and Arsenal's performance was outstanding.",
]

# Define the predefined concepts (list of words representing each concept)
concepts = {
    "Arsenal-related": ["arsenal", "gunners", "emirates"],
    "Match-related": ["match", "game", "play", "played"],
    "Victory-related": ["win", "victory", "secured"],
}

# Preprocess function to clean and tokenize text
def preprocess_text(text):
    # Lowercase the text
    text = text.lower()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Tokenize the text (split into words)
    return text.split()

# Step 1: Initialize an empty list to store the Bag of Concepts
bag_of_concepts = []

# Step 2: Loop through each document in the corpus
for document in corpus:
    tokenized_text = preprocess_text(document)
    document_concepts = Counter()
    
    # Step 3: Count the occurrence of each concept
    for concept, words in concepts.items():
        concept_count = sum([tokenized_text.count(word) for word in words])
        document_concepts[concept] = concept_count
    
    # Append the concept counts to the Bag of Concepts
    bag_of_concepts.append(document_concepts)

# Step 4: Display the Bag of Concepts for each document
for idx, doc_concepts in enumerate(bag_of_concepts):
    print(f"Document {idx + 1} Bag of Concepts: {dict(doc_concepts)}")

# Document 1: Talks about Arsenal and the match, but not victory.
# Document 2: Mentions Arsenal, the match, and winning.
# Document 3: Focuses on Arsenal and the match, but doesn't emphasize victory.
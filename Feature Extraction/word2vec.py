# Import necessary libraries
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import nltk

# Download NLTK data for tokenization
nltk.download('punkt')

# Sample corpus (you can replace these sentences with any text)
corpus = [
    "Arsenal won the match against Chelsea.",
    "Chelsea played well, but Arsenal secured the victory.",
    "The game was intense, and Arsenal's performance was outstanding.",
]

# Step 1: Tokenize the sentences into words
# The text is tokenized into words using nltk. This step is necessary because Word2Vec processes words as individual tokens.
tokenized_corpus = [word_tokenize(sentence.lower()) for sentence in corpus]

# Step 2: Initialize and train the Word2Vec model
# Parameters: sg=1 (Skip-gram), vector_size=100 (vector dimension), window=5 (context window), min_count=1 (ignore less frequent words)
word2vec_model = Word2Vec(sentences=tokenized_corpus, vector_size=100, window=5, min_count=1, sg=1)

# Step 3: Check the vector representation of a word (e.g., "arsenal")
print("Vector for 'arsenal':\n", word2vec_model.wv['arsenal'])

# Step 4: Find similar words to a given word (e.g., "arsenal")
print("\nWords similar to 'arsenal':", word2vec_model.wv.most_similar('arsenal'))
# The most_similar function finds words with vectors similar to the given word.

# Word Vectors: Each word is represented by a 100-dimensional vector (for example, "arsenal").
# Similar Words: The model can suggest words that are semantically close to "arsenal" based on their vector representation.
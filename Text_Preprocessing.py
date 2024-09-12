# Import necessary libraries
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
import re
import string

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Sample text (feel free to replace this with Arsenal FC related text)
sample_text = """Arsenal FC had an incredible performance in the Premier League last night. 
                The team's defense was solid, but the real highlight was Bukayo Saka's goal!"""

# Step 1: Lowercasing
def lower_case(text):
    return text.lower()

print(lower_case(sample_text))
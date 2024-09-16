import re

from nltk.corpus import stopwords  # Importing stopwords from nltk.corpus
import nltk

# Download stopwords if not already downloaded
nltk.download('stopwords')


text = "Hello, World! 123"

# Removing punctuation and numbers
text_clean = re.sub(r'[^a-zA-Z\s]', '', text)
print(text_clean)  # Output: 'Hello World '


# Getting English stop words
stop_words = set(stopwords.words('english'))

# Sample tokens
tokens = ['this', 'is', 'an', 'example']

# Filtering out stop words
filtered_tokens = [word for word in tokens if word not in stop_words]

print(filtered_tokens)
# Output: ['example']

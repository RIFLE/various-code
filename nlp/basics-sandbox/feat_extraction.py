# Importing CountVectorizer class from sklearn.feature_extraction.text module
from sklearn.feature_extraction.text import CountVectorizer

# Sample corpus (a list of documents)
corpus = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?'
]

# Creating an instance of CountVectorizer
vectorizer = CountVectorizer()

# Fitting the model and transforming the corpus into a BoW representation
X = vectorizer.fit_transform(corpus)

# Getting feature names (unique words)
feature_names = vectorizer.get_feature_names_out()

print('\n', feature_names)
# Output: ['and' 'document' 'first' 'is' 'one' 'second' 'the' 'third' 'this']

print(X.toarray())




# Importing TfidfVectorizer class from sklearn.feature_extraction.text module
from sklearn.feature_extraction.text import TfidfVectorizer

# Creating an instance of TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fitting the model and transforming the corpus into TF-IDF representation
X_tfidf = tfidf_vectorizer.fit_transform(corpus)

# Getting feature names
feature_names_tfidf = tfidf_vectorizer.get_feature_names_out()

print('\n', feature_names_tfidf)
print(X_tfidf.toarray())

import nltk
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Download nltk data for stop words
nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Sample text data
texts = [
    "Natural Language Processing with Python and NLTK is interesting.",
    "Bag of Words and TF-IDF are essential for text representation.",
    "NLP involves both statistical and machine learning methods."
]

# Define a simple preprocessing function
def preprocess(text):
    # Lowercase and tokenize
    tokens = word_tokenize(text.lower())
    # Remove stopwords
    tokens = [word for word in tokens if word.isalpha() and word not in stopwords.words('english')]
    return ' '.join(tokens)

# Apply preprocessing to each document
texts = [preprocess(text) for text in texts]
print("Preprocessed Texts:", texts)

# Initialize CountVectorizer for BoW with unigrams
bow_vectorizer = CountVectorizer()
bow_matrix = bow_vectorizer.fit_transform(texts)

# Display the feature names and BoW representation
print("BoW Feature Names:", bow_vectorizer.get_feature_names_out())
print("BoW Matrix (as array):\n", bow_matrix.toarray())

# Initialize TfidfVectorizer for TF-IDF with unigrams
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(texts)

# Display the feature names and TF-IDF representation
print("TF-IDF Feature Names:", tfidf_vectorizer.get_feature_names_out())
print("TF-IDF Matrix (as array):\n", tfidf_matrix.toarray())

# Initialize CountVectorizer for Bigrams (2-grams)
bigram_vectorizer = CountVectorizer(ngram_range=(2, 2))
bigram_matrix = bigram_vectorizer.fit_transform(texts)

print("Bigram Feature Names:", bigram_vectorizer.get_feature_names_out())
print("Bigram Matrix (as array):\n", bigram_matrix.toarray())

# Initialize CountVectorizer for Trigrams (3-grams)
trigram_vectorizer = CountVectorizer(ngram_range=(3, 3))
trigram_matrix = trigram_vectorizer.fit_transform(texts)

print("Trigram Feature Names:", trigram_vectorizer.get_feature_names_out())
print("Trigram Matrix (as array):\n", trigram_matrix.toarray())

# TF-IDF representation with bigrams
tfidf_bigram_vectorizer = TfidfVectorizer(ngram_range=(2, 2))
tfidf_bigram_matrix = tfidf_bigram_vectorizer.fit_transform(texts)

print("TF-IDF Bigram Feature Names:", tfidf_bigram_vectorizer.get_feature_names_out())
print("TF-IDF Bigram Matrix (as array):\n", tfidf_bigram_matrix.toarray())
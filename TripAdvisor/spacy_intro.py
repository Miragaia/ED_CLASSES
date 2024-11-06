import spacy
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

#If not downloaded during installation, make sure to download the model
#spacy download en_core_web_md

# Load spaCy's English model
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "Apple is looking to buy a startup in the AI sector based in San Francisco."

# Process the text with spaCy
doc = nlp(text)

# Tokenization
tokens = [token.text for token in doc]
print("Tokens:", tokens)

# Lemmatization
lemmas = [token.lemma_ for token in doc]
print("Lemmas:", lemmas)
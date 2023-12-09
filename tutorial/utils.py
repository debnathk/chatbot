# pip install nltk
import nltk
from nltk.stem.porter import PorterStemmer

# nltk.download('punkt')

# Tokeinizing
def tokenize(sentence):
    return nltk.word_tokenize(sentence)

# Stemming
stemmer = PorterStemmer()
def stem(word):
    return stemmer.stem(word.lower())

print(tokenize("Hi, I am Kusal."))

words = ['Organize', 'Organization', 'Organizer']
stemmed_words = [stem(w) for w in words]

print(stemmed_words)
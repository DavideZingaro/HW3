import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string


# funcion for cleaning the intro and plot for the film
# we choose to clean only intro and plot cause the search engine works only on them
# we doesn't save cleaned document because we want a readable intro and plot in the data frame
def cleaner(to_clean):
    stop_words = set(stopwords.words('english'))
    
    # tokenize intro and plot
    words = word_tokenize(to_clean)
    
    # remove stop words
    filtered = [w for w in words if not w in stop_words]

    # stemming of the words
    ps = PorterStemmer()
    stemmed = []
    for w in filtered:
        stemmed.append(ps.stem(w))
    
    # remove punctations
    punctuations = list(string.punctuation)
    punctuations.append("''")

    without_punctation = [w for w in stemmed if not w in punctuations]
    
    # cleaned text
    return without_punctation




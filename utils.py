import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
from sklearn.metrics.pairwise import cosine_similarity
import pycountry



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



# search engine 2
# film fector (1df1,idf2...)
# query vector (1,1,1.....)
def cosSim(row, query, tfidf_vocabulary, vocabulary):
	cleaned_query = cleaner(query)
	film_vector = []
	query_vector_idf = []
	for elem in cleaned_query:
		elem = vocabulary[elem]
		if(elem in tfidf_vocabulary):
			if(row['film_id'] in tfidf_vocabulary[elem]):
				film_vector.append(tfidf_vocabulary[elem][row['film_id']])
				query_vector_idf.append(1)
			else:
				film_vector.append(0)
				query_vector_idf.append(1)
		else:
			film_vector.append(0)
			query_vector_idf.append(1)

	cos_sim = cosine_similarity([film_vector], [query_vector_idf])[0][0]
	return cos_sim



# part 2

# make a list of languages in our dataframe
def get_languages(data_frame):

	# string with all languages in our dataframe
	languages = ''
	for elem in list(data_frame['Language'].drop_duplicates()):
	    try:
	        l = elem.strip().split()
	    except:
	        continue
	    for lan in l:
	        if lan not in languages:
	            languages += lan

	# take all languages and choose them only if they are in our dataframe
	opt = []
	for elem in list(pycountry.languages):
	    if elem.name in languages and elem.name not in opt and len(elem.name) > 3:
	        opt.append(elem.name)
	opt.append('Silent')
	opt.sort()

	return opt

# select only the films with selected language
def selected_films(row, language):
    try:
        if language in row['Language']:
            return 1
    except:
        return 0
    return 0

# function for defining running time ranking
def R_time_score(row):
	try:
	    time = int(row['Running time'].split()[0])
	    if time < 60:
	        return 4
	    elif time > 120:
	        return 3
	    elif 60 <= time < 90:
	        return 2
	    elif 90 <= time <= 120:
	        return 1
	except Exception as e:
		# no running time
		return 5






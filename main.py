import sys
import pandas as pd
import pickle
import utils
from heapq import heappush, nlargest
import heapq

def main(argv):
	if not argv[1].isnumeric():
		print("Serach engine should be = (1, 2, 3)")
		return
	if 1 < int(argv[1]) > 3:
		print("Serach engine should be = (1, 2, 3)")
		return

	df_films = pd.read_csv('data/films_dataFrame.csv')   # read data frame from a file

	# load words dict
	with open('data/words_dict.pickle', 'rb') as handle:
		words_dict = pickle.load(handle)

    # Load data (deserialize)
	with open('data/vocabulary.pickle', 'rb') as handle:
		vocabulary = pickle.load(handle)

	# Load data (deserialize)
	with open('data/tfidf_dict.pickle', 'rb') as handle:
		tfidf_vocabulary = pickle.load(handle)

	search_engine = int(argv[1])
	query = argv[2]

	if search_engine == 1:
		search_engine_1(df_films, words_dict, query, vocabulary)

	if search_engine == 2:
		search_engine_2(df_films, tfidf_vocabulary, query, vocabulary)

	if search_engine == 3:
		search_engine_3(df_films, tfidf_vocabulary, query, vocabulary)







# search engine 1
def search_engine_1(data_frame, words_dict, q, vocabulary):
	se1 = data_frame
	se1['Engine1'] = se1.apply(search_engine_1_apply, axis = 1, word_dict = words_dict, query = q, vocabulary = vocabulary)
	print(se1[se1['Engine1'] == 1][['title','Wikipedia_link', 'intro']].head(10).to_string())


def search_engine_1_apply(row, word_dict, query, vocabulary):
	cont = 0
	cleaned_query_1 = utils.cleaner(query)
	for elem in cleaned_query_1:
		elem = vocabulary[elem]
		if(elem in word_dict):
			if(row['film_id'] in word_dict[elem]):
				cont += 1
	if cont == len(cleaned_query_1):
	    return 1
	return 0


# Search engine 2
def search_engine_2(data_frame,tfidf_vocabulary, query, vocabulary):
	se2 = data_frame

	# add column similarity to the data frame
	se2['Similarity'] = se2.apply(utils.cosSim, axis = 1, tfidf_vocabulary = tfidf_vocabulary, query = query, vocabulary = vocabulary)

	# create tuples with similarity and film id
	list_tuples = []
	for i in range(30000):
	    list_tuples.append((list(se2[se2['film_id'] == i]['Similarity'])[0], i))

	# order tuples and take top 15th
	heapq.heapify(list_tuples)
	largest_sim = nlargest(15, list_tuples)

	# create a data frame with the top 15th results
	res_sim = pd.DataFrame(columns = ['title', 'intro', 'Wikipedia_link', 'Similarity'])
	for elem in largest_sim:
	    res_sim = res_sim.append(se2[se2['film_id'] == elem[1]][['title', 'intro', 'Wikipedia_link', 'Similarity']])

	print(res_sim.to_string())



# search engine 3
def search_engine_3(data_frame ,tfidf_vocabulary, query, vocabulary):
	se3 = data_frame

	languages = utils.get_languages(se3)

	# ask user for the language
	print("Choose a language from: ")
	print(languages)
	l = input("Select language: ")

	print("You selected: " + l)

	if(l not in languages):
		print("Sorry, your language is not in our dataset")


	# add column with new ranking
	se3['Similarity'] = se3.apply(utils.cosSim, axis = 1, tfidf_vocabulary = tfidf_vocabulary, query = query, vocabulary = vocabulary)

	# add a column to checking the language
	se3['sel_lan'] = se3.apply(utils.selected_films, axis = 1, language = l)

	# create tuples with similarity and film id
	list_tuples = []
	for i in range(30000):
	    list_tuples.append((list(se3[se3['film_id'] == i]['Similarity'])[0], i))

	# order tuples and take top 15th
	heapq.heapify(list_tuples)
	largest_sim = nlargest(15, list_tuples)

	# create a data frame with the top 15th results
	res_sim = pd.DataFrame(columns = ['title', 'intro', 'Wikipedia_link', 'Running time', 'Similarity'])
	for elem in largest_sim:
	    res_sim = res_sim.append(se3[se3['film_id'] == elem[1]][['title', 'intro', 'Wikipedia_link', 'Running time', 'Similarity']])

	# add column ranking running tima
	res_sim['rank_duration'] = res_sim.apply(utils.R_time_score, axis = 1)

	res_sim.sort_values(by = ['rank_duration'], inplace = True, ascending = True)

	print(res_sim[['title', 'intro', 'Wikipedia_link', 'rank_duration']].to_string())




if __name__ == "__main__":
	main(sys.argv)


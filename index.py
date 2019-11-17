import sys
import index_utils
import pandas as pd
import pickle



def main(argv):
	if len(argv) != 2:
		print("Invalid aruments")
		print("You have to specify: ")
		print("arg1 = <path to the films dataframe>")

	path = argv[1]

	# read data frame from a file
	df_films = pd.read_csv(path)

	# create vocabulary
	vocabulary = {}
	df_films.apply(index_utils.create_vocabulary, axis=1, voc = vocabulary)

	# create inverted dict
	words_dict = {}
	df_films['words_number'] = df_films.apply(index_utils.create_inverted_dict, axis=1, 
											inverted_dict = words_dict, vocabulary = vocabulary)

	# Store data (serialize)
	with open('data/vocabulary.pickle', 'wb') as handle:
	    pickle.dump(vocabulary, handle, protocol=pickle.HIGHEST_PROTOCOL)
	    
	# Store data (serialize)
	with open('data/words_dict.pickle', 'wb') as handle:
	    pickle.dump(words_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)

	# create tfidf
	tfidf_dict = index_utils.create_dictionary_tfidf(words_dict, df_films)

	# Store data (serialize)
	with open('data/tfidf_dict.pickle', 'wb') as handle:
	    pickle.dump(tfidf_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)




if __name__ == "__main__":
	main(sys.argv)
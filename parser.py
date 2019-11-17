from lxml import html
from bs4 import BeautifulSoup
import parser_utils
import sys
import pickle



def main(argv):
	if len(argv) != 5:
		print("arg1 = # pagest to download")
		print("arg2 = <path to .html files>")
		print("arg3 = <path where you want to save .tsv files>")
		print("arg3 = <path where you want to save the films data frame>")
		return

	n_pages = int(argv[1])
	p1 = argv[2]  # html
	p2 = argv[3]  # tsv
	p3 = argv[4]  # data frame

	with open('data/links_list.pickle', 'rb') as f:
		links_list = pickle.load(f)

	# save tsv files
	parser_utils.scapper_tsv(n_pages, p1, p2)

	# create films data frame
	df_films = parser_utils.films_data_frame(links_list[:n_pages], p2)

	# save dataframe to a file
	df_films.to_csv(p3 + '/films_dataFrame.csv')




if __name__ == "__main__":
	main(sys.argv)

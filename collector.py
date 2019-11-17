from lxml import html
from bs4 import BeautifulSoup
import collector_utils
import sys
import pickle

def main(argv):
	if len(argv) != 5:
		print("Invalid aruments")
		print("You have to specify: ")
		print("arg1 = <path to movies1>")
		print("arg2 = <path to movies2>")
		print("arg3 = <path to movies3>")
		print("arg4 = <path where you want to save the .html files>")
		return

	# paths
	p1 = argv[1]
	p2 = argv[2]
	p3 = argv[3]
	p4 = argv[4]

	# We take movies1-2-3.html parse them and create a list of links
	links = collector_utils.get_links(p1, p2, p3)

	# save links into a file
	with open('data/links_list.pickle', 'wb') as fp:
		pickle.dump(links, fp)


	# download pages
	#Command started only once to download pages
	collector_utils.download_pages(links, p4)

if __name__ == "__main__":
	main(sys.argv)

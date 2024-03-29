from lxml import html
from bs4 import BeautifulSoup
import urllib.request
from tqdm import tqdm
import time

# get list of links from movies1-2-3
def get_links(file1, file2, file3):
	# create list of the links in movies
	tree1 = html.parse(file1)
	movies1 = html.tostring(tree1)
	soup1 = BeautifulSoup(movies1, 'lxml')

	tree2 = html.parse(file2)
	movies2 = html.tostring(tree2)
	soup2 = BeautifulSoup(movies2, 'lxml')

	tree3 = html.parse(file3)
	movies3 = html.tostring(tree3)
	soup3 = BeautifulSoup(movies3, 'lxml')

	links = []
	for link in soup1.findAll('a'):
	    links.append(link.get('href'))
	for link in soup2.findAll('a'):
	    links.append(link.get('href'))
	for link in soup3.findAll('a'):
	    links.append(link.get('href'))

	return links

def download_pages(links, path):

	# loading bar
	with tqdm(total = len(links)) as pbar:
		for i in range(len(links)):
		    try:
		        html = urllib.request.urlopen(links[i]).read()
		        with open(path + '/article_{}.html'.format(i), 'wb+') as f:
		            f.write(html)
		        time.sleep(random.randint(1, 5))
		    except Exception as e:
		        #print(i, links[i], e)
		        pbar.update(1)
		        continue
		    pbar.update(1)


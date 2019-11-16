from lxml import html
from bs4 import BeautifulSoup
import collector_utils

# We take movies1-2-3.html parse them and create a list of links
links = collector_utils.get_links()

# download pages
#Command started only once to download pages
collector_utils.download_pages(links)
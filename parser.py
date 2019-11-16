from lxml import html
from bs4 import BeautifulSoup
import parser_utils

# save tsv files
parser_utils.scapper_tsv(30000)

# create films data frame
df_films = films_data_frame(30000)

# save dataframe to a file
df_films.to_csv('films_dataFrame.csv')   # save the dataframe into a file
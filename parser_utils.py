from lxml import html
from bs4 import BeautifulSoup
import pandas as pd
import csv
from tqdm import tqdm


# scrap html pages downloaded befor and save informationneeded in tsv files
def scapper_tsv(n_links, path_html, path_tsv):

    # loading bar
    with tqdm(total = n_links) as pbar:

        for article in range(n_links):  # range of files
            try:
                html = BeautifulSoup(open(path_html + "/article_{}.html".format(article)), 'html.parser')
            except Exception as e:   # if article doesn't exists
                print(article, e)
                continue

            title = html.select("h1")[0].text

            # initialize tmp as intro
            tmp = 'intro'
            sections = {'intro' : '', 'plot' : ''}

            # take all paragraphs section by section and save only intro and plot
            for section in html.select('div.mw-parser-output > *'):    # take only notes in the first level
                if(section.name == 'p' and tmp == 'intro'):
                    sections['intro'] += section.text.strip()

                # chage tmp on section names
                if(section.name in ['h2','h3']):
                    tmp = section.span['id']

                # take only sections we are interrested in
                if(section.name == 'p' and tmp in ['Plot','Plot_summary','Premise']):  # check different names for plot sections
                    sections['plot'] += section.text.strip()

            # we doesn't take in consideration pages without Plot
            if(sections['plot'] == ''):
                print(article, 'No Plot')
                continue

            # dictionary for infobox
            d = {'film_name':title, 'Directed by': 'NA', 'Produced by': 'NA', 'Written by': 'NA', 'Starring':'NA', 'Music by': 'NA',
                 'Release date': 'NA', 'Running time': 'NA', 'Country': 'NA', 'Language': 'NA', 'Budget': 'NA'}

            # take elem from infobox
            info_box = html.findAll(['th', 'td'])
            for elem in info_box:
                info = elem.text.strip('\n')   # take text from the table
                if info in d:
                    d[info] = info_box[info_box.index(elem)+1].text.strip('\n')

            # select elem in oroder as a list to save in .tsv
            ld = list(d.values())
            columns = ['title', 'intro', 'plot', 'film_name', 'Directed by', 'Produced by', 'Written by', 'Starring', 'Music by',
                 'Release date', 'Running time', 'Country', 'Language', 'Budget']
            data = [title, sections['intro'], sections['plot']] + ld[0:]

            # create and save a tsv
            with open(path_tsv + '/article_{}.tsv'.format(article), 'w', newline='',encoding='utf-8') as f_output:
                tsv_output = csv.writer(f_output, delimiter='\t')
                tsv_output.writerow(columns)
                tsv_output.writerow(data)

            pbar.update(1)




# create a data frame from the tsv files
def films_data_frame(links, path_tsv):
    # cols of the dataframe
    col = ['film_id','Wikipedia_link', 'title', 'intro', 'plot', 'film_name', 'Directed by', 'Produced by', 'Written by', 'Starring', 'Music by',
             'Release date', 'Running time', 'Country', 'Language', 'Budget']

    # create data frame
    df_films = pd.DataFrame(columns = col)


    with tqdm(total = len(links)) as pbar:

        # append each film
        for i in range(len(links)):
            try:
                with open('path_tsv'+ '/article_{}.tsv'.format(i)) as fd:
                    rd = csv.reader(fd, delimiter="\t", quotechar='"')
                    row = [i, links[i]] + list(rd)[1][0:]
                    df_films = df_films.append(pd.DataFrame([row], columns=col), ignore_index = True)
            except Exception as e:
                df_films = df_films.append(pd.DataFrame([[i, links[i], 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA',
                 'NA', 'NA', 'NA', 'NA', 'NA']], columns=col), ignore_index = True)
                print(i, e)

            pbar.update(1)
    return df_films

import utils
from tqdm import tqdm
import math

global vocabulary
voc_global = 0


# create dictionary of words
# add a column to the data frame containing the length of the document
def create_inverted_dict(row, inverted_dict, vocabulary):
    film_id = row['film_id']
    try:
        text = utils.cleaner(row['intro'] + row['plot'])
    except Exception as e:
        return 0
    for w in text:
        w = vocabulary[w]
        if w not in inverted_dict:
            inverted_dict[w] = {film_id : 1}
        else:
            if film_id not in inverted_dict[w]:
                inverted_dict[w][film_id] = 1
            else:
                inverted_dict[w][film_id] += 1
    return len(text)

# create tfidf dictionary
def create_dictionary_tfidf(Vocabulary, h):
    N_Vocabulary = {}
    with tqdm(total = len(Vocabulary)) as pbar:
        for k in Vocabulary.keys():
            repetition = len(Vocabulary[k])
            IDF = math.log(30000/repetition)
            for elem in Vocabulary[k].keys():
                valore = Vocabulary[k][elem]

                length = list(h[h['film_id'] == elem]['words_number'])[0]

                Tf = (valore)/(length)

                if k not in N_Vocabulary:
                    N_Vocabulary[k] = {elem : Tf*IDF}
                else:
                    N_Vocabulary[k][elem] = Tf*IDF
            pbar.update(1)
    return N_Vocabulary



# create vocabulary
def create_vocabulary(row, voc):
    global voc_global
    try:
        text = utils.cleaner(row['intro'] + row['plot'])
    except:
        return
    for elem in text:
        if elem not in voc:
            voc[elem] = voc_global
            voc_global += 1
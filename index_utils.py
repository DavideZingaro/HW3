import utils





# create dictionary of words
# add a column to the data frame containing the length of the document
def create_inverted_dict(row, vocabulary):
    film_id = row['film_id']
    try:
        text = utils.cleaner(row['intro'] + row['plot'])
    except Exception as e:
        return 0
    for w in text:
        if w not in vocabulary:
            vocabulary[w] = {film_id : 1}
        else:
            if film_id not in vocabulary[w]:
                vocabulary[w][film_id] = 1
            else:
                vocabulary[w][film_id] += 1
    return len(text)



# create vocabulary
def create_words_voc(d):
    vocabulary = {}
    for k,v in enumerate(d):
        vocabulary[v]= k
    return vocabulary
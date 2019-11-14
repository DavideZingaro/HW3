#!/usr/bin/env python
# coding: utf-8

# In[ ]:


document_score=[]
total_rank=[]
for document in query_document:
    rank_document=wup_score(document)
    total_rank+=[rank_document]

def wup_score(document):
    for w in document:
        query=input('query: ')
        w1=wordnet.synset(query)
        w2=wordnet.synset(w)
        score=(w1.wup_similarity(w2))
        document_score+=[score]
        return (mean(document_score),document)
    


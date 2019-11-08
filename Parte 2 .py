#!/usr/bin/env python
# coding: utf-8

# ### Questo serve per gli stop words (sono le nostre congiunzioni,ecc....)

# In[ ]:


from nltk,corpus import stopwords
from nltk.tokenize import word_tokenize 
documents='[lista di documenti che avremo]'
stop_words=set(stopwords.words('english'))
Filtered_Documents=[]
for elem in documents:
    elem= 'document=da inserire documento nostro da wiki'
    words=word_tokenize(document)
    filtered_document=[w for w in words if not stop_words]
    Filtered_Documents+=[filtered_documents]
    
            
    


# ### Questo serve a fare lo stemming cioè prende parole tipo [casale,casolare,casetta] restituisce [casa,casa,casa]

# In[ ]:


from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize
ps=PorterStemmer()
Stemmed_Documents=[]
for elem in Filtered_Document:
    document=elem
    stemmed_document=[ps.stem(w) for w in document] #da rivedere
    Stemmed_Documents+=[stemmed_document]


# ### Manca di togliere la punteggiatura

# ### 2.2 similarity (solo un idea)

# In[1]:


from nltk.corpus import wordnet
from collections import Counter
Documents_10=[]
for elem in Stemmed_Documents:
    document=elem
    for w in document:
        top_10_document=(Counter(words).most_common(10)).keys() #da rivedere
        Documents_10+=[top_10_document]
Tot_Similarity=[]
for i in range (len(Documents_10)):
    A=Documents_10[i]
    B=Documents_10[i+1]
    for i in range(10):
        w1 = wordnet.synset(A[i])
        w2 = wordnet.synset(B[i])
        similarity=(w1.wup_similarity(w2))
        Similarity+=[similarity]               #devo finire un return e fare la maedia 

        
            


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from itertools import combinations
import networkx as nx
import matplotlib.pyplot as plt


# In[ ]:


combination=[]
for i in range(10):
    starring=(b['Starring'][i].split('\n'))
    combination+=list(combinations(starring, 2))
relations_actor=[x for x in combination if combination.count(x)>1]
actors=[]
for i in relations_actor:
    for j in i:
        actors+=[j]
actors=set(actors)
actors=list(actors)
act_dic={}

for i in actors:
    act_dic[i]=actors.index(i)
relations_actor_2=[]
for elem in relations_actor:
    elem=list(elem)
    relations_actor_2+=[elem]
for i in relations_actor_2:
    i[0]=act_dic[i[0]]
    i[1]=act_dic[i[1]]


g=nx.Graph()
for i in act_dic.values():
    g.add_node(i)
for i in relations_actor_2:
    g.add_edge(*i)
nx.draw(g)


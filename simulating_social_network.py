
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd

import networkx as nx

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb


# In[2]:

get_ipython().magic('matplotlib inline')
rcParams['figure.figsize']=5,4
sb.set_style('whitegrid')


# # Generating a graph object and edgelist

# In[4]:

dg=nx.gn_graph(7, seed=25)

for line in nx.generate_edgelist(dg,data=False): print(line)


# # Assigning attributes to nodes

# In[6]:

print (dg.node[0])


# In[7]:

dg.node[0]['name']='Alice'


# In[8]:

print(dg.node[0])


# In[9]:

dg.node[1]['name']= 'Bob'
dg.node[2]['name']= 'Claire'
dg.node[3]['name']= 'Dennis'
dg.node[4]['name']= 'Esther'
dg.node[5]['name']= 'Frank'
dg.node[6]['name']= 'George'


# In[14]:

dg.add_nodes_from([(0,{'age':25}),(1,{'age':31}),(2,{'age':18}),(3,{'age':47}),(4,{'age':22}),(5,{'age':23}),(6,{'age':50})])
print (dg.node[0])


# In[15]:

dg.node[0]['gender']='f'
dg.node[1]['gender']='m'
dg.node[2]['gender']='f'
dg.node[3]['gender']='m'
dg.node[4]['gender']='f'
dg.node[5]['gender']='m'
dg.node[6]['gender']='n'


# # Visualizing the network graph

# In[16]:

nx.draw_circular(dg,node_color='bisque', with_labels=True)


# In[17]:

labeldict={0: 'Alice',1:'bob',2:'Claire',3:'Dennis',4:'Esther',5:'Frank',6:'George'}

nx.draw_circular(dg,labels=labeldict,node_color='bisque', with_labels=True)


# In[18]:

g=dg.to_undirected()



# In[19]:

nx.draw_spectral(g, labels=labeldict, node_color='bisque',with_labels=True)


# In[ ]:




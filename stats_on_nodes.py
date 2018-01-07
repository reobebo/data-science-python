
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

import networkx as nx


# In[2]:

get_ipython().magic('matplotlib inline')
rcParams['figure.figsize']=5,4
sb.set_style('whitegrid')


# In[7]:

dg=nx.gn_graph(7,seed=25)

for line in nx.generate_edgelist(dg,data=False):
    print (line)
    
dg.node[0]['name']= 'Alice'    
dg.node[1]['name']= 'Bob'
dg.node[2]['name']= 'Claire'
dg.node[3]['name']= 'Dennis'
dg.node[4]['name']= 'Esther'
dg.node[5]['name']= 'Frank'
dg.node[6]['name']= 'George'


# In[8]:

g = dg.to_undirected()


# In[9]:

print (nx.info(dg))


# # Considering degrees in a social network

# In[10]:

dg.degree()


# # Identifying successor nodes

# In[11]:

nx.draw_circular(dg,node_color='bisque', with_labels=True)


# In[12]:

dg.successors(3)


# In[13]:

dg.neighbors(4)


# In[14]:

g.neighbors(4)


# In[ ]:





# coding: utf-8

# In[1]:

get_ipython().system(' pip install networkx')


# In[2]:

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

import networkx as nx


# In[3]:

get_ipython().magic('matplotlib inline')
rcParams['figure.figsize']=5,4
sb.set_style('whitegrid')


# # Creating graph objects

# In[4]:

g=nx.Graph()
nx.draw(g)


# In[5]:

g.add_node(1)
nx.draw(g)


# In[7]:

g.add_nodes_from([2,3,4,5,6,8,9,12,15,16])
nx.draw(g)


# In[8]:

g.add_edges_from([(2,4),(2,6),(2,8),(2,12),(2,16),(3,6),(3,9),(3,12),(3,15),(4,8),(4,12),(4,16),(6,12),(8,16)])
nx.draw(g)


# # The basics about drawing graph objects

# In[9]:

nx.draw_circular(g)


# In[10]:

nx.draw_spring(g)


# # Labeling and coloring your graph plots

# In[11]:

nx.draw_circular(g, node_color='bisque', with_labels=True)


# In[15]:

g.remove_node(1)
nx.draw_circular(g, node_color='bisque', with_labels=True)


# # Identifying graph properties

# In[16]:

sum_stats=nx.info(g)
print (sum_stats)


# In[18]:

print (nx.degree(g))


# # Using graph generators

# In[19]:

g=nx.complete_graph(25)
nx.draw(g,node_color='bisque', with_labels=True)


# In[20]:

g=nx.gnc_graph(7,seed=25)
nx.draw(g,node_color='bisque', with_labels=True)


# In[21]:

ego_g = nx.ego_graph(g, 3, radius=5)
nx.draw(g,node_color='bisque', with_labels=True)


# In[ ]:




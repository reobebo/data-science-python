
# coding: utf-8

# In[3]:

import numpy as np
import pandas as pd

import scipy
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.cluster.hierarchy import fcluster
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

import sklearn 
from sklearn.cluster import AgglomerativeClustering
import sklearn.metrics as sm


# In[4]:

np.set_printoptions(precision=4, suppress=True)
plt.figure(figsize=(10,3))
get_ipython().magic('matplotlib inline')
plt.style.use('seaborn-whitegrid')


# In[6]:

address='/Users/Apple/Documents/Lynda/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv'
cars=pd.read_csv(address)
cars.columns=['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

x= cars.ix[:,(1,3,4,6)].values

y= cars.ix[:,(9)].values


# # Using scipy to generate dendrograms

# In[7]:

z=linkage(x,'ward')


# In[8]:

dendrogram(z,truncate_mode='lastp',p=12,leaf_rotation=45.,leaf_font_size=15.,show_contracted=True)
plt.title('Truncated Hierarchical Clustering Dendrogram')
plt.xlabel('Cluster Size')
plt.ylabel('Distance')

plt.axhline(y=500)
plt.axhline(y=150)
plt.show()


# # Generating hierarchical clusters

# In[11]:

k=2

Hclustering=AgglomerativeClustering(n_clusters=k, affinity='euclidean',linkage='ward')
Hclustering.fit(x)

sm.accuracy_score(y,Hclustering.labels_)


# In[12]:

Hclustering=AgglomerativeClustering(n_clusters=k, affinity='euclidean',linkage='complete')
Hclustering.fit(x)

sm.accuracy_score(y,Hclustering.labels_)


# In[13]:

Hclustering=AgglomerativeClustering(n_clusters=k, affinity='euclidean',linkage='average')
Hclustering.fit(x)

sm.accuracy_score(y,Hclustering.labels_)


# In[14]:

Hclustering=AgglomerativeClustering(n_clusters=k, affinity='manhattan',linkage='average')
Hclustering.fit(x)

sm.accuracy_score(y,Hclustering.labels_)


# In[ ]:





# coding: utf-8

# In[4]:

import numpy as np
import pandas as pd


import matplotlib.pyplot as plt
import pylab as plt
import seaborn as sb
from IPython.display import Image
from IPython.core.display import HTML
from pylab import rcParams


import sklearn
from sklearn import decomposition
from sklearn.decomposition import PCA
from sklearn import datasets


# In[5]:

get_ipython().magic('matplotlib inline')
rcParams['figure.figsize']=5,4
sb.set_style('whitegrid')



# # PCA on the iris dataset

# In[6]:

iris=datasets.load_iris()
x=iris.data
variable_names=iris.feature_names
x[0:10,]


# In[7]:

pca=decomposition.PCA()
iris_pcs=pca.fit_transform(x)

pca.explained_variance_ratio_


# In[9]:

pca.explained_variance_ratio_.sum()


# In[11]:

comps=pd.DataFrame(pca.components_,columns=variable_names)
comps


# In[12]:

sb.heatmap(comps)


# In[ ]:




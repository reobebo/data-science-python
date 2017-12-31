
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd

import sklearn
from sklearn.decomposition import FactorAnalysis

from sklearn import datasets


# # Factor analysis on iris dataset

# In[5]:

iris =  datasets.load_iris()
   

x=iris.data

variable_names=iris.feature_names

x[0:10,]


# In[6]:

factor=FactorAnalysis().fit(x)

pd.DataFrame(factor.components_,columns=variable_names)


# In[ ]:




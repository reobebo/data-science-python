
# coding: utf-8

# In[11]:

import numpy as np
import pandas as pd

from pandas import Series, DataFrame


# In[13]:

series_obj=Series(np.arange(8),index=['row 1','row 2','row 3','row 4','row 5', 'row 6','row 7','row 8'])
series_obj


# In[14]:

series_obj['row 7']


# In[16]:

series_obj[[0,7]]


# In[17]:

np.random.seed(25)
DF_obj = DataFrame(np.random.rand(36).reshape((6,6)),index=['row 1','row 2','row 3','row 4','row 5', 'row 6'],
                   columns=['column 1','column 2','column 3','column 4','column 5','column 6'])
DF_obj


# In[18]:

DF_obj.ix[['row 2', 'row 5'],['column 5','column 2']]


# # Data Slicing

# In[19]:

#data slicing allows you to select and retrieve all records from the starting label-index,
#to the ending label-index and every record in between

series_obj['row 3':'row 7']


# # Comparing with scalars

# In[20]:

#you use scalar values for indexing, to return only the 
#records that satisfy the comparison you write.
DF_obj<.2


# # Filtering with scalars

# In[21]:

series_obj[series_obj>6]


# # Setting values with scalars

# In[22]:

#selecting records associated with the specified label-indexes
# and set those values equal to a scalar
series_obj['row 1','row 5','row 8']=8
series_obj


# In[ ]:




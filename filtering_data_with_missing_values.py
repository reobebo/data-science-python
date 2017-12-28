
# coding: utf-8

# In[4]:

import numpy as np
import pandas as pd

from pandas import Series, DataFrame


# In[6]:

missing = np.nan
series_obj=Series(['row 1','row 2',missing,'row 4','row 5','row 6',missing,'row 8'])
series_obj


# In[7]:

series_obj.isnull()


# # Filling in for missing values

# In[10]:

np.random.seed(25)
DF_obj = DataFrame(np.random.randn(36).reshape(6,6))
DF_obj


# In[12]:

DF_obj.ix[3:5,0]=missing
DF_obj.ix[1:4,5]=missing
DF_obj


# In[13]:

#filling method finds each missing value from within a Pandas
#object and fills it with the numeric value you passed in
filled_DF=DF_obj.fillna(0)
filled_DF


# In[14]:

#you can pass dictionary into the .fillna() method and will
#fill the missing values from each colum series with its own
#unique values
filled_DF=DF_obj.fillna({0:0.1,5:1.25})
filled_DF


# In[15]:

fill_DF=DF_obj.fillna(method='ffill')
fill_DF


# # Counting missing values 

# In[16]:

np.random.seed(25)
DF_obj = DataFrame(np.random.randn(36).reshape(6,6))
DF_obj.ix[3:5,0]=missing
DF_obj.ix[1:4,5]=missing
DF_obj


# In[17]:

#get a count of how many values are missing from the dataset
DF_obj.isnull().sum()


# # Filtering missing values

# In[20]:

#drops all rows from a dataframe that contains missing values
DF_no_NaN=DF_obj.dropna(axis=1)
DF_no_NaN


# In[21]:

#will drop rows from a dataframe that contain all missing values
DF_obj.dropna(how='all')


# In[ ]:




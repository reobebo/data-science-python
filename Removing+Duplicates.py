
# coding: utf-8

# In[12]:

import numpy as np
import pandas as pd

from pandas import Series,DataFrame


# # Removing duplicates

# In[13]:

DF_obj=DataFrame({'column 1':[1,1,2,2,3,3,3],
                  'column 2':['a','a','b','b','c','c','c'],
                  'column 3':['A','A','B','B','C','C','C']})
DF_obj


# In[14]:

#the duplicated() method searches each row in the DataFrame
#and returns true or false
DF_obj.duplicated()


# In[15]:

#drop_duplicates() method drops duplicates
DF_obj.drop_duplicates()


# In[16]:

DF_obj=DataFrame({'column 1':[1,1,2,2,3,3,3],
                  'column 2':['a','a','b','b','c','c','c'],
                  'column 3':['A','A','B','B','C','D','C']})
DF_obj


# In[17]:

DF_obj.drop_duplicates(['column 3'])


# In[ ]:




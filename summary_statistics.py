
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import scipy
from scipy import stats


# In[2]:

address='/Users/Apple/Documents/Lynda/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv'
cars=pd.read_csv(address)

cars.columns=['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']
cars.head()


# # Looking at summary statistics that describe a variable's numeric values

# In[3]:

cars.sum()


# In[4]:

cars.sum(axis=1)


# In[5]:

cars.median()


# In[6]:

cars.mean()


# In[7]:

cars.max()


# In[8]:

mpg=cars.mpg
mpg.idxmax()


# # Looking at summary statistics that describe variable distribution

# In[9]:

cars.std()


# In[10]:

cars.var()


# In[12]:

gear=cars.gear
gear.value_counts()


# In[13]:

cars.describe()


# In[ ]:




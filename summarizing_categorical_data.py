
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd


# # The basics
# 

# In[2]:

address='/Users/Apple/Documents/Lynda/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv'
cars=pd.read_csv(address)
cars.columns=['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']
cars.index=cars.car_names
cars.head(15)


# In[3]:

carb=cars.carb
carb.value_counts()


# In[4]:

cars_cat=cars[['cyl','vs','am','gear','carb']]
cars_cat.head()


# In[5]:

gears_group=cars_cat.groupby('gear')
gears_group.describe()


# # Transforming variables to catagorical data type

# In[6]:

cars['group']=pd.Series(cars.gear,dtype='category')


# In[7]:

cars['group'].dtypes


# In[8]:

cars['group'].value_counts()


# # Describe categorical data with crosstabs

# In[10]:

pd.crosstab(cars['am'], cars['gear'])


# In[ ]:




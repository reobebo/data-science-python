
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd

from pandas import Series,DataFrame


# In[3]:

address='/Users/Apple/Documents/Lynda/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv'
cars=pd.read_csv(address)

cars.columns=['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']
cars.head()


# In[5]:

# to group a dataframe by its values in a particular column
# call the .groupby() method off of the dataframe
cars_groups=cars.groupby(cars['cyl'])
cars_groups.mean()


# In[ ]:




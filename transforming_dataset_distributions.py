
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
import scipy

import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sb

import sklearn
from sklearn import preprocessing
from sklearn.preprocessing import scale


# In[4]:

get_ipython().magic('matplotlib inline')
rcParams['figure.figsize']=5,4
sb.set_style('whitegrid')


# # Normalizing and transforming features withMinMacScalar() and fit_transform
# 

# In[5]:

address='/Users/Apple/Documents/Lynda/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv'
cars=pd.read_csv(address)
cars.columns=['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']


# In[6]:

mpg=cars.mpg
plt.plot(mpg)


# In[9]:

cars[['mpg']].describe()


# In[10]:

mpg_matrix=mpg.reshape(-1,1)
scaled=preprocessing.MinMaxScaler(feature_range=[0,10])
scaled_mpg=scaled.fit_transform(mpg_matrix)
plt.plot(scaled_mpg)


# # Using scale() to scale your features
# 

# In[14]:

standardized_mpg=scale(mpg,axis=0,with_mean=False, with_std=False)
plt.plot(standardized_mpg)


# In[15]:

standardized_mpg=scale(mpg)
plt.plot(standardized_mpg)


# In[ ]:




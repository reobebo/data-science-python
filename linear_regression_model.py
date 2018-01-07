
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import scale
from collections import Counter


# In[3]:

get_ipython().magic('matplotlib inline')
rcParams['figure.figsize']=5,4
sb.set_style('whitegrid')


# # (Multiple) linear regression on the enrollment data

# In[4]:

address='/Users/Apple/Documents/Lynda/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch08/08_01/enrollment_forecast.csv'

enroll= pd.read_csv(address)
enroll.columns=['year','roll','unem','hgrad','inc']
enroll.head()


# In[5]:

sb.pairplot(enroll)


# In[7]:

print (enroll.corr())


# In[10]:

enroll_data=enroll.ix[:,(2,3)].values
enroll_target=enroll.ix[:,1].values
enroll_data_names=['unem','hgrad']

x,y= scale(enroll_data), enroll_target


# # Checking for missing values

# In[11]:

missing_values= x==np.NAN
x[missing_values==True]


# In[13]:

LinReg=LinearRegression(normalize=True)
LinReg.fit(x,y)

print (LinReg.score(x,y))


# In[ ]:





# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import scipy
from scipy.stats import spearmanr

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

import sklearn 
from sklearn.preprocessing import scale
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
from sklearn import preprocessing


# In[2]:

get_ipython().magic('matplotlib inline')
rcParams['figure.figsize']=5,4
sb.set_style('whitegrid')


# # Logistic regression on mtcars

# In[3]:

address='/Users/Apple/Documents/Lynda/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv'
cars=pd.read_csv(address)
cars.columns=['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']
cars.head()


# In[4]:

cars_data = cars.ix[:,(5,11)].values
cars_data_names=['drat','carb']

y=cars.ix[:,9].values


# # Checking for independence between features

# In[5]:

sb.regplot(x='drat',y='carb',data=cars,scatter=True)


# In[6]:

drat=cars['drat']
carb=cars['carb']

spearmanr_coefficient, p_value= spearmanr(drat,carb)
print ('Spearman Rank Correlation Coefficient %0.3f' % spearmanr_coefficient)


# # Checking for missing values

# In[7]:

cars.isnull().sum()


# # Checking that your target is binary or ordinal

# In[8]:

sb.countplot(x='am',data=cars,palette='hls')


# # Checking that your dataset is sufficient 

# In[9]:

cars.info()


# # Deploying and evaluating your model

# In[10]:

x=scale(cars_data)


# In[11]:

LogReg=LogisticRegression()

LogReg.fit(x,y)

print(LogReg.score(x,y))


# In[13]:

y_pred=LogReg.predict(x)
from sklearn.metrics import classification_report
print(classification_report(y,y_pred))


# In[ ]:




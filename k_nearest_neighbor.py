
# coding: utf-8

# In[4]:

import numpy as np
import pandas as pd
import scipy

import matplotlib.pyplot as plt
from pylab import rcParams

import urllib

import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn import neighbors
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import metrics


# In[5]:

np.set_printoptions(precision=4, suppress=True)
get_ipython().magic('matplotlib inline')
rcParams['figure.figsize']=7,4
plt.style.use('seaborn-whitegrid')


# # Splitting your data into test and training datasets
# 

# In[8]:

address='/Users/Apple/Documents/Lynda/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv'
cars=pd.read_csv(address)
cars.columns=['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

x_prime = cars.ix[:,(1,3,4,6)].values

y= cars.ix[:,9].values


# In[9]:

x=preprocessing.scale(x_prime)


# In[10]:

x_train,x_test,y_train,y_test=train_test_split(x,y, test_size=.33, random_state=17)


# # Building and training your model with training data

# In[11]:

clf=neighbors.KNeighborsClassifier()

clf.fit(x_train,y_train)
print(clf)


# # Evaluating your model's predictions against the test dataset

# In[14]:

y_expect=y_test
y_pred=clf.predict(x_test)

metrics.classification_report(y_expect,y_pred)


# In[ ]:




# In[ ]:




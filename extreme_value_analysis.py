
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from pylab import rcParams


# In[2]:

get_ipython().magic('matplotlib inline')
rcParams['figure.figsize']=5,4


# In[4]:

df = pd.read_csv(
    filepath_or_buffer='/Users/Apple/Documents/Lynda/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch05/05_01/iris.data.csv',
    header=None,
    sep=',')
df.columns=['Sepal Length','Sepal Width','Petal Length','Petal Width','Species']
x=df.ix[:,0:4].values
y=df.ix[:,4].values

df[:5]


# # Identifying outliers from Tukey boxplots

# In[5]:

df.boxplot(return_type='dict')
plt.plot()


# In[6]:

Sepal_Width = x[:,1]
iris_outliers = (Sepal_Width>4)
df[iris_outliers]


# In[8]:

Sepal_Width = x[:,1]
iris_outliers = (Sepal_Width<2.05)
df[iris_outliers]


# # Applying Tukey outlier labeling

# In[10]:

pd.options.display.float_format='{:.1f}'.format
x_df = pd.DataFrame(x)
x_df.describe()


# In[ ]:




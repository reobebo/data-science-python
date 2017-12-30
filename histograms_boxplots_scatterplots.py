
# coding: utf-8

# In[2]:

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb


# In[5]:

get_ipython().magic('matplotlib inline')
rcParams['figure.figsize']=5,4
sb.set_style('whitegrid')


# # Eyeballing dataset distributions with histograms

# In[6]:

address='/Users/Apple/Documents/Lynda/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv'
cars=pd.read_csv(address)
cars.columns=['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']
cars.index=cars.car_names
mpg=cars['mpg']
mpg.plot(kind='hist')


# In[7]:

plt.hist(mpg)
plt.plot()


# In[8]:

sb.distplot(mpg)


# # Seeing scatterplots in action

# In[10]:

cars.plot(kind='scatter', x='hp',y='mpg',c=['darkgray'],s=150)


# In[11]:

sb.regplot( x='hp',y='mpg',data=cars,scatter=True)


# # Generating a scatter plot matrix
# 

# In[12]:

sb.pairplot(cars)


# In[13]:

cars_df=pd.DataFrame((cars.ix[:,(1,3,4,6)].values),columns=['mpg','disp','hp','wt'])
cars_target=cars.ix[:,9].values
target_names=[0,1]

cars_df['group']=pd.Series(cars_target,dtype='category')
sb.pairplot(cars_df,hue='group',palette='hls')


# # Building boxplots

# In[14]:

cars.boxplot(column='mpg',by='am')
cars.boxplot(column='wt',by='am')


# In[15]:

sb.boxplot(x='am',y='mpg',data=cars,palette='hls')


# In[ ]:




# In[ ]:




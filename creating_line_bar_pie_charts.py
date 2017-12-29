
# coding: utf-8

# In[1]:

get_ipython().system(' pip install Seaborn')


# In[2]:

import numpy as np 
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sb


# In[3]:

get_ipython().magic('matplotlib inline')
rcParams['figure.figsize']=5,4
sb.set_style('whitegrid')


# # Plotting a line chart in matplotlib

# In[4]:

x=range(1,10)
y=[1,2,3,4,0,4,3,2,1]
plt.plot(x,y)


# # Plotting a line chart from a Pandas object

# In[5]:

address='/Users/Apple/Documents/Lynda/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv'
cars=pd.read_csv(address)
cars.columns=['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']
mpg=cars['mpg']


# In[6]:

mpg.plot()


# In[8]:

df=cars[['cyl','wt','mpg']]
df.plot()


# # Creating bar charts
# # Creating a bar chart from a list

# In[9]:

plt.bar(x,y)


# # Creating bar charts from Pandas objects

# In[10]:

mpg.plot(kind='bar')


# In[11]:

mpg.plot(kind="barh")


# # Create a pie chart

# In[12]:

x=[1,2,3,4,0.5]
plt.pie(x)
plt.show


# In[14]:

plt.savefig('pie_chart.jpeg')
plt.show()


# In[15]:

get_ipython().magic('pwd')


# In[ ]:




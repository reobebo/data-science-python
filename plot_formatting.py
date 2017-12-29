
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
from pylab import rcParams

import seaborn as sb


# In[2]:

get_ipython().magic('matplotlib inline')
rcParams['figure.figsize']=5,4
sb.set_style('whitegrid')


# In[3]:

x=range(1,10)
y=[1,2,3,4,0.5,4,3,2,1]

plt.bar(x,y)


# In[4]:

wide=[0.5,0.5,0.5,0.9,0.9,0.9,0.5,0.5,0.5]
color=['salmon']
plt.bar(x,y,width=wide,color=color,align='center')


# In[5]:

address='/Users/Apple/Documents/Lynda/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv'
cars=pd.read_csv(address)

cars.columns=['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']
df=cars[['cyl','mpg','wt']]
df.plot()


# In[6]:

color_theme=['darkgray','lightsalmon','powderblue']
df.plot(color=color_theme)


# In[7]:

z=[1,2,3,4,0.5]
plt.pie(z)
plt.show()


# In[11]:

color_theme=['#A9A9A9','#FFA07A','#B0E0E6','#FFE4C4','#BDB76B']
plt.pie(z,colors=color_theme)
plt.show()


# # Customizing lin styles

# In[12]:

x1=range(0,10)
y1=[10,9,8,7,6,5,4,3,2,1]

plt.plot(x,y)
plt.plot(x1,y1)


# In[13]:

plt.plot(x,y, ls='steps',lw=5)
plt.plot(x1,y1,ls='--',lw=10)


# # Setting plot markers

# In[14]:

plt.plot(x,y,marker='1', mew=20)
plt.plot(x1,y1, marker='+',mew=15)


# In[ ]:




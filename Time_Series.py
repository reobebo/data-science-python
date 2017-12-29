
# coding: utf-8

# In[2]:

import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb


# In[3]:

get_ipython().magic('matplotlib inline')
rcParams['figure.figsize']=5,4
sb.set_style('whitegrid')


# # Simple time series plot

# In[19]:

address = '/Users/Apple/Desktop/Superstore-Sales copy.csv'
df = pd.read_csv(address, encoding = "ISO-8859-1",index_col='Order Date', parse_dates=False)
df.head()


# In[21]:

df['Order Quantity'].plot()


# In[24]:

df2=df.sample(n=100,random_state=25,axis=0)
plt.xlabel('Order Date')
plt.ylabel('Order Quantity')
plt.title('Superstore Sales')

df2['Order Quantity'].plot()


# In[ ]:




# In[ ]:




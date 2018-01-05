
# coding: utf-8

# In[3]:

import pandas as pd
import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb


# In[4]:

get_ipython().magic('matplotlib inline')
rcParams['figure.figsize']=5,4
sb.set_style('whitegrid')


# In[ ]:

df = pd.read_csv(
    filepath_or_buffer='/Users/Apple/Documents/Lynda/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch05/05_01/iris.data.csv',
    header=None,
    sep=',')
df.columns=['Sepal Length','Sepal Width','Petal Length','Petal Width','Species']
x=df.ix[:,0:4].values
y=df.ix[:,4].values

df[:5]

sb.boxplot(x='Species',y='Sepal Length', data=df, palette='hls')


# # Looking at the scatterplot matrix

# In[7]:

sb.pairplot(df,hue='Species',palette='hls')


# In[ ]:




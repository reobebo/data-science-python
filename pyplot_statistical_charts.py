
# coding: utf-8

# In[41]:

import numpy as np
import pandas as pd

import cufflinks as cf

import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go

import sklearn
from sklearn.preprocessing import StandardScaler

tls.set_credentials_file(username='reobebo', api_key='Pm4NwqHqNibankYtWsMn')


# # Creating histograms

# ### Make a histogram from a pandas series object

# In[42]:

address='/Users/Apple/Documents/Lynda/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv'
cars=pd.read_csv(address)
cars.columns=['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

mpg=cars.mpg

mpg.iplot(kind='histogram', filename='simple-histogram-chart')


# In[44]:

cars_data = cars.ix[:,(1,3,4)].values

cars_data_std = StandardScaler().fit_transform(cars_data)

cars_select = pd.DataFrame(cars_data_std)
cars_select.columns = ['mpg', 'disp', 'hp']

cars_select.iplot(kind='histogram', filename='multiple-histogram-chart')


# In[46]:

cars_select.iplot(kind='histogram', subplots=True, filename='subplot-histogram')


# In[47]:

cars_select.iplot(kind='histogram', subplots=True,shape=(3,1), filename='subplot-histogram')


# In[48]:

cars_select.iplot(kind='histogram', subplots=True,shape=(1,3), filename='subplot-histogram')


# # Creating box plots

# In[49]:

cars_select.iplot(kind='box', filename='box-plots')


# # Creating scatter plots

# In[50]:

fig={'data':[{'x':cars_select.mpg,'y':cars_select.disp, 'mode':'markers','name':'mpg'},
            {'x':cars_select.hp, 'y':cars_select.disp,'mode':'markers','name':'hp'}]
    , 'layout':{'xaxis':{'title':''},'yaxis':{'title':'Standardized Displacement'}}}

py.iplot(fig,filename='grouped-scatter-plot')


# In[ ]:




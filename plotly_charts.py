
# coding: utf-8

# In[1]:

get_ipython().system(' pip install Plotly')


# In[2]:

get_ipython().system(' pip install cufflinks')


# In[3]:

import numpy as np
import pandas as pd

import cufflinks as cf

import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go


# In[5]:

tls.set_credentials_file(username='reobebo', api_key='Pm4NwqHqNibankYtWsMn')


# # Creating line charts

# # A very basic line chart

# In[7]:

a=np.linspace(start=0,stop=36, num=36)
np.random.seed(25)
b=np.random.uniform(low=0.0,high=1.0,size=36)

trace=go.Scatter(x=a,y=b)

data=[trace]

py.iplot(data,filename='basic-line-chart')


# # A line chart with more than one variable plotted

# In[9]:

x=[1,2,3,4,5,6,7,8,9,10]
y=[1,2,3,4,0,4,3,2,1]
z=[10,9,8,7,6,5,4,3,2,1]

trace0=go.Scatter(x=x,y=y,name='List Object', line=dict(width=5))
trace1=go.Scatter(x=x,y=z,name='List Object 2', line=dict(width=10))

data=[trace0,trace1]

layout=dict(title='Double Line Chart',xaxis=dict(title='x-axis'),yaxis=dict(title='y-axis'))
print(layout)


# In[10]:

fig =dict(data=data,layout=layout)
print(fig)


# In[11]:

py.iplot(fig,filename='styled-line-chart')


# # A line chart from a pandas dataframe

# In[18]:

address='/Users/Apple/Documents/Lynda/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv'
cars=pd.read_csv(address)
cars.columns=['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']

df=cars[['cyl','wt','mpg']]

layout=dict(title='Chart from pandas DataFrame', xaxis=dict(title='x-axis'),yaxis=dict(title='y-axis'))
df.iplot(filename='cf-simple-line-chart',layout=layout)


# # Creating bar charts

# In[20]:

data=[go.Bar(x=[1,2,3,4,5,6,7,8,9,10],y=[1,2,3,4,0.5,4,3,2,1])]
print (data)


# In[21]:

layout=dict(title='Simple Bar Chart', xaxis=dict(title='x-axis'), yaxis=dict(title='y-axis'))

py.iplot(data,filename='basic-bar-charts',layout=layout)


# In[22]:

color_theme = dict(color=['rgba(169,169,169,1)', 'rgba(255,160,122,1)','rgba(176,224,230,1)', 'rgba(255,228,196,1)',
                          'rgba(189,183,107,1)', 'rgba(188,143,143,1)','rgba(221,160,221,1)'])

print(color_theme)


# In[25]:

trace0=go.Bar(x=[1,2,3,4,5,6,7],y=[1,2,3,4,0.5,3,1], marker=color_theme)
data=[trace0]
layout=go.Layout(title='Custom Colors')
fig=go.Figure(data=data,layout=layout)

py.iplot(fig, filename='color-bar-chart')


# In[26]:

fig={'data':[{'labels':['bicycle','motorbike','car','van','stroller'],'values':[1,2,3,4,0.5],'type':'pie'}],
     'layout':{'title':'Simple Pie Charts'}}

py.iplot(fig)


# In[ ]:




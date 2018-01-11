
# coding: utf-8

# In[2]:

import numpy as np
import pandas as pd

import plotly.plotly as py
import plotly.tools as tls



# In[3]:

tls.set_credentials_file(username='reobebo', api_key='Pm4NwqHqNibankYtWsMn')


# # Generating Choropleth maps

# In[6]:

address='/Users/Apple/Documents/Lynda/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch09/09_03/States.csv'
states=pd.read_csv(address)
states.columns=['code','region','pop','satv','satm','percent','dollars','pay']


states.head()


# In[10]:

states['text']='SATv'+states['satv'].astype(str)+'SATm'+states['satm'].astype(str)+'<br>' + 'State ' +states['code']

data=[dict(type='choropleth',autocolorscale=False,locations=states['code'],z=states['dollars'],locationmode='USA-states',
          text=states['text'],colorscale='custome-colorscale', colorbar=dict(title='thousand dollars'))]

data


# In[17]:

layout=dict(title='State spending on Public Education in $k/student', geo = dict(scope='usa',projection=dict(type='albers usa'),showlakes=True,lakecolor='rgb(66,165,245)',),)
layout


# In[18]:

fig=dict(data=data, layout=layout)

py.iplot(fig,filename='d3-chororpleth-map')


# # Generating point maps

# In[21]:

address='/Users/Apple/Documents/Lynda/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch09/09_04/snow_inventory.csv'
snow=pd.read_csv(address)
snow.columns=['stn_id','lat','long','elev','code']

snow_sample=snow.sample(n=200,random_state=25,axis=0)

snow_sample.head()


# In[22]:

data=[dict(type='scattergeo', locationmode='USA-states', lon=snow_sample['long'], lat=snow_sample['lat'],
          marker=dict(size=12, autocolorscale=False, colorscale='custom-colorscale', color=snow_sample['elev'],
                     colorbar=dict(title='Elevation(m)')))]

layout=dict(title='NOAA Weather Snowfall Station Elevation', colorbar=True, geo=dict(scope='usa', projection=dict(type='albers usa'),
                                                                                    showland=True, landcolor='rgb(250,250,250)',
                                                                                    subunitcolor='rgb(217,217,217)', countrycolor='rgb(217,217,217)', countrywidth=0.5, subunitwidth=0.5))
fig=dict(data=data,layout=layout)

py.iplot(fig,validate=False, filename='d3-elevation')



# In[ ]:




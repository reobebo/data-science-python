
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb


# In[4]:

get_ipython().magic('matplotlib inline')
rcParams['figure.figsize']=8,4
sb.set_style('whitegrid')
             


# # Labeling plot features

# # The functional feature

# In[7]:

x= range(1,10)
y=[1,2,3,4,0.5,4,3,2,1]
plt.bar(x,y)

plt.xlabel('your x-axis label')
plt.ylabel('your y-axis label')


# In[9]:

z=[1,2,3,4,0.5]
veh_type=['bicycle','motorbike','car','van','stroller']
plt.pie(z,labels=veh_type)
plt.show()


# In[14]:

address='/Users/Apple/Documents/Lynda/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv'
cars=pd.read_csv(address)

cars.columns=['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']
mpg=cars.mpg
fig=plt.figure()
ax=fig.add_axes([.1,.1,1,1])

mpg.plot()

ax.set_xticks(range(32))

ax.set_xticklabels(cars.car_names,rotation=60,fontsize='medium')
ax.set_title('Miles per Gallon of Cars in mtcars')

ax.set_xlabel('car names')
ax.set_ylabel('miles/gal')


# # Adding a legend to your plot

# # The functional method

# In[15]:

plt.pie(z)
plt.legend(veh_type,loc='best')
plt.show()


# # The object-oriented method

# In[17]:

fig=plt.figure()
ax=fig.add_axes([.1,.1,1,1])
mpg.plot()

ax.set_xticks(range(32))

ax.set_xticklabels(cars.car_names,rotation=60,fontsize='medium')
ax.set_title('Miles per Gallon of Cars in mtcars')

ax.set_xlabel('car names')
ax.set_ylabel('miles/gal')

ax.legend(loc='best')


# # Annotating your plot

# In[18]:

mpg.max()


# In[21]:

fig=plt.figure()
ax=fig.add_axes([.1,.1,1,1])
mpg.plot()
ax.set_title('Miles per Gallon of Cars in mtcars')
ax.set_ylabel('miles/gal')

ax.set_ylim([0,45])

ax.annotate('Toyota Corolla',xy=(19,33.9), xytext=(21,35),
            arrowprops=dict(facecolor='black',shrink=0.05))


# In[ ]:





# coding: utf-8

# In[3]:

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sb
from pylab import rcParams

import scipy
from scipy.stats.stats import pearsonr


# In[4]:

address='/Users/Apple/Documents/Lynda/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv'
cars=pd.read_csv(address)
cars.columns=['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']


# In[10]:

sb.pairplot(cars)
plt.show()


# In[9]:

x=cars[['mpg','hp','qsec','wt']]
sb.pairplot(x)
plt.show()


# # Using scipy to calculate Pearson correlation coefficient

# In[13]:

mpg=cars['mpg']
hp=cars['hp']
qsec=cars['qsec']
wt=cars['wt']

pearsonr_coefficient,p_value=pearsonr(mpg,hp)
print (pearsonr_coefficient) 


# In[14]:

pearsonr_coefficient,p_value=pearsonr(mpg,qsec)
print (pearsonr_coefficient) 


# In[15]:

pearsonr_coefficient,p_value=pearsonr(mpg,wt)
print (pearsonr_coefficient) 


# # Using pandas to calculate the Pearson correlation  coefficient

# In[16]:

corr =x.corr()
corr


# # Using Seaborn to visualize the Pearson correlation coefficient

# In[18]:

sb.heatmap(corr,xticklabels=corr.columns.values,yticklabels=corr.columns.values)
plt.show()


# In[ ]:




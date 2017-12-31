
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sb
from pylab import rcParams

import scipy 
from scipy.stats import spearmanr


# In[3]:

get_ipython().magic('matplotlib inline')
rcParams['figure.figsize']=14,7
plt.style.use('seaborn-whitegrid')


# In[4]:

address='/Users/Apple/Documents/Lynda/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch01/01_05/mtcars.csv'
cars=pd.read_csv(address)
cars.columns=['car_names','mpg','cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']
cars.head()


# In[5]:

sb.pairplot(cars)


# In[6]:

x=cars[['cyl','vs','am','gear']]
sb.pairplot(x)


# In[8]:

cyl=cars['cyl']
vs=cars['vs']
am=cars['am']
gear=cars['gear']
spearmanr_coefficient, p_value = spearmanr(cyl,vs)
print(spearmanr_coefficient)


# In[9]:

spearmanr_coefficient, p_value = spearmanr(cyl,am)
print(spearmanr_coefficient)


# In[10]:

spearmanr_coefficient, p_value = spearmanr(cyl,gear)
print(spearmanr_coefficient)


# # Chi-square test for independence

# In[11]:

table=pd.crosstab(cyl,am)

from scipy.stats import chi2_contingency
chi2,p,dof,expected= chi2_contingency(table.values)
print (chi2,p)


# In[12]:

table=pd.crosstab(cars['cyl'],cars['vs'])

chi2,p,dof,expected= chi2_contingency(table.values)
print (chi2,p)


# In[13]:

table=pd.crosstab(cars['cyl'],cars['gear'])

chi2,p,dof,expected= chi2_contingency(table.values)
print (chi2,p)


# In[ ]:




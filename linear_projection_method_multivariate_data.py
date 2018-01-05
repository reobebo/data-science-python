
# coding: utf-8

# In[1]:

import pandas as pd
import matplotlib.pyplot as plt
from pylab import rcParams
import seaborn as sb

import sklearn
from sklearn.cluster import DBSCAN
from collections import Counter


# In[2]:

get_ipython().magic('matplotlib inline')
rcParams['figure.figsize']=5,4
sb.set_style('whitegrid')


# # DBSCan clustering to identify outliers

# # Train your model and identify outliers

# In[10]:

df = pd.read_csv(
    filepath_or_buffer='/Users/Apple/Documents/Lynda/Ex_Files_Python_Data_Science_EssT/Exercise Files/Ch05/05_01/iris.data.csv',
    header=None,
    sep=',')
df.columns=['Sepal Length','Sepal Width','Petal Length','Petal Width','Species']
data=df.ix[:,0:4].values
target=df.ix[:,4].values

df[:5]


# In[11]:

model= DBSCAN(eps=0.8,min_samples=19).fit(data)
print (model)


# # Visualize your results

# In[15]:

outliers_df=pd.DataFrame(data)

print( Counter(model.labels_))

print (outliers_df[model.labels_==-1])


# In[20]:

fig=plt.figure()
ax=fig.add_axes([.1,.1,1,1])
colors=model.labels_
ax.scatter(data[:,2],data[:,1],c=colors,s=120)
ax.set_xlabel('Petal Length')
ax.set_ylabel('Sepal Width')
plt.title('DBSCAN for Outlier Detection')


# In[ ]:




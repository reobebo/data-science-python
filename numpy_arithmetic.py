
# coding: utf-8

# In[1]:

import numpy as np
from numpy.random import randn


# In[2]:

np.set_printoptions(precision=2)


# # Creating arrays

# # Creating arrays using a list

# In[3]:

a=np.array([1,2,3,4,5,6])
a


# In[5]:

b=np.array([[10,20,30],[40,50,60]])
b


# # Creating arrays via assignment

# In[6]:

np.random.seed(25)
c=36*np.random.randn(6)
c


# In[7]:

d=np.arange(1,35)
d


# # Performing arthimetic on arrays

# In[8]:

a*10


# In[9]:

c+a


# In[10]:

c-a


# In[11]:

c*a


# In[12]:

c/a


# # Multiplying matrices and basic linear algebra

# In[13]:

aa=np.array([[2.,4.,6.],[1.,3.,5.],[10.,20.,30.]])
aa


# In[14]:

bb=np.array([[0.,1.,2.],[3.,4.,5.],[6.,7.,8.]])
bb


# In[15]:

aa*bb


# In[16]:

np.dot(aa,bb)


# In[ ]:





# coding: utf-8

# In[20]:

from bs4 import BeautifulSoup


# In[21]:

soup= BeautifulSoup('<b body="description">Product Description</b>')


# # NavigableString objects

# In[22]:

tag=soup.b
type(tag)


# In[23]:

tag.name


# In[24]:

tag.string


# In[25]:

type(tag.string)


# In[26]:

nav_string=tag.string
nav_string


# In[27]:

nav_string.replace_with('Null')
tag.string


# # Working with NavigableString Objects

# In[29]:

html_doc='''
<html><head><title>Best Books</title></head>
<body>
<p class='title'><b>DATA SCIENCE FOR DUMMIES</b></p>

<p class='description'>Jobs in data science abound, but few people have the data science skills needed to fill these increasingly important roles in organizations. Data Science For Dummies is the pe
<br><br>
Edition 1 of this book:
        <br>
 <ul>
  <li>Provides a background in data science fundamentals before moving on to working with relational databases and unstructured data and preparing your data for analysis</li>
  <li>Details different data visualization techniques that can be used to showcase and summarize your data</li>
  <li>Explains both supervised and unsupervised machine learning, including regression, model validation, and clustering techniques</li>
  <li>Includes coverage of big data processing tools like MapReduce, Hadoop, Storm, and Spark</li>   
  </ul>
<br><br>
What to do next:
<br>
<a href='http://www.data-mania.com/blog/books-by-lillian-pierson/' class = 'preview' id='link 1'>See a preview of the book</a>,
<a href='http://www.data-mania.com/blog/data-science-for-dummies-answers-what-is-data-science/' class = 'preview' id='link 2'>get the free pdf download,</a> and then
<a href='http://bit.ly/Data-Science-For-Dummies' class = 'preview' id='link 3'>buy the book!</a> 
</p>

<p class='description'>...</p>
'''

soup = BeautifulSoup(html_doc,'html.parser')


# In[31]:

for string in soup.stripped_strings: print((repr(string)))


# In[32]:

title_tag=soup.title
title_tag


# In[33]:

title_tag.parent


# In[34]:

title_tag.string


# In[35]:

title_tag.string.parent


# In[ ]:




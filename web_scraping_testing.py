
# coding: utf-8

# In[6]:

get_ipython().system(' conda install beautifulsoup4')


# In[7]:

from bs4 import BeautifulSoup


# # The BeautifulSoup object

# In[8]:

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


# In[10]:

soup=BeautifulSoup(html_doc,'html.parser')
print(soup)


# In[11]:

print (soup.prettify()[0:350])


# # Tag objects

# ## Working with names

# In[12]:

soup= BeautifulSoup('<b body="description">Product Description</b>','html')

tag=soup.b
type(tag)


# In[13]:

print (tag)


# In[16]:

tag.name


# In[17]:

tag.name='bestbooks'
tag


# In[18]:

tag.name


# # Working with attributes

# In[19]:

tag['body']


# In[20]:

tag.attrs


# In[21]:

tag['id']=3
tag.attrs


# In[22]:

tag


# In[23]:

del tag['body']
del tag['id']
tag


# In[24]:

tag.attrs


# # Using tags to navigate a tree

# In[25]:

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

soup=BeautifulSoup(html_doc, 'html.parser')


# In[26]:

soup.head


# In[27]:

soup.title


# In[28]:

soup.body.b


# In[29]:

soup.body


# In[30]:

soup.ul


# In[31]:

soup.a


# In[ ]:




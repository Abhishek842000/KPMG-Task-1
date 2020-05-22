#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


get_ipython().system('pip install xlrd')


# In[3]:


df = pd.read_excel('Downloads//KPMG_VI_New_raw_data_update_final (1).xlsx',sheet_name='Transactions')


# In[4]:


df.head()


# In[5]:


df.columns = ['Transaction id','Product id','Customer id','Transaction date','online order','order status','brand','product line','product class','product size','list price','standard cost','product first sold date']


# In[6]:


# The dataset might contain duplicate rows of data, we have to find and remove them


# In[7]:


df.duplicated().sum()


# In[8]:


# The dataset does not contain any duplicate values


# In[9]:


# Checking for incomplete data


# In[10]:


df.isnull()


# In[11]:


df.isnull().sum()


# In[12]:


df = pd.read_excel('Downloads//KPMG_VI_New_raw_data_update_final (1).xlsx',sheet_name='NewCustomerList')


# In[13]:


df.tail()


# In[14]:


df.duplicated().sum()


# In[15]:


df.isnull()


# In[16]:


df.isnull().sum()


# In[17]:


df.gender.value_counts()


# In[18]:


df.owns_car.value_counts()


# In[19]:


df = pd.read_excel('Downloads//KPMG_VI_New_raw_data_update_final (1).xlsx',sheet_name='CustomerDemographic')


# In[20]:


df.head()


# In[21]:


df.duplicated().sum()


# In[22]:


df.isnull().sum()


# In[23]:


df.gender.value_counts()


# In[24]:


df = df.replace(to_replace = ["F","Femal"],value = "Female")


# In[25]:


df = df.replace(to_replace = "M",value = "Male")


# In[26]:


df.head()


# In[27]:


df.owns_car.value_counts()


# In[28]:


df.deceased_indicator.value_counts()


# In[29]:


df = pd.read_excel('Downloads//KPMG_VI_New_raw_data_update_final (1).xlsx',sheet_name='CustomerAddress')


# In[30]:


df.head()


# In[31]:


df.duplicated().sum()


# In[32]:


df.isnull().sum()


# In[33]:


df.country.value_counts()


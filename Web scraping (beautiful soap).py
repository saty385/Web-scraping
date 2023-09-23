#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install Bs4')
get_ipython().system('pip install requests')


# In[8]:


from bs4 import BeautifulSoup
import requests


# In[10]:


page = requests.get('https://www.dineout.co.in/delhi-restaurants')


# In[11]:


page


# In[12]:


soup = BeautifulSoup(page.content)


# In[13]:


soup


# In[14]:


first_tittle =soup.find('div',class_='restnt-info cursor')


# In[15]:


first_tittle


# In[16]:


first_tittle.text


# In[17]:


loc =soup.find('div',class_="restnt-loc ellipsis")


# In[19]:


loc


# In[20]:


loc.text


# In[21]:


sta = soup.find('span',class_="double-line-ellipsis")


# In[22]:


sta.text


# In[31]:


tittles=[]


for i in soup.find_all('div',class_="restnt-info cursor"):
    tittles.append(i.text)
    
   


# In[33]:


tittles


# In[36]:


location =[]
for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    location.append(i.text)


# In[37]:


location


# In[49]:


price=[]

for i in soup.find_all('span',class_="double-line-ellipsis"):
    price.append(i.text)
   


# In[50]:


price


# In[60]:


images =[]
for i in soup.find_all('img',class_="no-img"):
    images.append(i['data-src'])
    images


# In[61]:


images


# In[63]:


print(len(tittles),len(location),len(price),len(images))


# In[66]:


import pandas as pd
df = pd.DataFrame({'Tittles':tittles,'Location':location,'Price':price,'Images_Url':images})
df


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# Question 1.1

# In[1]:


from bs4 import BeautifulSoup
import urllib.request


# In[2]:


seed_url = "https://www.federalreserve.gov/newsevents/pressreleases.htm"
seed_url1= "https://www.federalreserve.gov/newsevents/pressreleases"


# In[3]:


urls = [seed_url]
seen = [seed_url]
opened = []
qualified = [] # pages that contain the word "covid"


# In[4]:


maxNumUrl = 10


# In[5]:


while len(urls) > 0 and len(qualified) < maxNumUrl:
    try:
        curr_url=urls.pop(0)
        req = urllib.request.Request(curr_url,headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urllib.request.urlopen(req).read()
        opened.append(curr_url)

    except Exception as ex:
        print("Unable to access= "+curr_url)
        print(ex)
        continue

    soup = BeautifulSoup(webpage)
        
    for tag in soup.find_all('a', href = True):
        childUrl = tag['href']
        o_childurl = childUrl
        childUrl = urllib.parse.urljoin(seed_url, childUrl)

        if seed_url1 in childUrl and childUrl not in seen:
            urls.append(childUrl)
            seen.append(childUrl)
            
            req1 = urllib.request.Request(childUrl,headers={'User-Agent': 'Mozilla/5.0'})
            webpage1 = urllib.request.urlopen(req1).read()
            soup1 = BeautifulSoup(webpage1)
            text = soup1.get_text()
            if 'covid' in str(text).lower():
                qualified.append(childUrl)


# In[6]:


print("num. of URLs seen = %d, scanned = %d, and contain the word 'covid' = %d" %(len(seen), len(opened),len(qualified)))


# In[7]:


print("List of qualified URLs:")
for qualified_url in qualified:
    print(qualified_url)


# Question 1.2

# In[8]:


seed_url = "https://www.sec.gov/news/pressreleases"
seed_url1= "https://www.sec.gov/news/press-release"


# In[9]:


urls = [seed_url]
seen = [seed_url]
opened = []
qualified = {} # pages that contain the word "charges"


# In[10]:


maxNumUrl = 20


# In[11]:


while len(urls) > 0 and len(qualified) < maxNumUrl:
    try:
        curr_url=urls.pop(0)
        req = urllib.request.Request(curr_url,headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urllib.request.urlopen(req).read()
        opened.append(curr_url)

    except Exception as ex:
        print("Unable to access= "+curr_url)
        print(ex)
        continue

    soup = BeautifulSoup(webpage)
        
    for tag in soup.find_all('a', href = True):
        childUrl = tag['href']
        o_childurl = childUrl
        childUrl = urllib.parse.urljoin(seed_url, childUrl)

        if seed_url1 in childUrl and childUrl not in seen:
            urls.append(childUrl)
            seen.append(childUrl)
            
            req1 = urllib.request.Request(childUrl,headers={'User-Agent': 'Mozilla/5.0'})
            webpage1 = urllib.request.urlopen(req1).read()
            soup1 = BeautifulSoup(webpage1)
            text = soup1.get_text()
            if 'charges' in str(text).lower():
                qualified[childUrl]= text
            
            if len(qualified) == maxNumUrl:
                break


# In[12]:


print("num. of URLs seen = %d, scanned = %d, and contain the word 'charges' = %d" %(len(seen), len(opened),len(qualified)))


# In[13]:


print("List of qualified URLs:")
for qualified_url in qualified:
    print(qualified_url)


# In[14]:


print("List and text of qualified URLs:")
for qualified_url, qualified_text in qualified.items():
    print(qualified_url,qualified_text)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install demoji


# In[2]:


import demoji
demoji.download_codes


# In[3]:


import demoji
text = """Today is a ☀️day. It was 🌧️☔ yesterday. As the🌞 is out. I'm planning go to🏖️, swim in 🌊 and find 🐚."""
demoji.findall(text)


# In[ ]:





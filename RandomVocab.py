#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize


# In[2]:


pdf = pd.read_pickle('thehindu_vocab-bz2.pkl',compression='bz2')


# In[13]:


for i in  range(42):
    if(pdf['Word'].loc[i] == "Rollback"):
        print("found")


# In[14]:


bool_series = pdf["Word"].duplicated()


# In[15]:


pdf[bool_series]


# In[29]:


from flask import Flask
import random
app = Flask(__name__)


# In[30]:


@app.route('/')
def hello_world():
   # msg = "hello World"
    rand_idx = random.choice(range(300))
    msg = pdf['Word'].loc[rand_idx]
    msg += " : "
    msg += pdf['Meaning & Synonym'].loc[rand_idx]
    return msg
if __name__ == '__main__':
    app.run()


# In[28]:


del app


# In[ ]:





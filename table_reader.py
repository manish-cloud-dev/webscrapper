#!/usr/bin/env python
# coding: utf-8

# In[27]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize

table_MN = pd.read_html('https://www.oliveboard.in/blog/hindu-vocabulary-pdf-download/#Daily_Hindu_Vocabulary_2022')


# In[61]:


len(table_MN)


# In[62]:


table_MN[2].info()
pmn = table_MN


# In[78]:


pmn[0]


# In[79]:



for i in range(42):
    pmn[i].columns = ["Word","Meaning & Synonym","Antonym","Usage"]


# In[80]:


del df


# In[81]:


df = pd.DataFrame(columns=["Word","Meaning & Synonym","Antonym","Usage"])
#df = pd.DataFrame()


# In[82]:


#df=pd.concat([df, table_MN[0]],ignore_index=True)
for i in range(42):
    #print(table_MN[i].columns)
    df=pd.concat([df, table_MN[i]],ignore_index=True, axis=0)
    
    


# In[83]:


df.columns


# In[85]:


df


# In[87]:


#df.to_pickle('thehindu_vocab-bz2.pkl',compression='bz2',protocol=4)


# In[95]:


pdf = pd.read_pickle('thehindu_vocab-bz2.pkl',compression='bz2')


# In[96]:


pdf


# In[101]:


pdf['Word'].isin(["Rollback", "Persecution"])


# In[ ]:





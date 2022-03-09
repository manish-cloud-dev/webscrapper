#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from os import path
import re


# In[2]:


pdf = pd.read_pickle('thehindu_vocab-bz2.pkl',compression='bz2')


# In[3]:


df = pdf[['Word', 'Antonym']] 


# In[5]:


valid_pattern=r'[a-zA-Z]+'
re_pattern = re.compile(valid_pattern)
synm_words=""
antnm_words=""
for words in df['Word']: 
    synm_words = synm_words + words + ' '
df['Antonym'] = df['Antonym'].astype(str)
for words in df['Antonym']: 
    #print(type(words))
    if bool(re.match(re_pattern,words)):
        antnm_words = antnm_words + words + ' '


# In[6]:



#img_mask = np.array(Image.open(path.join("","cheetah")))
#img_mask = np.array(Image.open(path.join("","twitter_mask.png")))
#img_mask = np.array(Image.open(path.join("","apple-logo-0.png")))

wc1 = WordCloud(width = 800, height = 800, 
            background_color ='white', #mask=img_mask,
            min_font_size = 10).generate(synm_words) 

wc2 = WordCloud(width = 800, height = 800, 
            background_color ='white', #mask=img_mask,
            min_font_size = 10).generate(antnm_words) 


# In[7]:


# plot the WordCloud image                        
plt.figure(figsize = (8, 8), facecolor = None) 
plt.imshow(wc1) 
#plt.imshow(wc2) 
plt.axis("off") 
plt.tight_layout(pad = 0) 

plt.show() 


# In[8]:


wc1.to_file("vocab_synm_learn.png")
wc2.to_file("vocab_antnm_learn.png")


# In[ ]:





# In[ ]:





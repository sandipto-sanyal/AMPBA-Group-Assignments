#!/usr/bin/env python
# coding: utf-8

# # Import the necessary libraries

# In[5]:


import requests
import pandas as pd


# # Get the dimension list

# In[6]:


# load the dimensions data
dimensions_df = pd.read_excel('dimensions.xlsx')
dimensions_df.head()


# # Pull requests from each of the dimensions

# In[8]:


error_log_file = './data/error_log.csv'
error_log = open(error_log_file,'w')


# In[ ]:


for dim in dimensions_df.IndicatorCode.unique():
    try:
        url = 'http://apps.who.int/gho/athena/api/GHO/{}?format=csv'.format(dim)
        resp = requests.get(url)
        # save the csv in data folder
        data_save_path = './data/{}.csv'.format(dim)
        with open(data_save_path,'w') as file:
            file.write(resp.text)
        print('Done:{}'.format(dim))
    except Exception as e:
        s = dim + "," + str(e) + '\n'
        error_log.write(s)
error_log.close()


# In[ ]:





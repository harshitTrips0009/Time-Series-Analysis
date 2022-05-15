#!/usr/bin/env python
# coding: utf-8

# Author: Harshit Tripathi
Time-Series-Analysis
# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


path = r'C:\Users\Asus\Downloads\stock-price-data\individual_stocks_5yr-20220118T050347Z-001\individual_stocks_5yr'
company_list = ['AAPL_data.csv','NKE_data.csv','NFLX_data.csv','IBM_data.csv']
all_data = pd.DataFrame()
for file in company_list:
    current_df = pd.read_csv(path+'/'+file)
    all_data=pd.concat([all_data,current_df],ignore_index= True)                            


# In[3]:


all_data.shape


# In[4]:


all_data.head()


# TASK-1 
# Analyse closing price of all the stocks.

# In[5]:


tech_list = all_data['Name'].unique()
tech_list


# In[6]:


all_data['date']=pd.to_datetime(all_data['date'])


# In[7]:


plt.figure(figsize=(15,15))
for i,company in enumerate(tech_list,1):
    plt.subplot(2,2,i)
    df = all_data[all_data['Name']==company]
    plt.plot(df['date'],df['close'])
    plt.title(company)
    plt.grid(which="major", color='k', linestyle='solid', linewidth=0.5)
    


# Task-2
# Analyse the total volume of stock traded each day.

# In[8]:


import plotly.express as px


# In[9]:


for company in tech_list:
    df=all_data[all_data['Name']==company]
    fig=px.line(df,x='date',y='volume',title=company)
    fig.show()


# TASK-3
# Analyse daily price change in stock

# In[10]:


df=pd.read_csv(r'C:\Users\Asus\Downloads\stock-price-data\individual_stocks_5yr-20220118T050347Z-001\individual_stocks_5yr\IBM_data.csv')


# In[11]:


all_data['Daily_price_change'] = (all_data['close']-all_data['open'])
all_data['1Day%return'] = ((all_data['close']-all_data['open'])/all_data['close'])*100


# In[12]:


all_data


# In[13]:


for company in tech_list:
    df=all_data[all_data['Name']==company]
    fig=px.line(df,x='date',y='1Day%return',title=company)
    fig.show()


# TASK-4
# Analyse monthly mean of close feature

# In[14]:


df2=df.copy()
df2['date']=pd.to_datetime(df2['date'])
df2.set_index('date',inplace=True)


# In[15]:


df2['close'].resample('M').mean()


# In[16]:


df2['close'].resample('M').mean().plot()


# In[17]:


df2['close'].resample('Y').mean().plot(kind='bar')


# TAKS-5
# Analyse whether the stock price of these campanies(AAPL, NKE, NFLX, IBM) are correalted or not!
# 

# In[18]:


aapl=pd.read_csv(r'C:\Users\Asus\Downloads\stock-price-data\individual_stocks_5yr-20220118T050347Z-001\individual_stocks_5yr/AAPL_data.csv')
nke=pd.read_csv(r'C:\Users\Asus\Downloads\stock-price-data\individual_stocks_5yr-20220118T050347Z-001\individual_stocks_5yr/NKE_data.csv')
nflx=pd.read_csv(r'C:\Users\Asus\Downloads\stock-price-data\individual_stocks_5yr-20220118T050347Z-001\individual_stocks_5yr/nflx_data.csv')
ibm=pd.read_csv(r'C:\Users\Asus\Downloads\stock-price-data\individual_stocks_5yr-20220118T050347Z-001\individual_stocks_5yr/ibm_data.csv')


# In[19]:


aapl.head()


# In[20]:


nke.head()


# In[21]:


nflx.head()


# In[22]:


ibm.head()


# In[23]:


close=pd.DataFrame()


# In[24]:


close['aapl']=aapl['close']
close['nke']=nke['close']
close['nflx']=nflx['close']
close['ibm']=ibm['close']
close.head()


# In[25]:


sns.pairplot(close)


# In[26]:


sns.heatmap(close.corr(),annot=True)


# TASK-6 
# Analyse Daily return of each stock & how they are correlated.

# In[27]:


DATA = pd.DataFrame()


# In[28]:


DATA['aapl']=((aapl['close']-aapl['open'])/aapl['close'])*100
DATA['nflx']=((nflx['close']-nflx['open'])/nflx['close'])*100
DATA['nke']=((nke['close']-nke['open'])/nke['close'])*100
DATA['ibm']=((ibm['close']-ibm['open'])/ibm['close'])*100
DATA.head()


# In[29]:


sns.pairplot(DATA)


# In[30]:


sns.heatmap(DATA.corr(),annot=True)


# TASK-7
# Value at risk analysis for each companies.

# In[31]:


sns.distplot(DATA['nke'],hist_kws=dict(edgecolor="black", linewidth=2))


# In[32]:


sns.distplot(DATA['ibm'],hist_kws=dict(edgecolor="black", linewidth=2))


# In[33]:


sns.distplot(DATA['nflx'],hist_kws=dict(edgecolor="black", linewidth=2))


# In[34]:


sns.distplot(DATA['aapl'],hist_kws=dict(edgecolor="black", linewidth=2))


# In[35]:


DATA.describe().T


# In[ ]:





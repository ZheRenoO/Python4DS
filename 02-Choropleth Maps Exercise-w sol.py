#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___

# # Choropleth Maps Exercise 
# 
# Welcome to the Choropleth Maps Exercise! In this exercise we will give you some simple datasets and ask you to create Choropleth Maps from them. Due to the Nature of Plotly we can't show you examples
# 
# [Full Documentation Reference](https://plot.ly/python/reference/#choropleth)
# 
# ## Plotly Imports

# In[1]:


import plotly.graph_objs as go 
from plotly.offline import init_notebook_mode,iplot
init_notebook_mode(connected=True) 


# ** Import pandas and read the csv file: 2014_World_Power_Consumption**

# In[2]:


import pandas as pd


# In[3]:


wp = pd.read_csv('2014_World_Power_Consumption')


# In[4]:


wp.head()


# ** Check the head of the DataFrame. **

# In[156]:





# ** Referencing the lecture notes, create a Choropleth Plot of the Power Consumption for Countries using the data and layout dictionary. **

# In[8]:


data = dict(
        type = 'choropleth',
        locations = wp['Country'],
        z = wp['Power Consumption KWH'],
        text = wp['Text'],
        colorbar = {'title' : 'Power Consumption for Countries'},
      ) 


# In[11]:


layout = dict(
    title = 'Power Consumption for Countries',
    geo = dict(
        showframe = False,
        projection = {'type':'mercator'}
    )
)


# In[ ]:





# In[12]:


choromap = go.Figure(data = [data],layout = layout)
iplot(choromap,validate=False)


# ## USA Choropleth
# 
# ** Import the 2012_Election_Data csv file using pandas. **

# In[13]:


ed = pd.read_csv('2012_Election_Data')


# ** Check the head of the DataFrame. **

# In[14]:


ed.head()


# In[110]:





# ** Now create a plot that displays the Voting-Age Population (VAP) per state. If you later want to play around with other columns, make sure you consider their data type. VAP has already been transformed to a float for you. **

# In[41]:


data = dict(
        type = 'choropleth',
        colorscale = 'Viridis',
        reversescale = True,
        locations = ed['State Abv'],
        z = ed['Voting-Age Population (VAP)'],
        locationmode = 'USA-states',
        text = ed['State'],
        marker = dict(line = dict(color = 'rgb(255,255,255)',width = 1)),
        colorbar = {'title' : 'Voting-Age Population (VAP) per state'},
      ) 


# In[42]:


layout = dict(
    title = 'Voting-Age Population (VAP) per state',
    geo = dict(
        scope='usa',
        showframe = True
        #projection = {'type':'mercator'}
    )
)


# In[43]:


choromap = go.Figure(data = [data],layout = layout)
iplot(choromap,validate=False)


# # Great Job!

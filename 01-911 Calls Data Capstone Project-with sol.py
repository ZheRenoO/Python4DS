#!/usr/bin/env python
# coding: utf-8

# # 911 Calls Capstone Project

# For this capstone project we will be analyzing some 911 call data from [Kaggle](https://www.kaggle.com/mchirico/montcoalert). The data contains the following fields:
# 
# * lat : String variable, Latitude
# * lng: String variable, Longitude
# * desc: String variable, Description of the Emergency Call
# * zip: String variable, Zipcode
# * title: String variable, Title
# * timeStamp: String variable, YYYY-MM-DD HH:MM:SS
# * twp: String variable, Township
# * addr: String variable, Address
# * e: String variable, Dummy variable (always 1)
# 
# Just go along with this notebook and try to complete the instructions or answer the questions in bold using your Python and Data Science skills!

# ## Data and Setup

# ____
# ** Import numpy and pandas **

# In[1]:


import numpy as np
import pandas as pd


# ** Import visualization libraries and set %matplotlib inline. **

# In[3]:


import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# ** Read in the csv file as a dataframe called df **

# In[4]:


df = pd.read_csv('911.csv')


# ** Check the info() of the df **

# In[5]:


df.info()


# ** Check the head of df **

# In[6]:


df.head()


# ## Basic Questions

# ** What are the top 5 zipcodes for 911 calls? **

# In[33]:


df['zip'].value_counts().head()


# In[134]:





# ** What are the top 5 townships (twp) for 911 calls? **

# In[34]:


df['twp'].value_counts().head()


# In[135]:





# ** Take a look at the 'title' column, how many unique title codes are there? **

# In[7]:


df['title'].nunique()


# In[136]:





# ## Creating new features

# ** In the titles column there are "Reasons/Departments" specified before the title code. These are EMS, Fire, and Traffic. Use .apply() with a custom lambda expression to create a new column called "Reason" that contains this string value.** 
# 
# **For example, if the title column value is EMS: BACK PAINS/INJURY , the Reason column value would be EMS. **

# In[27]:


df['Reason']=df['title'].apply(lambda x:x.split(':')[0])


# In[28]:


df['Reason'][1:5]


# ** What is the most common Reason for a 911 call based off of this new column? **

# In[29]:


df['Reason'].value_counts()


# In[138]:





# ** Now use seaborn to create a countplot of 911 calls by Reason. **

# In[36]:


sns.countplot(x='Reason',data=df,saturation=0.8)


# In[139]:





# ___
# ** Now let us begin to focus on time information. What is the data type of the objects in the timeStamp column? **

# In[40]:


type(df['timeStamp'])


# In[44]:


df['timeStamp'].dtypes


# In[140]:





# ** You should have seen that these timestamps are still strings. Use [pd.to_datetime](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.to_datetime.html) to convert the column from strings to DateTime objects. **

# In[45]:


df['timeStamp']=pd.to_datetime(df['timeStamp'])


# In[47]:


df['timeStamp'].dtypes


# ** You can now grab specific attributes from a Datetime object by calling them. For example:**
# 
#     time = df['timeStamp'].iloc[0]
#     time.hour
# 
# **You can use Jupyter's tab method to explore the various attributes you can call. Now that the timestamp column are actually DateTime objects, use .apply() to create 3 new columns called Hour, Month, and Day of Week. You will create these columns based off of the timeStamp column, reference the solutions if you get stuck on this step.**

# In[82]:


df['timeStamp'].iloc[:]


# In[80]:


df['timeStamp']


# In[111]:


df['ts'] = df['timeStamp'].iloc[:]
# df['ts1'] = df['timeStamp'].iloc[:]

df['hour'] = df['ts'].apply(lambda x:x.hour)
df['month'] = df['ts'].apply(lambda x:x.month)
df['weekday'] = df['ts'].apply(lambda x:x.dayofweek)


# In[112]:


time = df['timeStamp'].iloc[555];time
time.weekday()


# In[113]:


pd.options.display.max_rows = 4000


# In[117]:


df['weekday'].dtype


# In[142]:





# ** Notice how the Day of Week is an integer 0-6. Use the .map() with this dictionary to map the actual string names to the day of the week: **
# 
#     dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}

# In[119]:


dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}


# In[121]:


df['DayofWeek']=df['weekday'].map(dmap)
#dmap[df['weekday']]


# In[122]:


df['DayofWeek']


# ** Now use seaborn to create a countplot of the Day of Week column with the hue based off of the Reason column. **

# In[127]:


sns.countplot(x='DayofWeek',data=df,hue='Reason')


# In[168]:





# **Now do the same for Month:**

# In[128]:


sns.countplot(x='month',data=df,hue='Reason')


# In[3]:





# **Did you notice something strange about the Plot?**
# 
# _____
# 
# ** You should have noticed it was missing some Months, let's see if we can maybe fill in this information by plotting the information in another way, possibly a simple line plot that fills in the missing months, in order to do this, we'll need to do some work with pandas... **

# ** Now create a gropuby object called byMonth, where you group the DataFrame by the month column and use the count() method for aggregation. Use the head() method on this returned DataFrame. **

# In[134]:


byMonth = df.groupby('month').count();byMonth.head()


# In[169]:





# ** Now create a simple plot off of the dataframe indicating the count of calls per month. **

# In[145]:


byMonth['desc'].plot.line()


# In[175]:





# ** Now see if you can use seaborn's lmplot() to create a linear fit on the number of calls per month. Keep in mind you may need to reset the index to a column. **

# In[148]:


byMonth = byMonth.reset_index();byMonth


# In[153]:


byMonth.drop(columns=['level_0','index'],inplace=True);byMonth


# In[155]:


sns.lmplot(x='month',y='twp',data=byMonth)


# In[187]:





# **Create a new column called 'Date' that contains the date from the timeStamp column. You'll need to use apply along with the .date() method. ** 

# In[164]:


df['date'] = df['ts'].apply(lambda x:x.date)


# In[165]:


df['date']


# In[162]:


df['ts'].iloc[0]


# In[163]:


df['ts'].iloc[0].date()


# In[193]:


df['weekday'] = df['ts'].apply(lambda x:x.dayofweek)


# ** Now groupby this Date column with the count() aggregate and create a plot of counts of 911 calls.**

# In[169]:


df['date']=df['timeStamp'].dt.date
df['date']


# In[173]:


df3 = df.groupby('date').count();df3


# In[174]:


df3['twp'].plot.line()


# In[197]:





# ** Now recreate this plot but create 3 separate plots with each plot representing a Reason for the 911 call**

# In[184]:


df[df['Reason']=='Traffic'].groupby('date').count()['twp'].plot.line()


# In[ ]:





# In[199]:





# In[201]:





# In[202]:





# ____
# ** Now let's move on to creating  heatmaps with seaborn and our data. We'll first need to restructure the dataframe so that the columns become the Hours and the Index becomes the Day of the Week. There are lots of ways to do this, but I would recommend trying to combine groupby with an [unstack](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.unstack.html) method. Reference the solutions if you get stuck on this!**

# In[201]:


# df_1 = df.groupby('hour').count();df_1
table=df.pivot_table(values = 'twp', index='DayofWeek',columns='hour',aggfunc = 'count' )


# In[213]:


df.groupby(by=['DayofWeek','hour']).count()['twp'].unstack()


# ** Now create a HeatMap using this new DataFrame. **

# In[205]:


sns.heatmap(table,cmap='coolwarm')


# In[204]:





# ** Now create a clustermap using this DataFrame. **

# In[207]:


sns.clustermap(table,figsize=(10,10))


# In[205]:





# ** Now repeat these same plots and operations, for a DataFrame that shows the Month as the column. **

# In[ ]:





# In[ ]:





# In[207]:





# In[208]:





# In[209]:





# **Continue exploring the Data however you see fit!**
# # Great Job!

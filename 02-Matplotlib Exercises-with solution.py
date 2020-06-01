#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___
# # Matplotlib Exercises 
# 
# Welcome to the exercises for reviewing matplotlib! Take your time with these, Matplotlib can be tricky to understand at first. These are relatively simple plots, but they can be hard if this is your first time with matplotlib, feel free to reference the solutions as you go along.
# 
# Also don't worry if you find the matplotlib syntax frustrating, we actually won't be using it that often throughout the course, we will switch to using seaborn and pandas built-in visualization capabilities. But, those are built-off of matplotlib, which is why it is still important to get exposure to it!
# 
# ** * NOTE: ALL THE COMMANDS FOR PLOTTING A FIGURE SHOULD ALL GO IN THE SAME CELL. SEPARATING THEM OUT INTO MULTIPLE CELLS MAY CAUSE NOTHING TO SHOW UP. * **
# 
# # Exercises
# 
# Follow the instructions to recreate the plots using this data:
# 
# ## Data

# In[2]:


import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2


# ** Import matplotlib.pyplot as plt and set %matplotlib inline if you are using the jupyter notebook. What command do you use if you aren't using the jupyter notebook?**

# In[1]:


import matplotlib.pyplot as plt


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')


# ## Exercise 1
# 
# ** Follow along with these steps: **
# * ** Create a figure object called fig using plt.figure() **
# * ** Use add_axes to add an axis to the figure canvas at [0,0,1,1]. Call this new axis ax. **
# * ** Plot (x,y) on that axes and set the labels and titles to match the plot below:**

# In[7]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

ax.plot(x,y,'b')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Title')


# ## Exercise 2
# ** Create a figure object and put two axes on it, ax1 and ax2. Located at [0,0,1,1] and [0.2,0.5,.2,.2] respectively.**

# In[10]:


fig = plt.figure()

ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,.2,.2])


# ** Now plot (x,y) on both axes. And call your figure object to show it.**

# In[16]:


ax1.plot(x, y, 'r')
ax2.plot(x, y, 'r')
fig #why make this additional call?


# ## Exercise 3
# 
# ** Create the plot below by adding two axes to a figure object at [0,0,1,1] and [0.2,0.5,.4,.4]**

# In[17]:


fig = plt.figure()

ax1 = fig.add_axes([0,0,1,1])
ax2 = fig.add_axes([0.2,0.5,.4,.4])


# In[6]:





# ** Now use x,y, and z arrays to recreate the plot below. Notice the xlimits and y limits on the inserted plot:**

# In[27]:


fig, axes = plt.subplots(2, 1, figsize=(8, 4))

ax1 = fig.add_axes([0,0,1,1])
ax1.plot(x,x**2)
ax1.set_xlim([0,100])
ax1.set_ylim([0,10000])
ax2.set_xlabel('x')
ax2.set_ylabel('z')

ax2 = fig.add_axes([0.2,0.5,.4,.4])
ax2.plot(x,1.1*x+20)
ax2.set_xlim([20,22])
ax2.set_ylim([30,50])
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('zoom')


# In[5]:





# ## Exercise 4
# 
# ** Use plt.subplots(nrows=1, ncols=2) to create the plot below.**

# In[28]:


fig, axes = plt.subplots(nrows=1,ncols=2)


# In[48]:





# ** Now plot (x,y) and (x,z) on the axes. Play around with the linewidth and style**

# In[52]:


# line, = ax.plot(x, x+8, color="black", lw=1.50)
# line.set_dashes([0,20,40,60,80,100])
axes[0].plot(x,x*2,lw=0.5,ls='-.',color='b')
axes[0].set_xlim(1,20)
axes[1].plot(x,x**2,lw=3,ls='-',color='r')
fig


# In[48]:


axes[0].plot(x,y,color="blue", lw=3, ls='--')
axes[1].plot(x,z,color="red", lw=3, ls='-')
fig


# In[51]:





# ** See if you can resize the plot by adding the figsize() argument in plt.subplots() are copying and pasting your previous code.**

# In[32]:





# # Great Job!

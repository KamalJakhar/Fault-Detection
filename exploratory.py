
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import array
import matplotlib.pyplot as plt
import matplotlib.axes as d
from sklearn import datasets, linear_model 


# In[2]:


df = pd.read_csv("explofinal.csv") 


# In[3]:


df


# In[13]:


plt.plot(df["time "],df["output voltage"])


# In[17]:


df.iloc[207]


# In[11]:


l=df["output voltage"][53:53+204].tolist()


# In[12]:


np.sum(l)


# In[13]:


l=[]
l1=[]
for j in range(53,1500):
    l.append(np.sum(df["output voltage"][j:j+204]))
    l1.append(j)


# In[14]:


#plt.xlim(1500)
plt.plot(l1,l)


# In[34]:


#.set_xlim(900,1100)
#plt.ylim(-100,100)
plt.xlim(750,900)
plt.plot(l1,l)


# In[36]:


df["time "][840]


# In[72]:


l1[790]


# In[70]:


l[790]


# In[35]:


df["time "][840]


# In[7]:


#l=df["output voltage"][52:1502].tolist()


# In[15]:


l2=[]
for i in range(53,1500):
    l2.append((((df["output voltage"][i+1]-df["output voltage"][i-1])/(0.0002*100*np.pi))**2)+df["output voltage"][i]**2)


# In[21]:


plt.plot(l1,l2)


# In[30]:


plt.xlim(950,1100)
plt.plot(l1,l2)


# In[37]:


df["time "][1010]


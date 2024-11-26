#!/usr/bin/env python
# coding: utf-8

# # Data Visualization

# ## Matplotlib

# ### 1.Plotting Line

# In[2]:


import matplotlib.pyplot as plt


# In[3]:


import numpy as np


# In[4]:


x=np.array([0,6])


# In[5]:


y=np.array([0,250])


# In[6]:


plt.plot(x,y)


# In[7]:


plt.show()


# ### 2. Plotting without line

# In[8]:


import matplotlib.pyplot as plt


# In[9]:


import numpy as np


# In[10]:


x=np.array([0,6])


# In[11]:


y=np.array([0,250])


# In[12]:


plt.plot(x,y,'o')
plt.show()


# ### 3. Multiple Points

# In[13]:


import matplotlib.pyplot as plt


# In[14]:


import numpy as np


# In[15]:


x=np.array([1,2,6,8])


# In[16]:


y=np.array([3,8,1,10])


# In[18]:


plt.plot(x,y)
plt.show()


# ### 4. Default x-axis

# In[19]:


import matplotlib.pyplot as plt


# In[20]:


import numpy as np


# In[21]:


y=np.array([3,8,1,10,5,7])


# In[22]:


plt.plot(y)
plt.show()


# ### 5. Matplot Markers

# In[23]:


import matplotlib.pyplot as plt


# In[24]:


import numpy as np


# In[25]:


y=np.array([3,8,1,10])


# In[26]:


plt.plot(y,marker='o')
plt.show()


# ### 6. Format string fmt

# In[27]:


import matplotlib.pyplot as plt


# In[28]:


import numpy as np


# In[29]:


y=np.array([3,8,1,10])


# In[30]:


plt.plot(y,'o:r')
plt.show()


# ### 6. Marker Size

# In[32]:


import matplotlib.pyplot as plt


# In[33]:


import numpy as np


# In[34]:


y=np.array([3,8,1,10])


# In[35]:


plt.plot(y,marker='o',ms=20)
plt.show()


# ### 8. Marker Edge Size

# In[36]:


import matplotlib.pyplot as plt


# In[37]:


import numpy as np


# In[38]:


y=np.array([3,8,1,10])


# In[39]:


plt.plot(y,marker='o',ms=20,mec='r')
plt.show()


# ### 9. Marker Face Color

# In[40]:


import matplotlib.pyplot as plt


# In[41]:


import numpy as np


# In[42]:


y=np.array([3,8,1,10])


# In[43]:


plt.plot(y,marker='o',ms=20,mfc='r')
plt.show()


# ### 10. Line Style Argument

# In[44]:


import matplotlib.pyplot as plt


# In[45]:


import numpy as np


# In[46]:


y=np.array([3,8,1,10])


# In[48]:


plt.plot(y,linestyle='dotted')
plt.show()


# ### 11. Line color Argument

# In[49]:


import matplotlib.pyplot as plt


# In[50]:


import numpy as np


# In[51]:


y=np.array([3,8,1,10])


# In[52]:


plt.plot(y,color='r')
plt.show()


# ### 11. Line Width Argument

# In[53]:


import matplotlib.pyplot as plt


# In[54]:


import numpy as np


# In[55]:


y=np.array([3,8,1,10])


# In[59]:


plt.plot(y,linewidth='9.6')
plt.show()


# ### 12. Multiple Width Argument

# In[60]:


import matplotlib.pyplot as plt


# In[61]:


import numpy as np


# In[75]:


x1=np.array([0,1,2,3])
y1=np.array([3,6,1,10])


# In[76]:


x2=np.array([0,1,2,3])
y2=np.array([6,2,7,11])


# In[77]:


plt.plot(x1,y1, color="r")
plt.plot(y2,x2,color="g")


# ### 13. Create Lables

# In[78]:


import matplotlib.pyplot as plt


# In[79]:


import numpy as np


# In[80]:


x=np.array([0,1,2,3,4,5])


# In[81]:


y=np.array([0,8,12,20,26,28])


# In[83]:


plt.plot(x,y)
plt.xlabel("overs")
plt.ylabel("Runs")
plt.show()


# ### 14. Create Title

# In[84]:


import matplotlib.pyplot as plt


# In[85]:


import numpy as np


# In[86]:


x=np.array([0,1,2,3,4,5])


# In[87]:


y=np.array([0,8,12,20,26,28])


# In[89]:


plt.plot(x,y)
plt.xlabel("overs")
plt.ylabel("Runs")
plt.title("Sport Data")
plt.show()


# ### 15. Set Font Properties for title and Labels

# In[90]:


import matplotlib.pyplot as plt


# In[91]:


import numpy as np


# In[92]:


x=np.array([0,1,2,3,4,5])


# In[93]:


y=np.array([0,8,12,20,26,28])


# In[94]:


font1={'family':'cambria','color':'red','size':20}
font2={'family':'cambria','color':'blue','size':20}


# In[97]:


plt.plot(x,y)
plt.xlabel("Overs",fontdict=font2)
plt.ylabel("Runs",fontdict=font2)
plt.title("Sport Data",fontdict=font1)
plt.show()


# In[ ]:





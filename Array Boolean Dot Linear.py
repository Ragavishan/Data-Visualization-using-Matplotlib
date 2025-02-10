#!/usr/bin/env python
# coding: utf-8

# # Array Concatenation

# In[1]:


import numpy as np


# In[2]:


arr1=np.array([1,2,3])


# In[3]:


arr2=np.array([4,5,6])


# In[5]:


concatenated=np.concatenate((arr1,arr2))


# In[10]:


print("Concatenated Array", concatenated)


# # Boolean Indexing

# In[11]:


import numpy as np


# In[12]:


arr=np.array([1,2,3,4,5])


# In[13]:


filter_arr=arr[arr>2]


# In[14]:


print("Filtered Array(greater then 2)", filter_arr)


# # Dot Product

# In[15]:


import numpy as np


# In[16]:


arr1=np.array([1,2,3])


# In[17]:


arr2=np.array([4,5,6])


# In[19]:


dot_product=np.dot(arr1,arr2)


# In[20]:


print("Dot Product",dot_product)


# # Linear Algebra Operations

# In[21]:


import numpy as np


# In[24]:


matrix=np.array([[1,2],[3,4]])


# In[25]:


determinant=np.linalg.det(matrix)


# In[26]:


inverse=np.linalg.inv(matrix)


# In[27]:


print("Determinant", determinant)


# In[28]:


print("Inverse", inverse)


# In[ ]:





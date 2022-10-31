#!/Users/antonincarratero/opt/anaconda3/bin/python
# coding: utf-8

# In[46]:


import pandas as pd
import numpy as np


# In[47]:


df=pd.DataFrame(columns=['A','B','C','D'], index=range(1000000))
for col in df:
    df[col]= df[col].fillna(np.random.normal(0,100))
df


# In[44]:


df['copy_D'] = df['D']



# In[ ]:


df.to_hdf5('HDF5_Dataframe', '/Users/antonincarratero/git/DigitalToolsForFinanceHomework/homework/week/data/')


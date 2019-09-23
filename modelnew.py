
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np
import re
import sklearn
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import warnings
warnings.filterwarnings('ignore')

from collections import Counter


# In[19]:


data=pd.read_csv('training.csv', encoding='Latin1')
data.head()


# In[20]:


data=data.drop(['ID'], axis=1)
data.head()


# In[21]:


data.info()


# In[22]:



#Convert categorical variable from integer to object
#this part have a purpose to simplify the creation of dummy variables at a next stage
data['MARRIAGE']=data['MARRIAGE'].astype(object)
data['EDUCATION']=data['EDUCATION'].astype(object)
data['SEX']=data['SEX'].astype(object)
data['PAY_1']=data['PAY_1'].astype(object)
data['PAY_2']=data['PAY_2'].astype(object)
data['PAY_3']=data['PAY_3'].astype(object)


# In[23]:


#Defined of Target as variable dependent and Other variable as variable independent
#Convert categorical variable to dummy variable

y=data['TARGET']
X=data[['BILL_AMT3', 'LIMIT_BAL', 'AGE']]

#Convert categorical variable to dummy variable
#X=pd.get_dummies(X)
X.shape


# In[24]:


X


# In[27]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)


# In[34]:


from sklearn.ensemble import RandomForestClassifier, VotingClassifier
clf = RandomForestClassifier(n_estimators=50, max_features='sqrt')
clf.fit(X_train, y_train)


# In[38]:


# Predicting the Test set results
y_pred = clf.predict(X_test)

# Saving model to disk
pickle.dump(clf, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load( open('model.pkl','rb'))
print(model.predict([[23881.0, 30000.0, 20]]))


# In[44]:


[np.array(data[['BILL_AMT3', 'LIMIT_BAL', 'AGE']])]


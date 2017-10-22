
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
import pickle


# In[2]:

train=pd.read_csv('new_data.csv')


# In[3]:

train.head()


# In[4]:

train.describe()


# In[5]:

x_train=train.drop(['Result'],axis=1)
y_train=train['Result']


# In[6]:

from sklearn import linear_model
model=linear_model.LogisticRegression()


# In[7]:

from sklearn.model_selection import cross_val_score
scores=cross_val_score(model, x_train, y_train, cv=10)
scores.mean()


# In[8]:

from sklearn import svm
model=svm.SVC()
scores=cross_val_score(model, x_train, y_train, cv=10)
scores.mean()


# In[9]:

from sklearn import tree
model=tree.DecisionTreeClassifier()
scores=cross_val_score(model, x_train, y_train, cv=10)
scores.mean()


# In[10]:

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
scores=cross_val_score(model, x_train, y_train, cv=10)
scores.mean()


# In[11]:

from sklearn.ensemble import AdaBoostClassifier
model = AdaBoostClassifier()
scores=cross_val_score(model, x_train, y_train, cv=10)
scores.mean()


# In[12]:

model.fit(x_train,y_train)


# In[13]:

model.feature_importances_


# In[14]:

filename= 'best_model.sav'
pickle.dump(model, open(filename, 'wb'))


# In[ ]:





# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

# In[2]:

train=pd.read_csv('train.csv')


# In[3]:

#print(train.head())


# In[4]:

#train.describe()


# In[5]:

#train.info()


# In[6]:

x_train=train.drop(['Result'],axis=1)
y_train=train['Result']


# In[9]:

from sklearn import linear_model
model=linear_model.LogisticRegression()


# In[10]:

from sklearn.model_selection import cross_val_score
scores=cross_val_score(model, x_train, y_train, cv=10)
scores.mean()


# In[11]:

from sklearn import svm
model=svm.SVC()
scores=cross_val_score(model, x_train, y_train, cv=10)
scores.mean()


# In[13]:

from sklearn import tree
model=tree.DecisionTreeClassifier()
scores=cross_val_score(model, x_train, y_train, cv=10)
scores.mean()


# In[21]:

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
scores=cross_val_score(model, x_train, y_train, cv=10)
scores.mean()


# In[31]:

from sklearn.ensemble import AdaBoostClassifier
model = AdaBoostClassifier()
scores=cross_val_score(model, x_train, y_train, cv=10)
scores.mean()


# In[32]:

best_model=RandomForestClassifier()
best_model.fit(x_train,y_train)

filename= 'best_model.sav'
pickle.dump(best_model, open(filename, 'wb'))
# In[36]:



# In[ ]:




#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from mp.Dataprocessor import *
from mp.Modelevaluator import *
from sklearn.preprocessing import Normalizer
import os
os.chdir(os.getcwd()+'\\data')


dl=Data_Loader()
data=dl.upload()

dp=Data_Processor
d_train, d_test = dp.test_train_split(data)
x_train,y_train,x_test,y_test = dp.normaliser(d_train,d_test)

#Cross Validate Logistic Regression Classifier
rf = RandomForestRegressor(n_estimators=10, n_jobs=-1, random_state=5, max_depth=5)
mod = Modelevaluator(rf,x_train, x_test, y_train, y_test)

print(mod.cross_evaluation(cv_int=5))
print(mod.r2score())

path_parent = os.path.dirname(os.getcwd())
os.chdir(path_parent)
print(os.getcwd())

mod.save_model('xgbregressor.pkl')

d_test_norm=pd.DataFrame(Normalizer().fit_transform(d_test.loc[:,'sens_1':'sens_5']))
cols=list(d_test.columns)
d_test_norm.columns=cols
d_test_norm['sens_1_pred']=mod.generate_predictions()
d_test_norm=d_test_norm.set_index(d_test.index)

d_test_norm.to_csv('test_data.csv',index=True)

#engine.execute('drop table sensor')


from sqlalchemy import *
engine = create_engine('sqlite:///pyakc.db', echo=False)
table_name='sensor'
qry_table=pd.read_sql_query("SELECT * FROM {}".format(table_name), con=engine)


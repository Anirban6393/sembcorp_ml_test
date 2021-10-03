#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd 
import numpy as np
import pickle
import os
from mp.DB import *

model = pickle.load(open("xgbregressor.pkl",'rb'))

table_name='model_logging'
db='pyakc'
dba=Database()
engine=dba.define_engine(db)

#dba.delete_table(table_name)

#dba.create_logging_table(table_name)

import datetime as dt
from scipy.stats import binom

ct=dt.datetime.now()
log_data=pd.DataFrame({'timestamp':ct.strftime("%m/%d/%Y, %H:%M:%S"),
                'sens_2': binom.rvs(n=125,p=0.65,size=100),
              'sens_4': binom.rvs(n=100,p=0.7,size=100),
              'sens_5': binom.rvs(n=235,p=0.2,size=100)})

log_data['sens1_logging']=model.predict(log_data.loc[:,'sens_2':'sens_5'])

log_data.to_sql('model_logging', con=engine, if_exists='append',index=False)


#qry_table=pd.read_sql_query("SELECT * FROM {}".format(table_name), con=engine)
#qry_table


# In[ ]:





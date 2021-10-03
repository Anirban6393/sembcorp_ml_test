import pandas as pd
import numpy as np
from sklearn.preprocessing import Normalizer
import os
import glob

class Data_Loader(object):   
    def __init__(self):
        self.path=os.getcwd()
        
    def upload(self):
        path=self.path
        parqs = glob.glob(os.path.join(path, "*.parquet"))
        jsons = glob.glob(os.path.join(path, "*.json"))
        pickles = glob.glob(os.path.join(path, "*.pickle"))
        csvs = glob.glob(os.path.join(path, "*.csv"))
        excels = glob.glob(os.path.join(path, "*.xlsx"))
        for pq in parqs:     
            parquet = pd.read_parquet(pq, engine='pyarrow')
        for pk in pickles:     
            pickle = pd.read_pickle(pk)
        for js in jsons:     
            json = pd.read_json(js).transpose()
        for cv in csvs:     
            csv = pd.read_csv(cv)
        for xl in excels:     
            xlsx = pd.read_excel(xl)
        d=pd.concat([parquet,pickle,json,csv,xlsx],axis=0)
        d=d.reset_index(drop=True)
        return d


class Data_Processor(object):
    def __init__(self):
        self.data=Data_Loader().upload()
        self.data=d
        
    def test_train_split(d):
        d.loc[d["tag_quality"]!='Good','tag_val']='Bad'
        d['tag_val']=d['tag_val'].replace('Bad',np.nan)
        d['tag_val']=d['tag_val'].fillna(method="ffill")
        d_pivot=d.pivot(index='created_timestamp',columns='tag_key',values='tag_val')
        d_pivot.sort_index(ascending=True)
        for i in list(d_pivot.columns):
            d_pivot[i]=d_pivot[i].fillna(method="ffill")
            d_pivot[i]=d_pivot[i].fillna(method="bfill")        
        n=int(d_pivot.shape[0]*0.7)
        d_train = d_pivot[:n]
        d_test = d_pivot[n:]
        return d_train, d_test

    def normaliser(d_train,d_test):
        transformer = Normalizer()
        cols=list(d_train.columns)
        d_train_norm = pd.DataFrame(transformer.fit_transform(d_train))
        d_test_norm = pd.DataFrame(transformer.fit_transform(d_test))
        d_train_norm.columns=cols
        d_test_norm.columns=cols
        x_train=d_train_norm.loc[:,'sens_2':'sens_5']
        x_test=d_test_norm.loc[:,'sens_2':'sens_5']
        y_train=d_train_norm['sens_1']
        y_test=d_test_norm['sens_1']
        return x_train,y_train,x_test,y_test 
    

        

        
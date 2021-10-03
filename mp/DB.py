from flask import Flask, jsonify
import pandas as pd 
import numpy as np
import pickle
import os
from sqlalchemy import *
from sqlalchemy import create_engine
from mp.DB import *

model = pickle.load(open("xgbregressor.pkl",'rb'))

class Database(object):
    @staticmethod
    def define_engine(db):
        engine = create_engine('sqlite:///{}.db'.format(db), echo=False)
        return engine
    
    @staticmethod
    def create_logging_table(table_name):
        table = """CREATE TABLE {}(
            timestamp key NOT NULL,
            sens_2 float NULL,
            sens_4 float NULL,
            sens_5 float NULL,
            sens1_logging float NULL
        ); """.format(table_name)
        return engine.execute(table)
    
    @staticmethod
    def delete_table(table_name):
        return engine.execute('drop table {}'.format(table_name))
    
    @staticmethod
    def data_transformation(query):
        return engine.execute(query)
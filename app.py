from flask import Flask, render_template, request
import pandas as pd
import pickle
from sqlalchemy import *
from sqlalchemy import create_engine
import os

model = pickle.load(open("xgbregressor.pkl",'rb'))

app = Flask(__name__)
engine = create_engine('sqlite:///pyakc.db', echo=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        file = request.form['upload-file']
        data = pd.read_csv(file) 
        #data.to_html(header="true", table_id="table")
        data['sens_1_pred'] = model.predict(data.loc[:,'sens_2':'sens_5'])
        data.to_sql('sensor', con=engine, if_exists='fail')
        qry_table=pd.read_sql_query("SELECT * FROM sensor", con=engine)
        return qry_table.to_html(header="true", table_id="table")
    
if __name__ == '__main__':
    app.run(port = 1000, debug=True)
    
    




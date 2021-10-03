from flask import Flask, jsonify
import pandas as pd 
import numpy as np
import pickle
import os

model = pickle.load(open("xgbregressor.pkl",'rb'))
app = Flask(__name__)

 
@app.route('/')
def home():
	return render_template('home.html')
 
@app.route('/predict',methods=['POST'])
def predict():
	if request.method == 'POST':
		data = pd.DataFrame(columns=['sens_2','sens_4','sens_5'])
		for i in list(data.columns):
			data[i] = request.form[i]
		for i in ['sens_2','sens_4','sens_5']:
			data[i] = data[i].astype('int')
		my_prediction = model.predict(data)
	return render_template('result.html',data=my_prediction)

if __name__ == '__main__':
	app.run(debug=True, port=1500)
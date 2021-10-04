# sembcorp_ml_test
## Rest API
A RESTful API to return predictions from a trained ML model, built with Python 3 and Flask-RESTX

Development set-up instructions
First, open a command line interface and clone the GitHub repo in your workspace

```
PS > git clone https://github.com/Anirban6393/sembcorp_ml_test.git
PS > cd sembcorp_ml_test
```

Once dependencies are installed, set up the requirements.txt to download required packages.
```
(venv) PS > pip install -r requirements.txt
```

The file app.py is an interface that takes in your normalised test data, uploads them into an embedded sqlite database and then returns display of the table in html interface.
```
(venv) PS > python app.py
```
Open the URL http://127.0.0.1:1000/ with your browser, upload test.csv file and then you will see list of genre and titles returned from sqlite3.

The file visual.py is a dashboard showing time series visualisation of sensor 1 prediction as well as that of other sensors.

(venv) PS > python visual.py
```
Open the URL http://127.0.0.1:1000/ 
with your browser and you will see the dashboard built from python reputed dash and plotly libraries.

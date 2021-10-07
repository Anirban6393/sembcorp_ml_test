import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
from sqlalchemy import *
import numpy as np
import pandas as pd

engine = create_engine('sqlite:///pyakc.db', echo=False)
table_name='sensor'
df=pd.read_sql_query("SELECT * FROM {}".format(table_name), con=engine)


app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id="ticker",
        options=[{"label": x, "value": x} 
                 for x in df.columns[2:]],
        value=df.columns[1],
        clearable=False,
    ),
    dcc.Graph(id="time-series-chart"),
])


@app.callback(
    Output("time-series-chart", "figure"), 
    [Input("ticker", "value")])
def display_time_series(ticker):
    fig = px.line(df, x='created_timestamp', y=ticker)
    return fig


if __name__ == "__main__":
    app.run_server(debug=True, port=500)

import pandas_datareader.data as web
import datetime
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import flask
flask_app = flask.Flask(__name__)
app = dash.Dash(__name__, server = flask_app)
start= datetime.datetime(2017,1,1)
end = datetime.datetime.now()
stock = 'TSLA'
df = web.DataReader(stock,'yahoo', start, end)
app.layout = html.Div(children=[
    html.H1('Dash tutorial'),
    dcc.Input(id ='input', value='', type= 'text'),
    html.Div(id='output-graph')

    ])

@app.callback(
Output(component_id = 'output-graph', component_property='children'),
[Input(component_id = 'input', component_property='value')]
)
def update_graph(input_data):
    end = datetime.datetime.now()
    df = web.DataReader(input_data,'yahoo', start, end)
    return dcc.Graph(id = 'example',
    figure={
        'data':[{'x':df.index, 'y':df.Open, 'type':'line', 'name':stock},
                # {'x':[1,2,3,4], 'y':[10,5,7,1], 'type':'bar', 'name':'cats'}
                ],
                'layout':{
                'title': input_data
                }
            })
if __name__ == '__main__':
    flask_app.run(host = '0.0.0.0', debug=True)

print(df.head())

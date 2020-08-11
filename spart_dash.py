import findspark
findspark.init('/home/mysparkub/spark-3.0.0-bin-hadoop2.7')
from IPython.display import display, clear_output
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split
import time
import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
spark = SparkSession.builder.appName('struct_streaming1').getOrCreate()
lines = spark.readStream.format("socket").option('host', 'localhost').option('port', 9999).load()
words = lines.select(explode(split(lines.value, " ")).alias("word"))
wordCounts = words.groupBy("word").count()

app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1('counting words'),
    dcc.Graph(id = 'live-graph'),
    dcc.Interval(
        id = 'graph-update',
        interval = 1000,
        n_intervals=0
    )]
)
@app.callback(
Output('live-graph', 'figure'),
[Input('graph-update', 'n_intervals')]
)
def update_graph(n):
    X=dict(spark.sql('select * from table1').collect())
    fig = plotly.tools.make_subplots(rows=1, cols=1, vertical_spacing=0.2)
    fig['layout']['margin'] = {
        'l':30, 'r':10, 'b':30, 't':10
    }
    fig.append_trace({
        'x':list(X.keys()),
        'y':list(X.values()),
        'type':'bar'
    },1,1)
    return fig
if __name__ == "__main__":
    try:
        query = wordCounts.writeStream.outputMode("complete").format("memory").queryName("table1").start()
        app.run_server(debug = False)
    except :
        print('other side is not running')

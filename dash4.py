import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
X = deque()
Y = deque()
BX = ['a','b', 'c']
X.append(1)
Y.append(1)
intro_text = html.P(
    'این یه  تکست رندمه',
    dir = 'rtl'
)
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("this is a random plot"),
    html.Div(intro_text),
    html.Div(id = 'live-text'),
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
    global X
    global Y
    global BX
    BY = [random.randint(1,20) for i in range(3)]
    X.append(X[-1] + 1)
    Y.append(Y[-1]*(1 + random.uniform(-0.1,0.1)))

    fig = plotly.tools.make_subplots(rows=1, cols=1, vertical_spacing=0.2)
    fig['layout']['margin'] = {
        'l':30, 'r':10, 'b':30, 't':10
    }
    # fig.append_trace({
    #     'x':list(X)[-15:],
    #     'y':list(Y)[-15:],
    #     'name':'random',
    #     'mode':'lines+markers',
    #     'type':'scatter'
    # },1,1)
    fig.append_trace({
        'x':BX,
        'y':BY,
        'type':'bar'
    },1,1)
    return fig

@app.callback(Output('live-text', 'children'),
    [Input('graph-update', 'n_intervals')])
def update_text(n):
    try:
        return [html.H3(str(X[-3]) + '\t' + str(X[-2]) + '\t' + str(X[-1]))]
    except:
        return '1\t2\t\3'
if __name__ == "__main__":
    app.run_server(debug = True)

import dash
import dash_core_components as dcc
import dash_html_components as html
app = dash.Dash()
app.layout = html.Div(children=[
    html.H1('Dash tutorail'),
    dcc.Graph(id = 'example',
    figure={
        'data':[{'x':[1,2,3,4], 'y':[10,5,7,1], 'type':'line', 'name':'boats'},
                {'x':[1,2,3,4], 'y':[10,5,7,1], 'type':'bar', 'name':'cats'}
                ],
                'layout':{
                'title': 'Basic Graphs'
                }
            })
    ])
if __name__ == '__main__':
    app.run_server(debug=True)

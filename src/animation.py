# Inspired by https://dash.plotly.com/live-updates
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from Estimate_pi import rain_drop, is_point_in_circle
import sys

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(
    html.Div([
        html.H3('Pi Estimation'),
        html.Div(id='live-update-text'),
        dcc.Graph(id='live-update-graph',animate=True),
        dcc.Interval(
            id='interval-component',
            interval=1000, # in milliseconds
            n_intervals=0
        )
    ])
)

points_outside_circule_x=[]
points_outside_circule_y=[]
points_inside_circule_x=[]
points_inside_circule_y=[]
# @app.callback(Output('live-update-text', 'children'), [Input('interval-component', 'n_intervals')])
# def update_metrics(n):
#     x, y, z = random_num()
#     style = {'padding': '5px', 'fontSize': '16px'}
#     return [
#         html.Span('x: {0:.2f}'.format(x), style=style),
#         html.Span('y: {0:.2f}'.format(y), style=style),
#         html.Span('z: {0:0.2f}'.format(z), style=style)
#     ]

# Multiple components can update everytime interval gets fired.
@app.callback(Output('live-update-graph', 'figure'), [Input('interval-component', 'n_intervals')])
def update_graph_live(n):

    global points_outside_circule_x, points_outside_circule_y
    global points_outside_circule_y

    for i in range(1,20):
        rain = rain_drop()
        if is_point_in_circle(rain):
            points_inside_circule_x.append(rain[0])
            points_inside_circule_y.append(rain[1])
        else:
            points_outside_circule_x.append(rain[0])
            points_outside_circule_y.append(rain[1])

    # global timestamp
    #
    # accel.append(gVert)
    # # timestamp.append(datetime.datetime.fromtimestamp(ts))
    # timestamp.append(datetime.datetime.fromtimestamp(ts/1000))

    # data['time'] = timestamp
    # data['x'] = accel

    # Create the graph with subplots
    # fig = plotly.tools.make_subplots(rows=1, cols=1, vertical_spacing=0.2)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=points_inside_circule_x, y=points_inside_circule_y,
                             mode='markers',
                             marker=dict(
                                 color='red'),
                             name='In Circule'))
    fig.add_trace(go.Scatter(x=points_outside_circule_x, y=points_outside_circule_y,
                             mode='markers',
                             marker=dict(
                                 color='blue'),
                             name='Outside Circule'))
    fig['layout']['xaxis'] = {
        'range':[-0.5,0.5]
    }
    fig['layout']['yaxis'] = {
        'range': [-0.5, 0.5]
    }
    fig['layout'] = {'template':'plotly_dark'}

    return fig


if __name__ == '__main__':
    # argv[1] = host ipaddress
    # argv[2] = host port
    # argv[3] = Kafka server IP Address and Port
    # argv[4] = topic

    ipaddress   =   sys.argv[1]
    hostport    =   sys.argv[2]

    app.run_server(debug=True, port=hostport, host=ipaddress)
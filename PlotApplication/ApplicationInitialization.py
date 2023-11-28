import util

import dash
from dash import html, dcc


class ApplicationInitialization:
    def __init__(self) -> None:
        pass
    
    def InitedApplication(self, app: dash.Dash) -> None:
        app.layout = html.Div([
            dcc.Graph(id='live-update-graph', animate=True),
            html.Div([
                html.Img(src='https://ifh.cc/g/JL1YHk.png', style={'width': '20%', 'padding': '10px', 'padding-top': '20px'}),
            ], style={'display': 'flex', 'justify-content': 'right'}),
            dcc.Interval(
            id='interval-component',
            interval=500, 
            n_intervals=100
            )])    
        return 
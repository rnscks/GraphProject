import util
import threading
import dash
from dash.dependencies import Input, Output
from PlotApplication.Plotter import Plotter 
from PlotApplication.ApplicationInitialization import ApplicationInitialization

app = dash.Dash(__name__)
ApplicationInitialization().InitedApplication(app)

@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n):
    trace, layout = plotter.GetPlotTraceAndLayout()
    return {'data': [trace], 'layout': layout}

if __name__ == '__main__':
    plotter = Plotter()
    print("start")
    target=app.run_server(debug=False)
    
    
    
    
    
import util

import plotly.graph_objs as go


class TraceDeterminer:
    def __init__(self):
        self.colors = ['red', 'royalblue']
        return    
    
    def GetTrace(self, xRange: list[int], yValueList: list[int], colorIndex: int) -> go.Scatter:
        trace = go.Scatter(
            x=list(xRange),
            y=yValueList,
            name='Random Data',
            mode='lines+markers',
            line=dict(color=self.colors[colorIndex], width=3)  
        )
        
        return trace
import util

import plotly.graph_objs as go


class LayoutDeterminer:
    def __init__(self) -> None:
        self.minimumXRange = 0
        self.maximumXRange = 22
        self.delayFactor = 0
        return
    
    def GetLayout(self, minimumXRange, maximumXrange) -> go.Layout:
        layout = go.Layout(
            title='Similarity - Time Step Graph',
            title_font=dict(size=24, family='Times New Roman'),
            
            xaxis=dict(
            title='Time Step',
            title_font=dict(size=24, family='Times New Roman'),
            tickfont=dict(size=20, family='Times New Roman'),
            autorange=True,
            range=[minimumXRange, maximumXrange],
            showgrid=True,
            gridcolor='white' 
            ),
            
            yaxis=dict(
            title='Similarity',
            title_font=dict(size=24, family='Times New Roman'),
            tickfont=dict(size=20, family='Times New Roman'),
            autorange=False,
            range=[0, 100],
            gridcolor='white'
            ),
            
            plot_bgcolor='lightgrey',
            transition={'duration': 1000}
        )
        
        return layout
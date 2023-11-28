import util
import time
import threading

from PlotApplication.PlotUpdator import PlotUpdator 
from PlotApplication.LayoutDeterminer import LayoutDeterminer 
from PlotApplication.TraceDeterminer import TraceDeterminer 
import plotly.graph_objs as go



class Plotter:
    def __init__(self) -> None:
        self.valueUpdator = PlotUpdator()    
        self.callCount = 0
        self.trace = None
        self.layout = None
        pass
    
    
    def ThearingTraceAndLayout(self) -> None:   
        while True:
            self.callCount = (self.callCount + 1) % 2
            xRange, yValueList, minimumXRange, maximumXRange, colorIndex = self.__GetPlotData()
            self.trace = TraceDeterminer().GetTrace(xRange, yValueList, colorIndex)
            self.layout = LayoutDeterminer().GetLayout(minimumXRange, maximumXRange)
            time.sleep(0.1)
        return
    
    def GetPlotTraceAndLayout(self) -> tuple[go.Scatter, go.Layout]:
        if (self.trace == None or self.layout == None):
            threading.Thread(target=self.ThearingTraceAndLayout()).start()  
            
        return self.trace, self.layout
        
    def __GetPlotData(self) -> tuple[list[int], list[int], int, int]:        
        xRange, minimumXRange, maximumXrange = self.valueUpdator.GetXRange()
        yValueList, colorIndex = self.valueUpdator.GetYValueList()   
        return xRange, yValueList, minimumXRange, maximumXrange, colorIndex
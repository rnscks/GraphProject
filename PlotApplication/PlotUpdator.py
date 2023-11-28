import util

from PlotApplication.RangeUpdator import RangeUpdator
from PlotApplication.ArduinoSerialConector import ArduinoSerialConnector
import torch
import torch.nn as nn   
import torch.nn.functional as F 
from PlotApplication.BFS import BFS

class ANN(nn.Module):
    def __init__(self, stateSize, actionSize):
        super(ANN, self).__init__()
        self.fc1 = nn.Linear(stateSize, 128)
        self.fc2 = nn.Linear(128, 128)
        self.fc3 = nn.Linear(128, actionSize)
        return

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = torch.sigmoid(self.fc3(x))
        return x
    
    
class PlotUpdator:
    def __init__(self) -> None:
        self.rangeDeterminer  = RangeUpdator()
        self.yValueList: list[int] = [0 for i in range(32)]
        self.model = self.__InitANNModel()  
        self.bfs = BFS(self.model)  
        pass
    
    def __InitANNModel(self):   
        model = ANN(4,1)  # 동일한 모델 구조
        model.load_state_dict(torch.load('model.pth'))
        return model
            
    def GetYValueList(self) -> tuple[list[int], bool]:
        serialSensorData = None
        while (serialSensorData is None):
            serialSensorData = ArduinoSerialConnector().GetSerialData()
            bfsResult = self.bfs.Run(serialSensorData[0],serialSensorData[1],serialSensorData[2],serialSensorData[3])
            if (serialSensorData is not None):
                break
        
        self.yValueList.pop(0)
        self.yValueList.append(bfsResult[1]) 
        if (bfsResult[0] == True):
            colorIndex = 1
        else:
            colorIndex = 0
        return self.yValueList, colorIndex
    
    def GetXRange(self) -> tuple[list[int], int, int]:
        minimumXRange, maxinumXRange = self.rangeDeterminer.GetRange()
        xRange = range(minimumXRange, maxinumXRange)
        return xRange, minimumXRange, maxinumXRange

if (__name__ == '__main__'):
    plotUpdator = PlotUpdator()
    print(plotUpdator.GetYValueList())
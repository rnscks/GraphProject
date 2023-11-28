import pandas as pd
from ArduinoSerialConector import ArduinoSerialConnector    

class DataFrameMaker:
    def __init__(self):
        self.dictforDataFrame = {"v1": [], "v2": [], "v3": [], "v4": [], "boarding number": []}
        return
    
    def AppendDatatoDataFrame(self, vectorList: list[int], boardingNumber: int) -> None:
        self.dictforDataFrame['v1'].append(vectorList[0])
        self.dictforDataFrame['v2'].append(vectorList[1])
        self.dictforDataFrame['v3'].append(vectorList[2])
        self.dictforDataFrame['v4'].append(vectorList[3])
        self.dictforDataFrame['boarding number'].append(boardingNumber)
        return

    def SaveDataFrameToExcel(self, fileName: str) -> None:
        pd.DataFrame(self.dictforDataFrame).to_excel(fileName, index=False)
        return 
        
        
        
arduinoSerialConnector = ArduinoSerialConnector()
dfm = DataFrameMaker()

for i in range(20):
    boardingNumber = int(input())
    arduinoSerialConnector.arduinoSerial.open()
    arduinoSerialConnector.arduinoSerial.reset_output_buffer()
    arduinoSerialConnector.arduinoSerial.reset_input_buffer()

    for j in range(200):
        sensorData = arduinoSerialConnector.GetSerialData()
        if (sensorData is None):
            continue
        dfm.AppendDatatoDataFrame(sensorData, boardingNumber)   
        print(".", end="")
    arduinoSerialConnector.arduinoSerial.reset_output_buffer()
    arduinoSerialConnector.arduinoSerial.reset_input_buffer()
    arduinoSerialConnector.arduinoSerial.close()

dfm.SaveDataFrameToExcel("test.xlsx")
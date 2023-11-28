import util
import threading
import serial
from typing import Optional
from PlotApplication.SerialDataParser import SerialDataParser

class ArduinoSerialConnector:
    def __init__(self) -> None:
        self.arduinoSerial = serial.Serial('COM4', 9600)
        # self.arduinoSerial.close()
        return
    
    def GetSerialData(self) -> Optional[list[int]]:
        #self.arduinoSerial.open()
        serialStringData = self.arduinoSerial.readline().decode('utf-8').split()
        serialDataParser = SerialDataParser()
        
        
        return serialDataParser.Parsing(serialStringData)
        

        
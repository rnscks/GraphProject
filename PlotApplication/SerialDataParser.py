import util

from typing import Optional

class SerialDataParser:
    def __init__(self) -> None:
        pass
    
    def Parsing(self, serialStringData) -> Optional[str]:        
        if (serialStringData is None or len(serialStringData) != 12):
            return None
        serialStringData = list(map(int, serialStringData))
        return serialStringData[-4:]
 
    
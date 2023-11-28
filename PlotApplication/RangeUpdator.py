import util

class RangeUpdator:
    def __init__(self) -> None:
        self.minimumXRange = 0
        self.maximumXRange = 31
        self.delayFactor = 0
        return
    
    def GetRange(self) -> tuple[int, int]:
        self.minimumXRange += 1
        self.maximumXRange += 1
        
        if (self.maximumXRange > 999):
            self.minimumXRange = 0
            self.maximumXRange = 31 
        
        return self.minimumXRange, self.maximumXRange
    
    
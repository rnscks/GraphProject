from collections import deque  
import torch

class BFS:
    def __init__(self, model) -> None:
        self.model = model
        self.closed = set() 
        
        pass
    
    def __NextState(self, pos):
        nextState = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if (i == j == k == l == 0):
                            continue    
                        if (pos[0]+i < 0 or pos[1]+j < 0 or pos[2]+k < 0 or pos[3]+l < 0):
                            continue   
                        if (pos[0] + i > 70 or pos[1] + j > 70 or pos[2] + k > 70 or pos[3] + l > 70):
                            continue 
                        nextState.append((pos[0]+i, pos[1]+j, pos[2]+k, pos[3]+l))  
        return nextState
    
    def Run(self, v1,v2,v3,v4):
        self.model.eval()
        qeueu = deque([])
        count = 0 
        qeueu.append((v1,v2,v3,v4)) 
        
        while (len(qeueu) != 0):    
            pos = qeueu.popleft()
            self.closed.add(pos)
            
            count += 1
            
            if (count > 100):
                break
            
            for nxt in self.__NextState(pos):
                if (nxt in self.closed):
                    continue
                
                with torch.no_grad():
                    input = torch.tensor(list(nxt)).float()
                    outputs:torch.Tensor = self.model(input)
                    if (outputs.item() == 1):
                        return True, count
                    elif (outputs.item() == 0): 
                        return False, count
                
                qeueu.append(nxt)
                
        with torch.no_grad():
            input = torch.tensor(list(pos)).float()
            outputs:torch.Tensor = self.model(input)
            if (outputs.item() < 0.6):
                return False, 100
            else:
                return True, 100
    
    
    
     
from enum import Enum

class allStates(Enum):
    MINING = 'MINING_STATE'
    GBH = 'GET_BLOCK_HASHES'
    GB = 'GET_BLOCK'
    IDLE = 'IDLE'
    
class State:
    def __init__(self):
        self.currentState = allStates.IDLE
    
    def setCurrentState(self, state):
        if state == "1":
            self.currentState = allStates.MINING
        elif state == "2":
            self.currentState = allStates.GBH
        elif state == "3":
            self.currentState = allStates.GB
        else:
            print("!!!!!!!!!!!WRONG STATE PARAMS")
    
    def getCurrentState(self):
        return self.currentState
    
    # def handleMiningState(self):


        
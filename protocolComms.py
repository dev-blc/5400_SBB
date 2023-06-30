import threading
import state
states = state.allStates
class protocolComms:
    def __init__(self, sI, pI) -> None:
        self.stateInstance = sI
        self.protocolInstance = pI
        handler = threading.Thread(target=self.executeStateHandlers)
        handler.start()
    def executeStateHandlers(self):
        state = self.stateInstance.getCurrentState()
        if state == states.MINING:
            print("+++++++InsideMining")
            self.protocolInstance.createProtocolPayload("a", None) 

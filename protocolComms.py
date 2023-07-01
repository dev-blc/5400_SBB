import threading
import time
import state
states = state.allStates
class protocolComms:
    def __init__(self, sI, pI, peerI) -> None:
        self.stateInstance = sI
        self.protocolInstance = pI
        self.peerInstance = peerI
    def executeStateHandlers(self):
        while True:
            state = self.stateInstance.getCurrentState()
            if state == states.MINING:
                print("+++++++InsideMining")
                msg = self.protocolInstance.createProtocolPayload("a", None)
                self.peerInstance.broadcastMessage(msg)
            elif state == states.GBH:
                print("+++++++InsideGBH")
                msg = self.protocolInstance.createProtocolPayload("h", None)
                self.peerInstance.broadcastMessage(msg)
            time.sleep(20)

    def broadcastDivert(self, msg):
        self.peerInstance.broadcastMessage(msg)
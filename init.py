import wallet
import block
import transaction
import miner
import chain
import threading
import time

class Node:
    def __init__(self):
        self.walletInstance = wallet.Wallet()
        wallet2 = wallet.Wallet()
        self.public_key_2 = wallet2.getPublicKey()
        self.public_key = self.walletInstance.getPublicKey()  
        # self.blockInstance = block.Block()
        self.chainInstance = chain.Chain()
        self.minerInstance = miner.Miner(self.walletInstance, self.chainInstance)
        # thread = threading.Thread(target=self.runMinerThread )#args= (minerInstance)
        # thread.start()
    # def runMinerThread(self):
    #     print("In run")
    #     self.minerInstance.run()
    def handleUserActions(self):
        self.minerInstance.addTxn(self.public_key,self.public_key_2)
        self.walletInstance.checkBalance(self.chainInstance)
    def getInstances(self):
        return self.walletInstance, self.chainInstance, self.minerInstance
# print("INIT FUNCTION OF SBB")
# print("STARTING IN DEFAULT CONFIG")
class util:
    def __init__(self):
        self.nodeInstance = None
    def startNode(self):
        self.nodeInstance = Node()
    def utilsCall(self):
        self.nodeInstance.handleUserActions()
    def fetchInstances(self):
        return self.nodeInstance.getInstances()

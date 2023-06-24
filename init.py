import wallet
import block
import transaction
import miner
import chain
import threading
import time

class Node:
    def __init__(self):
        self.walletInstance = None
        wallet2 = None
        self.public_key_2 = None
        self.public_key = None  
        # self.blockInstance = block.Block()
        self.chainInstance = None
        self.minerInstance = None
        # thread = threading.Thread(target=self.runMinerThread )#args= (minerInstance)
        # thread.start()
    # def runMinerThread(self):
    #     print("In run")
    #     self.minerInstance.run()
    def initInstances(self):
        self.walletInstance = wallet.Wallet()
        wallet2 = wallet.Wallet()
        self.public_key_2 = wallet2.getPublicKey()
        self.public_key = self.walletInstance.getPublicKey()  
        # self.blockInstance = block.Block()
        self.chainInstance = chain.Chain()
        self.minerInstance = miner.Miner(self.walletInstance, self.chainInstance, str(0))
    def handleUserActions(self):
        signature = self.walletInstance.getPrivateKey().sign((self.public_key).encode('utf-8'))
        self.minerInstance.addTxn(self.public_key,self.public_key_2, signature)
        self.walletInstance.getBalance()
    def getInstances(self):
        return self.walletInstance, self.chainInstance, self.minerInstance
# print("INIT FUNCTION OF SBB")
# print("STARTING IN DEFAULT CONFIG")
class util:
    def __init__(self):
        self.nodeInstance = None #Node()
    def startNode(self):
        self.nodeInstance = Node()
        self.nodeInstance.initInstances()
    def utilsCall(self):
        self.nodeInstance.handleUserActions()
    def fetchInstances(self):
        return self.nodeInstance.getInstances()

import hashlib
import json
import threading
import wallet
import block
import time 
import transaction
import chain

class MinerPoT:
    def __init__(self, walletI, chainI, pI, txnMode):
        self.walletInstance = walletI
        # self.blockInstance = blockI
        self.chainInstance = chainI
        self.protocolInstance = pI
        self.blockTime = []
        # msg = self.protocolInstance.createProtocolPayload("g", json.dumps({}))

        thread = threading.Thread(target=self.run)
        thread.start()
    
    def initProtocol(self):
        msg = self.protocolInstance.createProtocolPayload("g", json.dumps({}))
        return msg

    def calcTruncatedHash(self, publicKey):
        self.prevBlockHash = self.chainInstance.getLastBlock().get("blockHash")
        # self.publicKey = self.walletInstance.getPublicKey()
        concat = self.prevBlockHash + publicKey
        hashedConcat = hashlib.sha256(concat.encode()).hexdigest()
        truncatedHash = hashedConcat[-16:]
        return int(truncatedHash, 16)

    def run(self):
        self.bcount = 0
        nextMiner = 0
        while(True):
            peers = self.protocolInstance.getPeersPK()
            if len(set(peers)) == 2: #4 #HARDCODED
                min = self.calcTruncatedHash(peers[0]) #CAN ONLY GET AS MESG
                nextMiner = peers[0]
                count = 0
                for peer in peers:
                    temp = peer#self.calcTruncatedHash(peer.getPK())
                    if min > temp:
                        min = temp
                        nextMiner = peer
                        minPeer = count
                    count += 1
                time.sleep(4)
                payloadObj = {"nextMiner": nextMiner}
                if nextMiner == self.walletInstance.getPublicKey():
                    self.mineNextBlock()
                    # msg = self.protocolInstance.createProtocolPayload("n", json.dumps(payloadObj))

                else:
                    #peers[count].getMinerInstace().mineNextBlock(self.chainInstance)
                    # payloadObj = {"nextMiner": nextMiner}
                    msg = self.protocolInstance.createProtocolPayload("n", json.dumps(payloadObj))
            else:
                time.sleep(2)
            print("////",nextMiner)
            

    def mineNextBlock(self, chainI):
        self.txnInstance = transaction.Transaction()
        rewardTxn = self.addTxn(str(0),self.walletInstance.getPublicKey(), None)
        txnObj = self.txnInstance.getTxns()
        ts= time.time()
        self.blockInstance = block.Block()

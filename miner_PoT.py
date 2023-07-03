import hashlib
import json
import threading
import wallet
import block
import time 
import transaction
import chain
import blockUtil

class MinerPoT:
    def __init__(self, walletI, chainI, pI, peerI ,txnMode):
        self.walletInstance = walletI
        # self.blockInstance = blockI
        self.chainInstance = chainI
        self.protocolInstance = pI
        self.peerInstance = peerI
        self.blockTime = []
        # msg = self.protocolInstance.createProtocolPayload("g", json.dumps({}))

        thread = threading.Thread(target=self.run)
        thread.start()
    
    def initProtocol(self):
        msg = self.protocolInstance.createProtocolPayload("g", json.dumps({}))
        return msg

    def calcTruncatedHash(self, publicKey):
        
        bcount = self.chainInstance.getBlockCount()
        if bcount == 0:
            concat = "0" + publicKey
            hashedConcat = hashlib.sha256(concat.encode()).hexdigest()
            truncatedHash = hashedConcat[-16:]
            return int(truncatedHash, 16)
        # self.publicKey = self.walletInstance.getPublicKey()
        else :
            self.prevBlockHash = self.chainInstance.getLastBlock().get("blockHash")
            concat = self.prevBlockHash + publicKey
            hashedConcat = hashlib.sha256(concat.encode()).hexdigest()
            truncatedHash = hashedConcat[-16:]
            return int(truncatedHash, 16)

        
    def run(self):
        self.bcount = 0
        nextMiner = 0
        while(True):
            peers = self.protocolInstance.getPeersPK()
            print(set(peers))
            if len(set(peers)) == 2: #4 #HARDCODED
                min = self.calcTruncatedHash(peers[0]) #CAN ONLY GET AS MESG
                nextMiner = peers[0]
                count = 0
                for peer in peers:
                    temp = self.calcTruncatedHash(peer)
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
                msg = self.initProtocol()
                self.peerInstance.broadcastMessage(msg)

            print("////",nextMiner)
            

    def mineNextBlock(self):
        self.txnInstance = transaction.Transaction()
        rewardTxn = self.addTxn(str(0),self.walletInstance.getPublicKey(), None)
        txnObj = self.txnInstance.getTxns()
        ts= time.time()
        self.blockInstance = block.Block()
        bno = self.chainInstance.getBlockCount()
        if bno == 0 : 
            self.blockInstance.addBlock(0,ts,txnObj)
            # print("inside0")
            # count += 1
        else:
            chainBlock = self.chainInstance.getLastBlock()
            prev = chainBlock.get("blockHash")
            # self.bno = chainBlock.get("block_no") + 1

            self.blockInstance.addBlock(prev,ts,txnObj)
        bHash = self.blockInstance.calculateHash()
        blockObj = self.chainInstance.getLastBlock()
        isValid = blockUtil.validateBlock(blockObj)
        if isValid:
            print("BLOCK FOUND =====> ", bHash)
            print("BLOCK ====> " , blockObj)
            self.chainInstance.addBlock(blockObj)
            payloadObj = {"block": blockObj}
            msg = self.protocolInstance.createProtocolPayload("z",  json.dumps(payloadObj))
            self.peerInstance.broadcastMessage(msg)
        
        


        


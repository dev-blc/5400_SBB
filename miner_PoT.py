import hashlib
import threading
import wallet
import block
import time 
import transaction
import chain

class MinerPoT:
    def __init__(self, walletI, chainI):
        self.walletInstance = walletI
        # self.blockInstance = blockI
        self.chainInstance = chainI
        self.blockTime = []
        # thread = threading.Thread(target=self.run)
        # thread.start()

    def calcTruncatedHash(self, publicKey):
        self.prevBlockHash = self.chainInstance.getLastBlock().get("block_no")
        # self.publicKey = self.walletInstance.getPublicKey()
        concat = self.prevBlockHash + publicKey
        hashedConcat = hashlib.sha256(concat.encode()).hexdigest()
        truncatedHash = hashedConcat[-16:]
        return int(truncatedHash, 16)

    def run(self):
        self.bcount = 0
        while(True):
            peers = peerInstance.getPeers()
            min = self.calcTruncatedHash(peers[0].getPK())
            nextMiner = peers[0].getPK()
            count = 0
            for peer in peers:
                temp = self.calcTruncatedHash(peer.getPK())
                if min > temp:
                    min = temp
                    nextMiner = peer.getPK()
                    minPeer = count
                count += 1
            time.sleep(4)
            if nextMiner == self.walletInstance.getPublicKey():
                self.mineNextBlock()
            else:
                peers[count].getMinerInstace().mineNextBlock(self.chainInstance)

    def mineNextBlock(self, chainI):
        self.txnInstance = transaction.Transaction()
        rewardTxn = self.addTxn(str(0),self.walletInstance.getPublicKey(), None)
        txnObj = self.txnInstance.getTxns()
        ts= time.time()
        self.blockInstance = block.Block()

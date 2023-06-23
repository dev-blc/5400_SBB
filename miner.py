import threading
import wallet
import block
import time 
import transaction
import chain
# chainInstance = chain.Chain()
# # create a new Wallet instance
# walletInstance = wallet.Wallet()
# # blockInstance = block.Block()
# blockInstance = block.Block()
class Miner:
    def __init__(self, walletI, chainI):
        self.walletInstance = walletI
        # self.blockInstance = blockI
        self.chainInstance = chainI
        thread = threading.Thread(target=self.run)
        thread.start()

    def run(self):
        count = 0
        while True:
            self.txnInstance = transaction.Transaction()
            # txnHash = txnInstance.calculateHash()
            # txnObj = txnInstance.getCurrentTxn()
            rewardTxn = self.addTxn(str(0),self.walletInstance.getPublicKey())
            txnObj = self.txnInstance.getTxns()
            ts= time.time()
            self.blockInstance = block.Block()
            if count == 0 : 
                self.blockInstance.addBlock(0,0,ts,txnObj)
                print("inside0")
                count += 1
            else:
                chainBlock = self.chainInstance.getLastBlock()
                prev = chainBlock.get("blockHash")
                self.bno = chainBlock.get("block_no") + 1
                self.blockInstance.addBlock(self.bno,prev,ts,txnObj)
                # print(prev)
            bcount = 0 

            while(True):
                tempHash = self.blockInstance.calculateHash()
                if(tempHash[:5] == "00000"):
                    blockObj = self.blockInstance.getCurrentBlock()

                    print("******************************************")
                    print("MINED A NEW BLOCK ====> ", tempHash)
                    print("BLOCK CONTENTS ====>",blockObj)
                    print("******************************************")
                    self.chainInstance.addBlock(blockObj)

                    # print(chainInstance.getLastBlock())
                    break
                else:
                    self.blockInstance.increaseNonce()
                    bcount += 1
                    # print(bcount)
        # print(count)

    def addTxn(self, sender, to):
        # txnHash = self.txnInstance.calculateHash()
        self.txnInstance.createTxn(str(sender), str(to))
        print("NEW TRANSACTION REQUEST FROM ============>",sender)
        # print("bno",self.bno)
        return self.txnInstance.getCurrentTxn()


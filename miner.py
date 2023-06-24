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
        self.blockTime = []
        thread = threading.Thread(target=self.run)
        thread.start()

    def run(self):
        count = 0
        while True:
            self.txnInstance = transaction.Transaction()
            # txnHash = txnInstance.calculateHash()
            # txnObj = txnInstance.getCurrentTxn()
            rewardTxn = self.addTxn(str(0),self.walletInstance.getPublicKey(), None)
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
            start = time.time()
            while(True):
                tempHash = self.blockInstance.calculateHash()
                if(tempHash[:5] == "00000"):
                    end = time.time()
                    self.blockTime.append(end - start)
                    print(">>>>>>>>>>>>>> Elapsed time: {:.2f} seconds".format(self.blockTime[-1]))
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
    def getBlockTime(self):
        return self.blockTime
    def addTxn(self, sender, to, sign):
        # txnHash = self.txnInstance.calculateHash()
        # self.txnInstance.createTxn(str(sender), str(to))
        # print("NEW TRANSACTION REQUEST FROM ============>",sender)
        # print("bno",self.bno)

        if sender == str(0):
            self.txnInstance.createTxn(str(sender), str(to))
            print("************** MINING REWARD TXN **************")
        else:
            isValid = self.walletInstance.verifySign(sign)
            if isValid:
                if self.walletInstance.checkBalance(self.chainInstance) >= 1:
                    self.txnInstance.createTxn(str(sender), str(to))
                else: 
                    print("************** BALANCE NOT ENOUGH **************")
            else:
                print("************** INVALID SIGNATURE **************")
        return self.txnInstance.getCurrentTxn()


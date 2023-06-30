import threading
import wallet
import block
import time 
import transaction
import chain
import transactionUTXO
import accountDB
# chainInstance = chain.Chain()
# # create a new Wallet instance
# walletInstance = wallet.Wallet()
# # blockInstance = block.Block()
# blockInstance = block.Block()
class Miner:
    def __init__(self, walletI, chainI, txnModel):
        self.walletInstance = walletI
        # self.blockInstance = blockI
        self.chainInstance = chainI
        self.dbInstance = accountDB.AccountModel(chainI)

        self.blockTime = []
        self.txnType = txnModel
        thread = threading.Thread(target=self.run)
        thread.start()


    def run(self):
        count = 0
        while True:
            # ADD TXN MODEL SELECTION
            if self.txnType == "0":
                #acc
                self.txnInstance = transaction.Transaction(self.dbInstance)
            else:
                #utxo
                self.txnInstance = transactionUTXO.Transaction(self.chainInstance)
            # self.txnInstance = transaction.Transaction()
            # txnHash = txnInstance.calculateHash()
            # txnObj = txnInstance.getCurrentTxn()
            self.txnInstance.sendMinerRewards(self.walletInstance.getPublicKey())
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
    def getAccountBalances(self):
        self.txnInstance.getBalances()
    def getBlockTime(self):
        return self.blockTime
    def addTxn(self, sender, to, sign):
        # txnHash = self.txnInstance.calculateHash()
        # self.txnInstance.createTxn(str(sender), str(to))
        # print("NEW TRANSACTION REQUEST FROM ============>",sender)
        # print("bno",self.bno)
        
        isValid = self.walletInstance.verifySign(sign)
        if isValid:
            if self.walletInstance.checkBalance(self.chainInstance) >= 1:
                self.txnInstance.createTxn(str(sender), str(to), sign )
            else: 
                print("************** BALANCE NOT ENOUGH **************")
        else:
            print("************** INVALID SIGNATURE **************")

        return self.txnInstance.getCurrentTxn()


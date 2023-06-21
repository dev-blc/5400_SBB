
import threading
import wallet
import block
import time 
import transaction
import chain
chainInstance = chain.Chain()
# create a new Wallet instance
walletInstance = wallet.Wallet()
# blockInstance = block.Block()
blockInstance = block.Block()
class Miner:
    def __init__(self):
        thread = threading.Thread(target=self.run())
        thread.start()

    def run(self):
        count = 0
        while True:
            txnInstance = transaction.Transaction(str(0),walletInstance.getPublicKey())
            txnHash = txnInstance.calculateHash()
            txnObj = txnInstance.getCurrentTxn()
            ts= time.time()
            if count == 0 : 
                blockInstance.addBlock(0,ts,txnObj)
                # print("inside0")
                count += 1
            else:
                chainBlock = chainInstance.getLastBlock()
                prev = chainBlock.get("blockHash")
                blockInstance.addBlock(prev,ts,txnObj)
                # print(prev)
            bcount = 0 

            while(True):
                tempHash = blockInstance.calculateHash()
                if(tempHash[:6] == "000000"):
                    blockObj = blockInstance.getCurrentBlock()
                    print("MINED A NEW BLOCK ====> ", tempHash)
                    print("BLOCK CONTENTS ====>",blockObj)
                    chainInstance.addBlock(blockObj)

                    # print(chainInstance.getLastBlock())
                    break
                else:
                    blockInstance.increaseNonce()
                    bcount += 1
                    # print(bcount)
        # print(count)
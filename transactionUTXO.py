import hashlib
# UTXO TXN
class Transaction:
    def __init__(self, chainI):
        self.fromAccount = str(0)
        self.toAccount = str(0)
        self.transactions = [{}]
        self.spentMark = None
        self.chainInstance = chainI
    def sendMinerRewards(self,to):
        self.fromAccount = str(0)
        self.toAccount = to
        self.txnHash = hashlib.sha256(repr(self.fromAccount + self.toAccount).encode('utf-8')).hexdigest()
        self.transactions.append({
            "TXN_Hash": self.txnHash,
            "From" : self.fromAccount,
            "To" : self.toAccount,
            "UTXO_SPENT" : False
        })
    def createUTXOTxn(self, sender, to):
        self.fromAccount = sender
        self.toAccount = to
        self.txnHash = hashlib.sha256(repr(self.fromAccount + self.toAccount).encode('utf-8')).hexdigest()
        self.spentMark = False
        self.transactions.append({
            "TXN_Hash": self.txnHash,
            "From" : self.fromAccount,
            "To" : self.toAccount,
            "UTXO_SPENT" : False
        })
    def createTxn(self, sender, to):
        index = 0 
        chain = self.chainInstance.getChain()
        for block in chain:
            # print("////In Block", block.get("block_no") )
            txns = block.get("Transaction")
            # txn = txns[-1]
            flag = False
            for txn in txns:
                if txn.get("To") == sender:
                    if txn.get("UTXO_SPENT") == False:
                        # balance += 1
                        self.transactions[index]["UTXO_SPENT"] = True
                        print("|||||||| UTXO SPENT ===>",txn)
                        self.spentMark = True
                        self.createUTXOTxn(sender, to)
                        index +=1
                        flag = True
                        break
                    else:
                        index += 1
            if flag == False:
                print(" !!!!!!!!!!!!!!!!! NO UNSPENT UTXO MINE MORE !!!!!!!!!!!!!!!!!")
            else :
                break
    def getCurrentTxn(self):
        return {
            "TXN_Hash": self.txnHash,
            "From" : self.fromAccount,
            "To" : self.toAccount,
            "UTXO_SPENT": self.spentMark
        }
    def getTxns(self):
        return self.transactions
import hashlib
# UTXO TXN
class Transaction:
    def __init__(self):
        self.fromAccount = str(0)
        self.toAccount = str(0)
        self.transactions = [{}]
        self.spentMark = False
    def createTxn(self, sender, to):
        self.fromAccount = sender
        self.toAccount = to
        self.txnHash = hashlib.sha256(repr(self.fromAccount + self.toAccount).encode('utf-8')).hexdigest()
        self.transactions.append({
            "TXN_Hash": self.txnHash,
            "From" : self.fromAccount,
            "To" : self.toAccount,
            "UTXO_SPENT" : False
        })
    def spend(self):
        index = 0 
        for txn in self.transactions:
            if txn.get("UTXO_SPENT") == False:
                # balance += 1
                self.transactions[index]["UTXO_SPENT"] = True
                index +=1
                break
            else:
                index += 1
            
    def getCurrentTxn(self):
        return {
            "TXN_Hash": self.txnHash,
            "From" : self.fromAccount,
            "To" : self.toAccount
        }
    def getTxns(self):
        return self.transactions
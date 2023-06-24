import hashlib
# UTXO TXN
class Transaction:
    def __init__(self):
        self.fromAccount = str(0)
        self.toAccount = str(0)
        self.transactions = [{}]
        # self.spentMark = None
    def createTxn(self, sender, to):
        self.fromAccount = sender
        self.toAccount = to
        self.txnHash = hashlib.sha256(repr(self.fromAccount + self.toAccount).encode('utf-8')).hexdigest()
        self.transactions.append({
            "TXN_Hash": self.txnHash,
            "From" : self.fromAccount,
            "To" : self.toAccount,
            # "UTXO_SPENT" : False
        })
        # self.balances[to] += 1
        # self.balances[sender] -= 1
    # def addToBalances(self, chainI, sender):
    #     chainI.addBalance(sender)
    # def getBalances(self):
    #     return self.balances
    def getCurrentTxn(self):
        return {
            "TXN_Hash": self.txnHash,
            "From" : self.fromAccount,
            "To" : self.toAccount
        }
    def getTxns(self):
        return self.transactions
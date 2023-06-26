import hashlib
# ACCOUNT MODEL TXN

class Transaction:
    def __init__(self, dbI):
        self.fromAccount = str(0)
        self.toAccount = str(0)
        self.transactions = [{}]
        self.dbInstance = dbI

    def sendMinerRewards(self,to):
        self.fromAccount = str(0)
        self.toAccount = to
        self.txnHash = hashlib.sha256(repr(self.fromAccount + self.toAccount).encode('utf-8')).hexdigest()
        self.transactions.append({
            "TXN_Hash": self.txnHash,
            "From" : self.fromAccount,
            "To" : self.toAccount
        })
        self.dbInstance.minerRewardUpdate(to)

        #get balance and update
        # self.chainInstance.balances.update({str(to): 1})
    def createTxn(self, sender, to):
        self.fromAccount = sender
        self.toAccount = to
        self.txnHash = hashlib.sha256(repr(self.fromAccount + self.toAccount).encode('utf-8')).hexdigest()
        self.transactions.append({
            "TXN_Hash": self.txnHash,
            "From" : self.fromAccount,
            "To" : self.toAccount
        })
        self.dbInstance.transferBalance(sender, to)
        # self.chainInstance.balances.update({str(to): 1})
    # def addToBalances(self, chainI, sender):
    #     chainI.addBalance(sender)
    # def getBalances(self):
    #     return self.chainInstance.balances
    def getCurrentTxn(self):
        return {
            "TXN_Hash": self.txnHash,
            "From" : self.fromAccount,
            "To" : self.toAccount
        }
    def getTxns(self):
        return self.transactions
import hashlib
class Transaction:
    def __init__(self, sender, to):
        self.fromAccount = sender
        self.toAccount = to
    def calculateHash(self):
        self.txnHash = hashlib.sha256(repr(self.fromAccount + self.toAccount).encode('utf-8')).hexdigest()
        return self.txnHash
    def getCurrentTxn(self):
        return {
            "From" : self.fromAccount,
            "To" : self.toAccount
        }
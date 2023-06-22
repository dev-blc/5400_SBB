import hashedContent
import hashlib
# hasher = hashlib.sha256()

class Block:
    def __init__(self):
        self.prevHash = 0
        self.nonce = 0
        self.timestamp = 0
        self.transactions = [{}]
        self.blockNo = 0
        # self.hash = 0
    
    def addBlock(self, bno, prev, ts, transactions):
        self.prevHash = prev
        # self.nonce = 0
        self.timestamp = ts
        self.transactions.append(transactions)
        self.blockNo = bno #+= 1

    def increaseNonce(self):
        self.nonce += 1
        return self.nonce

    def calculateHash(self):
        hahsedTxns = hashlib.sha256(repr(self.transactions).encode('utf-8')).hexdigest()
        self.content = hashlib.sha256(repr(str(self.prevHash) + str(self.nonce) + str(self.timestamp)).encode('utf-8')).hexdigest()
        self.hash = hashlib.sha256(repr(self.content + hahsedTxns).encode('utf-8')).hexdigest()
        return self.hash
    
    def getCurrentBlock(self):
        blockObj = {
            "block_no" : self.blockNo,
            "nonce" : self.nonce,
            "prevHash" : self.prevHash,
            "Transaction" : self.transactions,
            "blockHash" : self.hash
        }
        return blockObj

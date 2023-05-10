import hashedContent
import hashlib
# hasher = hashlib.sha256()

class Block:
    def __init__(self):
        self.prevHash = 0
        self.nonce = 0
        self.timestamp = 0
    def increaseNonce(self):
        self.nonce += 1
        return self.nonce

    def calculateHash(self):
        self.content = self.prevHash + self.nonce + self.timestamp 
        self.hash = hashlib.sha256(repr(self.content).encode('utf-8')).hexdigest()
        return self.hash


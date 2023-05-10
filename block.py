import hashedContent
import hashlib


class Block:
    def __init__(self):
        self.prevHash = 0
        self.nonce = 0
        self.timestamp = 0
    def increaseNonce(self):
        self.nonce += 1
        return self.nonce

    def calculateHash(self):
        self.hash = hashlib.sha256(hashedContent.encode('utf-8')).hexdigest()
        return self.hash


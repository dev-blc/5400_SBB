import block
blockInstance = block.Block()

class Chain:
    def __init__(self):
        self.blocks = []
        self.balances = {None}
        
    
    # def addBalance(self, publicKey):
    #     self.balances["PublicKey"] = publicKey
    #     self.balances["Balance"] += 1
    

    def addBlock(self, newBlock):
        self.blocks.append(newBlock)
    
    def getLastBlock(self):
        return self.blocks[-1]
    
    def getChain(self):
        return self.blocks
    
    def getBlockCount(self):
        return len(self.blocks)
    
    def getBlockHashes(self):
        blkHashes = []
        for block in self.blocks:
            blkHashes.append(block.get("blockHash"))
        return blkHashes
        
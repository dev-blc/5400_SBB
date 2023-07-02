import block
blockInstance = block.Block()

class Chain:
    def __init__(self):
        self.blocks = []
        self.balances = {None}
        self.altBlocks = []
        
    
    # def addBalance(self, publicKey):
    #     self.balances["PublicKey"] = publicKey
    #     self.balances["Balance"] += 1
    

    def addBlock(self, newBlock):
        self.blocks.append(newBlock)

    def addPeerBlock(self, newBlock):
        self.altBlocks.append(newBlock)
    
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
    
    def getBlock(self, hash):
        for block in self.blocks:
            if block.get("blockHash") == hash:
                return block
        
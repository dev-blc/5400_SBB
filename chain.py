import block
blockInstance = block.Block()

class Chain:
    def __init__(self):
        self.blocks = []
    
    def addBlock(self, newBlock):
        self.blocks.append(newBlock)
    
    def getLastBlock(self):
        return self.blocks[-1]
    
    def getChain(self):
        return self.blocks
        
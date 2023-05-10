import block
blockInstance = block.Block()

class Chain:
    def __init__(self):
        self.blocks = []
    
    def addBlock(self):
        self.tempBlock = block.Block()
        self.tempBlock
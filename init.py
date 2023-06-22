import wallet
import block
import transaction
import miner
import chain



class Node:
    def __init__(self):
        walletInstance = wallet.Wallet()
        self.public_key = walletInstance.getPublicKey()  
        blockInstance = block.Block()
        chainInstance = chain.Chain()
        minerInstance = miner.Miner()
        
    
    def 

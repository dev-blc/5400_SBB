import wallet
import block
import transaction
import miner
import chain

# chainInstance = chain.Chain()
# minerInstance = miner.Miner()


class Node:
    def __init__(self):
        walletInstance = wallet.Wallet()
        self.public_key = walletInstance.getPublicKey()  
        

    def 

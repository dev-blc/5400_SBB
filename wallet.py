import ecdsa

class Wallet:
    def __init__(self):
        self.sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        self.vk = self.sk.verifying_key
        self.balance = 0

    def getPublicKey(self):
        return self.vk.to_string().hex()
    
    def checkBalance(self,chainI):
        chain = chainI.getChain()
        #parse chain
        for block in chain:
            txns = block.get("Transaction")
            txn = txns[-1]
            if txn.get("To") == self.vk.to_string().hex():
                self.balance += 1
        return self.balance



    
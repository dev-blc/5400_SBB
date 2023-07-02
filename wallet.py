import ecdsa

class Wallet:
    def __init__(self):
        self.sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        self.vk = self.sk.verifying_key
        self.balance = int(0)
        self.balances = {None} # SHOULD IT BE HERE?
    def getPublicKey(self):
        return self.vk.to_string().hex()
    def getPrivateKey(self):
        return self.sk
    def verifySign(self, sign):
        return self.vk.verify(sign, (self.vk.to_string().hex()).encode('utf-8'))
    def checkBalance(self,chainI):
        chain = chainI.getChain()
        #parse chain
        temp = 0
        for block in chain:
            # print("////In Block", block.get("block_no") )
            txns = block.get("Transactions")
            # txn = txns[-1]
            for txn in txns:
                if txn.get("To") == self.vk.to_string().hex():
                    # print("////Found To")
                    temp += 1
                elif txn.get("From") == self.vk.to_string().hex():
                    # print("////Found From")
                    temp -= 1
        print("****************BALANCE****************")
        print("=============>",temp)
        self.balance = temp
        return temp
    # def getBalance(self):
    #     return self.balance


    
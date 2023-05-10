import ecdsa

class Wallet:
    def __init__(self):
        self.sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        self.vk = self.sk.verifying_key

    def getPublicKey(self):
        return self.vk.to_string().hex()
    #checkBalance

    
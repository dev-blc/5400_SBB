
import wallet
import block
# create a new Wallet instance
walletInstance = wallet.Wallet()
blockInstance = block.Block()

# get the public key
public_key = walletInstance.getPublicKey()

# print(public_key)

print(blockInstance.increaseNonce())
print(blockInstance.increaseNonce())

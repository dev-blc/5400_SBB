
import wallet
import block
# create a new Wallet instance
walletInstance = wallet.Wallet()
blockInstance = block.Block()

# get the public key
public_key = walletInstance.getPublicKey()

# print(public_key)

# print(blockInstance.increaseNonce())
# print(blockInstance.calculateHash())
# print(blockInstance.increaseNonce())
# print(blockInstance.calculateHash())

count = 0
while(True):
    tempHash = blockInstance.calculateHash()
    if(tempHash[:4] == "0000"):
        print(tempHash)
        break
    else:
        blockInstance.increaseNonce()
        count += 1
        print(count)
print(count)
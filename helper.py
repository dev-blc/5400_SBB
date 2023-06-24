import subprocess
import wallet
import block
import miner
import chain 
import time 
import threading
import multiprocessing
import miner_PoT
# create a new Wallet instance
walletInstance = wallet.Wallet()
blockInstance = block.Block()
chainInstance = chain.Chain()
wallet2 = wallet.Wallet()

minerInstance = miner.Miner(walletInstance, chainInstance)
# get the public key
public_key = walletInstance.getPublicKey()
public_key_2 = wallet2.getPublicKey()
print(public_key)
print(public_key_2)

# minerPOT = miner_PoT.MinerPoT(walletInstance, chainInstance)
# print(minerPOT.calcTruncatedHash(public_key))

def runMiner():
    # print("In run")
    minerInstance.run()

# def handleUserActions():
#     # print("In hua")
#     minerInstance.addTxn(public_key,public_key_2)

# # print(blockInstance.increaseNonce())
# # print(blockInstance.calculateHash())
# # print(blockInstance.increaseNonce())
# # print(blockInstance.calculateHash())

# # count = 0
# # while(True):
# #     tempHash = blockInstance.calculateHash()
# #     if(tempHash[:4] == "0000"):
# #         print(tempHash)
# #         break
# #     else:
# #         blockInstance.increaseNonce()
# #         count += 1
# #         # print(count)
# # print(count)
# # # minerInstance.__init__()
# thread = threading.Thread(target=runMiner )#args= (minerInstance)
# thread.start()
# # command = ["osascript", "-e", 'tell app "Terminal" to do script "python -c \\"import main; main.runMiner()\\""']
# # subprocess.Popen(command)
# # print("anyhting")
# # time.sleep(10)
# print("After10")
# # thread2 = threading.Thread(target=handleUserActions) #, args= (minerInstance)
# # thread2.start()

# # process1 = multiprocessing.Process(target=runMiner, args= (minerInstance))
# # process1.start()
# minerInstance.addTxn(public_key,public_key_2)
# # print("****************BALANCE*********")
# # print("=============>",walletInstance.checkBalance(chainInstance))
# time.sleep(10)

# print("****************BALANCE*********")
# print("=============>",walletInstance.checkBalance(chainInstance))
# print("=============>",chainInstance.getLastBlock().get("block_no"))
# # # print("anyhting")
# # while True:
# #     choice = input("Do you wnat to check balance 9 to terminate")
# #     if choice == 1:
# #         print("****************BALANCE*********")
# #         print("=============>",walletInstance.checkBalance(chainInstance))
# #     elif choice == 9:
# #         break

# def utilsCall():
#     print("****************BALANCE*********")
#     print("=============>",walletInstance.checkBalance(chainInstance))
#     print("=============>",chainInstance.getLastBlock().get("block_no"))
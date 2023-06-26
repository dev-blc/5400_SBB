import block
import threading
import wallet
import time 
import transaction
import chain
import miner
import miner_PoT
import init 
import utils
import psutil
# initInstance = init.util()
# walletInstance = wallet.Wallet()
chainInstance = chain.Chain()
minerChoice = None
def printCPU():
        cpu_percent = psutil.cpu_percent()
        print(f"CPU Usage: {cpu_percent}%")
while True:
    printCPU()
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print(":::::::::::::::::::::::::::::::::::::: SBB BLOCKCHAIN ::::::::::::::::::::::::::::::::::::::")
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print("===> ENTER 0 TO START THE CHAIN IN DEFAULT CONFIGURATION")
    print("===> ENTER 1 TO START WITH CUSTOM CONFIGURATION")
    print("===> ENTER X to STOP AND EXIT")
    choice = input("YOUR CHOICE ==> ")
    if choice == "0":
        utils.menu()
    elif choice == "1": 
        print(" ------------------------ CONFIGURATION ------------------------ ")
        print(" ------------ CHOOSE BETWEEN THE OPTIONS WITH 0 & 1 ------------ ")
        minerChoice = input (" ---- CONSENSUS ALGORITHM (PoW(0) or PoT(1)) ===> ")
        txnChoice = input (" ---- BALANCES MODEL (Account(0) or UTXO(1)) ===> ")
        protocolChoice = input (" ---- PROTOCOL MODEL (JSON(0) or Byte Encoding(1)) ===> ")
        # chainInstance = chain.Chain()
        if minerChoice == "0":
            print("miner pow")
            if txnChoice == "0": #ADD PROTOCOL WHERE 
                if protocolChoice == "0":
                    #CREATE INSTANCES
                    # PROTOCOL
                    # print("whatbef")
                    walletInstance = wallet.Wallet()
                    minerInstance = miner.Miner(walletInstance, chainInstance, txnChoice)
                    # activateInteraction(minerInstance,walletInstance)
                    # print("what")
                    # time.sleep(10)
                    # print("Aftre10")
                    # sign = walletInstance.getPrivateKey().sign(walletInstance.getPublicKey().encode('utf-8'))
                    # minerInstance.addTxn(walletInstance.getPublicKey(), "640c8d9619bb9f46bf9e29010dddcaddbadd05f201a6a2f5f9de3e4ed7f1cde320f21b097b6b650e08cacdc14fde630ad0869155a46c3af04014fc96e93e3fb1", sign)
                else:
                    #CREATE INSTANCES
                    walletInstance = wallet.Wallet() #CHANGE WALLET FOR UTXO?
                    minerInstance = miner.Miner(walletInstance, chainInstance, txnChoice)
            else:
                if protocolChoice == "0":
                    #CREATE INSTANCES#CHANGE WALLET FOR UTXO?
                    walletInstance = wallet.Wallet() #CHANGE WALLET FOR UTXO?
                    minerInstance = miner.Miner(walletInstance, chainInstance, txnChoice)
                    # time.sleep(10)
                    # print("Aftre10")
                    # sign = walletInstance.getPrivateKey().sign(walletInstance.getPublicKey().encode('utf-8'))
                    # minerInstance.addTxn(walletInstance.getPublicKey(), "640c8d9619bb9f46bf9e29010dddcaddbadd05f201a6a2f5f9de3e4ed7f1cde320f21b097b6b650e08cacdc14fde630ad0869155a46c3af04014fc96e93e3fb1", sign)
                
                else:
                    #CREATE INSTANCES
                    walletInstance = wallet.Wallet() #CHANGE WALLET FOR UTXO?
                    minerInstance = miner.Miner(walletInstance, chainInstance, txnChoice)
        else:
            print("miner pot")
            if txnChoice == 0: #ADD PROTOCOL WHERE 
                if protocolChoice == "0":
                    #CREATE INSTANCES
                    walletInstance = wallet.Wallet() #CHANGE WALLET FOR UTXO?
                    minerInstance = miner_PoT.MinerPoT(walletInstance, chainInstance, txnChoice)
                else:
                    #CREATE INSTANCES
                    walletInstance = wallet.Wallet() #CHANGE WALLET FOR UTXO?
                    minerInstance = miner_PoT.MinerPoT(walletInstance, chainInstance, txnChoice)
            else:
                if protocolChoice == "0":
                    #CREATE INSTANCES
                    walletInstance = wallet.Wallet() #CHANGE WALLET FOR UTXO?
                    minerInstance = miner_PoT.MinerPoT(walletInstance, chainInstance, txnChoice)
                else:
                    #CREATE INSTANCES
                    walletInstance = wallet.Wallet() #CHANGE WALLET FOR UTXO?
                    minerInstance = miner_PoT.MinerPoT(walletInstance, chainInstance, txnChoice)
    elif choice == "X" or choice == "x":
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ END ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        break


        
    # minerInstance = miner.Miner(walletInstance, chainInstance, 0)
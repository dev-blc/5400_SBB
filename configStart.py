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
# initInstance = init.util()
minerChoice = None
while True:
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
        chainInstance = chain.Chain()
        if minerChoice == 0:
            if txnChoice == 0: #ADD PROTOCOL WHERE 
                if protocolChoice == 0:
                    #CREATE INSTANCES
                    # PROTOCOL
                    walletInstance = wallet.Wallet()
                    minerInstance = miner.Miner(walletInstance, chainInstance, txnChoice)
                else:
                    #CREATE INSTANCES
                    walletInstance = wallet.Wallet() #CHANGE WALLET FOR UTXO?
                    minerInstance = miner.Miner(walletInstance, chainInstance, txnChoice)
            else:
                if protocolChoice == 0:
                    #CREATE INSTANCES#CHANGE WALLET FOR UTXO?
                    walletInstance = wallet.Wallet() #CHANGE WALLET FOR UTXO?
                    minerInstance = miner.Miner(walletInstance, chainInstance, txnChoice)
                else:
                    #CREATE INSTANCES
                    walletInstance = wallet.Wallet() #CHANGE WALLET FOR UTXO?
                    minerInstance = miner.Miner(walletInstance, chainInstance, txnChoice)
        else:
            if txnChoice == 0: #ADD PROTOCOL WHERE 
                if protocolChoice == 0:
                    #CREATE INSTANCES
                    walletInstance = wallet.Wallet() #CHANGE WALLET FOR UTXO?
                    minerInstance = miner_PoT.MinerPoT(walletInstance, chainInstance, txnChoice)
                else:
                    #CREATE INSTANCES
                    walletInstance = wallet.Wallet() #CHANGE WALLET FOR UTXO?
                    minerInstance = miner_PoT.MinerPoT(walletInstance, chainInstance, txnChoice)
            else:
                if protocolChoice == 0:
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

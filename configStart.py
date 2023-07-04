import json
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
import peers
import state
import protocol
import protocolComms
# initInstance = init.util()
walletInstance = None
minerInstance = None
chainInstance = chain.Chain()
peerInstance = None
stateInstance = state.State()
commsInstance = None
# protocolInstance = None
walletInstance = wallet.Wallet()
protocolInstance = protocol.Protocol(chainInstance, stateInstance, walletInstance)
portNo = None
minerChoice = None
cpu_percent = []
def printCPU():
        cpu_percent.append(psutil.cpu_percent())
        cpuAvg = sum(cpu_percent)/len(cpu_percent)
        return cpuAvg
        # print(f"CPU Usage: {cpuAvg}%")
def getPeerInstance():
    return peerInstance
def getMinerInstance():
    return minerInstance
def getStateInstance():
    return stateInstance
def getInstances():
    return walletInstance, minerInstance, chainInstance, peerInstance, stateInstance, protocolInstance, commsInstance
def localMenu():
    
    while True:
        print("MENU")
        print("1. Check Balance")
        print("2. TXN Trial")
        print("3. TXN Custom")
        print("4. AVG BlockTime")
        # print("5. Send Message")
        print("0. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            print(">>>>>>>>>>>>>>>>>> LIST OF BALANCES")
            print(minerInstance.dbInstance.balances)
        elif choice == "2":
            sign = walletInstance.getPrivateKey().sign(walletInstance.getPublicKey().encode('utf-8'))
            signHex = sign.hex()
            # print(type(signHex),signHex)
            minerInstance.addTxn(walletInstance.getPublicKey(), "640c8d9619bb9f46bf9e29010dddcaddbadd05f201a6a2f5f9de3e4ed7f1cde320f21b097b6b650e08cacdc14fde630ad0869155a46c3af04014fc96e93e3fb1", signHex)
        elif choice == "3": 
            to = input("Enter to address: ") 
            sign = walletInstance.getPrivateKey().sign(walletInstance.getPublicKey().encode('utf-8'))
            # print(type(sign))
            signHex = sign.hex()
            minerInstance.addTxn(walletInstance.getPublicKey(), to, signHex)
        # elif choice == "4":
        #     wI, cI, mI = initInstance.fetchInstances()  
        #     to = input("Enter to address: ") 
        #     sign = wI.getPrivateKey().sign(wI.getPublicKey().encode('utf-8'))
        #     mI.addTxn(wI.getPublicKey(), to, sign)
        #     mI.addTxn(wI.getPublicKey(), to, sign)
        #     mI.addTxn(wI.getPublicKey(), to, sign)
        #     mI.addTxn(wI.getPublicKey(), to, sign)
        #     mI.addTxn(wI.getPublicKey(), to, sign)
        #     mI.addTxn(wI.getPublicKey(), to, sign)
        elif choice == "4":
            # wI, cI, mI = initInstance.fetchInstances()
            bno = chainInstance.getLastBlock().get("block_no") + 1
            blockTime = minerInstance.getBlockTime()
            bTAvg = sum(blockTime)/bno
            print(">>>>>>>>>>>>>>>>AVG BLOCK TIME => ",bTAvg)
        elif choice == "5":
            # msg = input("Enter your message")
            obj = chainInstance.getLastBlock()
            # pI = protocol.Protocol()
            msg = protocolInstance.createProtocolPayload("a",obj)
            # jsonMsg = json.dumps(msg)
            peerInstance.broadcastMessage(msg)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

start = time.time()
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print(":::::::::::::::::::::::::::::::::::::: SBB BLOCKCHAIN ::::::::::::::::::::::::::::::::::::::")
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    
portNo = int(input("######## ENTER HOST PORT NUMBER (5000 - 5004) "))
peerInstance = peers.Peers(portNo, protocolInstance)
start = 0
now = 0 

while True:
    printCPU()
    
    print("===> ENTER 0 TO START THE CHAIN IN DEFAULT CONFIGURATION")
    print("===> ENTER 1 TO START WITH CUSTOM CONFIGURATION")
    print("===> ENTER M TO MONITOR DETAILS")
    print("===> ENTER X TO STOP AND EXIT")
    choice = input("YOUR CHOICE ==> ")

    if choice == "0":
        # walletInstance = wallet.Wallet()
        stateInstance.setCurrentState("1")
        minerInstance = miner.Miner(walletInstance, chainInstance, stateInstance, protocolInstance, peerInstance, "0")
        handler = threading.Thread(target=peerInstance.receiver)
        handler.start()
        commsInstance = protocolComms.protocolComms(stateInstance, protocolInstance, peerInstance)
        handler2 = threading.Thread(target=commsInstance.executeStateHandlers)
        handler2.start()
        localMenu()
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
                    # walletInstance = wallet.Wallet()
                    stateInstance.setCurrentState("1")
                    minerInstance = miner.Miner(walletInstance, chainInstance, stateInstance, protocolInstance, peerInstance, txnChoice)
                    handler = threading.Thread(target=peerInstance.receiver)
                    handler.start()
                    commsInstance = protocolComms.protocolComms(stateInstance, protocolInstance, peerInstance)
                    handler2 = threading.Thread(target=commsInstance.executeStateHandlers)
                    handler2.start()
                    localMenu()
                    # activateInteraction(minerInstance,walletInstance)
                    # print("what")
                    # time.sleep(10)
                    # print("Aftre10")
                    # sign = walletInstance.getPrivateKey().sign(walletInstance.getPublicKey().encode('utf-8'))
                    # minerInstance.addTxn(walletInstance.getPublicKey(), "640c8d9619bb9f46bf9e29010dddcaddbadd05f201a6a2f5f9de3e4ed7f1cde320f21b097b6b650e08cacdc14fde630ad0869155a46c3af04014fc96e93e3fb1", sign)
                else:
                    #CREATE INSTANCES
                    # walletInstance = wallet.Wallet() #CHANGE WALLET FOR UTXO?
                    stateInstance.setCurrentState("1")
                    minerInstance = miner.Miner(walletInstance, chainInstance, stateInstance, protocolInstance, peerInstance, txnChoice)
                    handler = threading.Thread(target=peerInstance.receiver)
                    handler.start()
                    commsInstance = protocolComms.protocolComms(stateInstance, protocolInstance, peerInstance)
                    handler2 = threading.Thread(target=commsInstance.executeStateHandlers)
                    handler2.start()
                    localMenu()                     

            else:
                if protocolChoice == "0":
                    #CREATE INSTANCES#CHANGE WALLET FOR UTXO?
                    stateInstance.setCurrentState("1")
                    # walletInstance = wallet.Wallet() #CHANGE WALLET FOR UTXO?
                    minerInstance = miner.Miner(walletInstance, chainInstance, stateInstance, protocolInstance, peerInstance, txnChoice)
                    handler = threading.Thread(target=peerInstance.receiver)
                    handler.start()
                    commsInstance = protocolComms.protocolComms(stateInstance, protocolInstance, peerInstance)
                    handler2 = threading.Thread(target=commsInstance.executeStateHandlers)
                    handler2.start()
                    localMenu()
                    # time.sleep(10)
                    # print("Aftre10")
                    # sign = walletInstance.getPrivateKey().sign(walletInstance.getPublicKey().encode('utf-8'))
                    # minerInstance.addTxn(walletInstance.getPublicKey(), "640c8d9619bb9f46bf9e29010dddcaddbadd05f201a6a2f5f9de3e4ed7f1cde320f21b097b6b650e08cacdc14fde630ad0869155a46c3af04014fc96e93e3fb1", sign)
                
                else:
                    #CREATE INSTANCES
                    # walletInstance = wallet.Wallet() #CHANGE WALLET FOR UTXO?
                    stateInstance.setCurrentState("1")
                    minerInstance = miner.Miner(walletInstance, chainInstance, stateInstance, protocolInstance, peerInstance, txnChoice)
                    handler = threading.Thread(target=peerInstance.receiver)
                    handler.start()
                    commsInstance = protocolComms.protocolComms(stateInstance, protocolInstance, peerInstance)
                    handler2 = threading.Thread(target=commsInstance.executeStateHandlers)
                    handler2.start()
                    localMenu()
        else:
            print("miner pot")
            if txnChoice == 0: #ADD PROTOCOL WHERE 
                if protocolChoice == "0":
                    #CREATE INSTANCES
                    # walletInstance = wallet.Wallet() #CHANGE WALLET FOR UTXO?
                    stateInstance.setCurrentState("1")
                    minerInstance = miner_PoT.MinerPoT(walletInstance, chainInstance,protocolInstance, peerInstance ,txnChoice)
                    handler = threading.Thread(target=peerInstance.receiver)
                    handler.start()
                    peerInstance.broadcastMessage(minerInstance.initProtocol())
                    commsInstance = protocolComms.protocolComms(stateInstance, protocolInstance, peerInstance)
                    handler2 = threading.Thread(target=commsInstance.executeStateHandlers)
                    handler2.start()
                    localMenu()
                else:
                    #CREATE INSTANCES
                    # walletInstance = wallet.Wallet() #CHANGE WALLET FOR UTXO?
                    stateInstance.setCurrentState("1")
                    minerInstance = miner_PoT.MinerPoT(walletInstance, chainInstance,protocolInstance, peerInstance ,txnChoice)
                    handler = threading.Thread(target=peerInstance.receiver)
                    handler.start()
                    peerInstance.broadcastMessage(minerInstance.initProtocol())
                    commsInstance = protocolComms.protocolComms(stateInstance, protocolInstance, peerInstance)
                    handler2 = threading.Thread(target=commsInstance.executeStateHandlers)
                    handler2.start()
                    localMenu()
            else:
                if protocolChoice == "0":
                    #CREATE INSTANCES
                    # walletInstance = wallet.Wallet() #CHANGE WALLET FOR UTXO?
                    stateInstance.setCurrentState("1")
                    minerInstance = miner_PoT.MinerPoT(walletInstance, chainInstance,protocolInstance, peerInstance ,txnChoice)
                    handler = threading.Thread(target=peerInstance.receiver)
                    handler.start()
                    peerInstance.broadcastMessage(minerInstance.initProtocol())
                    commsInstance = protocolComms.protocolComms(stateInstance, protocolInstance, peerInstance)
                    handler2 = threading.Thread(target=commsInstance.executeStateHandlers)
                    handler2.start()
                    localMenu()
                else:
                    #CREATE INSTANCES
                    # walletInstance = wallet.Wallet() #CHANGE WALLET FOR UTXO?
                    stateInstance.setCurrentState("1")
                    minerInstance = miner_PoT.MinerPoT(walletInstance, chainInstance,protocolInstance, peerInstance ,txnChoice)
                    handler = threading.Thread(target=peerInstance.receiver)
                    handler.start()
                    peerInstance.broadcastMessage(minerInstance.initProtocol())
                    commsInstance = protocolComms.protocolComms(stateInstance, protocolInstance, peerInstance)
                    handler2 = threading.Thread(target=commsInstance.executeStateHandlers)
                    handler2.start()
                    localMenu()
    elif choice == "M" or choice == "m":
        print("------------------------------- MONITORING -------------------------------")
        print("----> Average CPU Usage", printCPU())
        now = time.time()
        print("----> Time Elapsed", now - start)
    elif choice == "X" or choice == "x":
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ END ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        break


        
    # minerInstance = miner.Miner(walletInstance, chainInstance, 0)
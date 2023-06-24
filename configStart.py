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
    # else: 
        
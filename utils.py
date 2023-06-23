import init
import wallet

walletHere = wallet.Wallet()
toPK = walletHere.getPublicKey()
print(toPK)
initInstance = init.util()
while True:
    print("MENU")
    print("1. Initialize Miner")
    print("2. Perform Other Action")
    print("3. TXN")
    print("0. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        initInstance.startNode()
    elif choice == "2":
        initInstance.utilsCall()
    elif choice == "3":
        wI, cI, mI = initInstance.fetchInstances()  
        to = input("Enter to address: ") 
        sign = wI.getPrivateKey().sign(wI.getPublicKey().encode('utf-8'))
        mI.addTxn(wI.getPublicKey(), to, sign)
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please try again.")
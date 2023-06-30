def validateBlock(block):
    txns = block.get("Transactions")
    isSignValid = False
    for txn in txns:
        pk = txn.get("From")
        sign = txn.get("Sign")
        if sign != None:
            isSignValid = pk.verify(sign, pk)
            if not isSignValid:
                print("!!!!!!!!!!!!!! INVALID TXN IN THE BLOCK !!!!!!!!!!!!!!")
    return isSignValid
    
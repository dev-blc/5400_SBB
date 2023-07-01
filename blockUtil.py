def validateBlock(block):
    txns = block.get("Transactions")
    isSignValid = False
    for txn in txns:
        pk = txn.get('From')
        sign = txn.get('Sign')
        print(txn)
        print(pk,sign)
        if sign != None:
            isSignValid = pk.verify(sign, pk)
            if not isSignValid:
                print("!!!!!!!!!!!!!! INVALID TXN IN THE BLOCK !!!!!!!!!!!!!!")
        else:
            isSignValid = True
    return isSignValid

# block = {'block_no': 0, 'nonce': 550963, 'prevHash': 0, 'Transactions': [{}, {'TXN_Hash': 'e53131506810789d8fd5eae54bcae6394ea7f3f77f8ca0908393d18c66492705', 'From': '0', 'To': 'd727bf06aad2b7b98a6ce4bc7622475b0c668abd362593b341efcbdb6f7965917e2d9eea1c84c7c3029bc2a205a7013054823e032817eebd1ad840f7ad04d9ff', 'Sign': None}], 'blockHash': '00000285d577801649a737feed6c3d403e68638b7780af25601159b1ba589183'}
# print(validateBlock(block))
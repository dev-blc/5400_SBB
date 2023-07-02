class AccountModel:
    def __init__(self, chainI):
        self.balances = {}
        self.chainInstance = chainI

    def transferBalance(self, sender, to):
        toBalance = self.balances.get(str(to))
        if toBalance is None:
            toBalance = self.fetchBalance(to) + 1
            self.balances.update({str(to): int(toBalance)})
        else :
            toBalance +=1 
            self.balances.update({str(to): int(toBalance)})
        
        senderBalance = self.balances.get(str(sender))
        if senderBalance is None:
            senderBalance = self.fetchBalance(to) - 1
            self.balances.update({str(sender): int(senderBalance)})
        else :
            senderBalance -=1 
            self.balances.update({str(sender): int(senderBalance)})

    def minerRewardUpdate(self, minerAddress):
        toBalance = self.balances.get(str(minerAddress))
        if toBalance is None:
            toBalance = self.fetchBalance(minerAddress)
            self.balances.update({str(minerAddress): int(toBalance)})
        else :
            toBalance +=1 
            self.balances.update({str(minerAddress): int(toBalance)})

    # def checkBalanceOfAddress(self, address):
    def fetchBalance(self,address):
        chain = self.chainInstance.getChain()
        #parse chain
        temp = 0
        for block in chain:
            # print("////In Block", block.get("block_no") )
            txns = block.get("Transactions")
            # txn = txns[-1]
            for txn in txns:
                if txn.get("To") == str(address):
                    # print("////Found To")
                    temp += 1
                elif txn.get("From") == str(address):
                    # print("////Found From")
                    temp -= 1
        # print("****************BALANCE****************")
        # print("=============>",temp)
        # self.balance = temp
        return temp  

    def getBalance(self, address):
        return int(self.balances.get(str(address))) 
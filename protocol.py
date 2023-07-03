import json
import blockUtil
import state
# import configStartUtils
states = state.allStates
emptyObj = json.dumps({})
class Protocol:
    def __init__(self, cI, sI, wI) -> None:
        self.temp = None
        self.chainInstance = cI
        self.stateInstance = sI
        self.walletInstance = wI
        self.pk = []
        self.pk.append(self.walletInstance.getPublicKey())
    def processIncomingMessage(self, jsonMsg):
        message = json.loads(jsonMsg)
        if message[0] == '\x02' and message[-1] == ('\x03'):
            stx = message[0]
            msg_len = message[1]
            opid = message[2]
            # print("//",message[1:3])
            # print(">>>",message[14:-2])
            obj = json.loads(message[3])
            # self.executeStates()
            # return self.opid,self.obj
            # Print the extracted components
            # print("STX:", stx)
            # print("Message Length:", msg_len)
            # print("Operation ID:", opid)
            # print("111111111Payload Object:", obj)
            # print("ETX:", message[-1])
            if opid == "a": # GET_COUNT
                # print("====GET_COUNT====")
                if self.stateInstance.getCurrentState() == states.MINING:
                    blockCount = self.chainInstance.getBlockCount()
                    payloadObj = {"blocks": blockCount}
                    msg = self.createProtocolPayload("c", json.dumps(payloadObj)) 
                    # print("=======",msg)
                    return msg 
                else: 
                    # msg = self.createProtocolPayload("a", None)
                    return "0"
                
            elif opid == "c":
                if self.stateInstance.getCurrentState() == states.MINING:
                    obj = json.loads(obj)
                    peerBlockCount = int(obj.get("blocks"))
                    localBlockCount = int(self.chainInstance.getBlockCount())
                    # print("||||||",localBlockCount,peerBlockCount)
                    if peerBlockCount > localBlockCount:
                        
                        self.stateInstance.setCurrentState("2") # Check state instance impl
                        # print("========= REQUEST NEW BLOCK HASHES")
                        msg = self.createProtocolPayload("b", json.dumps(emptyObj))# Here or in stateActions()?
                        print(msg)
                        return msg 
                    elif peerBlockCount == localBlockCount:
                        self.stateInstance.setCurrentState("1")
                        msg = self.createProtocolPayload("a", None)
                        return msg
                    else :
                        block = self.chainInstance.getLastBlock()
                        
                        payloadObj = {"block": block}
                        msg = self.createProtocolPayload("z",  json.dumps(payloadObj))
                        self.stateInstance.setCurrentState("1")
                        return msg 
                        # msg = self.createProtocolPayload("a", None)
                else:
                    
                    # msg = self.createProtocolPayload("a", None)
                    # self.stateInstance.setCurrentState("1")
                    return "0"
            elif opid == "b":
                state = self.stateInstance.getCurrentState()
                if state == states.GBH:
                    self.stateInstance.setCurrentState("3")
                    blockHashes = self.chainInstance.getBlockHashes()
                    payloadObj = {"blockHashes": blockHashes}
                    msg = self.createProtocolPayload("h",  json.dumps(payloadObj))  #BLOCK_HASHES
                    return msg 
                else :
                    # self.stateInstance.setCurrentState("1")
                    # msg = self.createProtocolPayload("a", None)
                    return "0"
                
            elif opid == "h":
                obj = json.loads(obj)
                blockHashes = obj.get('blockHashes')
                localBlockHashes = self.chainInstance.getBlockHashes()
                min_length = min(len(blockHashes), len(localBlockHashes))
                toBeFetched = []
                for i in range(min_length):
                    if blockHashes[i] != localBlockHashes[i]:
                        toBeFetched.append(i)
                    
                if len(blockHashes) != len(localBlockHashes):
                        toBeFetched.extend(range(min_length, max(len(blockHashes), len(localBlockHashes))))
                # index =0 
                for index in toBeFetched:
                    hash = blockHashes[index]
                    payloadObj = {"hash": hash}
                msg = self.createProtocolPayload("r",  json.dumps(payloadObj))  #BLOCK_HASHES
                return msg 
            elif opid == "r":
                obj = json.loads(obj)
                block = self.chainInstance.getBlock(obj.get("hash"))
                payloadObj = {"block": block}
                msg = self.createProtocolPayload("x",  json.dumps(payloadObj))
                return msg 
            elif opid == "x":
                #Validate block , make state change, add to chain 
                # Verify is all txns is signed by right person 
                if obj.get("block").get("blockHash") not in self.chainInstance.getBlockHashes():
                    isValid = blockUtil.validateBlock(obj.get("block"))
                    #Replace with exceptions 
                    print("-----------VALIDITY OF PEER NODE BLOCK ",isValid)
                    if isValid:
                        blockObj = obj.get("block")
                        if self.chainInstance.getBlockCount() == 0:
                            blockObj["prevHash"] = "0"
                        else:
                            prevHash = self.chainInstance.getLastBlock().get("blockHash")
                            blockObj["prevHash"] = prevHash

                        self.chainInstance.addBlock(blockObj) 
                        print("******************************************")
                        print("MINED// A NEW BLOCK ====> ", obj.get("block").get("blockHash"))
                        print("BLOCK CONTENTS ====>",obj.get("block"))
                        print("******************************************")
                        msg = self.createProtocolPayload("a", None)
                        return msg
                else :
                    self.stateInstance.setCurrentState("1")
                    # msg = self.createProtocolPayload("a", None)
                    return "0"
                
            elif opid == "g":
                # SEND PK
               
                myPK = self.walletInstance.getPublicKey()
                # print("inG===>",myPK)
                payloadObj = {"PK":myPK}
                msg = self.createProtocolPayload("p",  json.dumps(payloadObj))
                return msg 
            elif opid == "p":
                print("inP")

                obj = json.loads(obj)
                self.pk.append(obj.get("PK"))
                # print("inG===>",obj.get("PK"))
                # msg = self.createProtocolPayload("a", None)
                return "0"

                # None
            elif opid == "z":
                obj = json.loads(obj)
                block = obj
                #Validate block , make state change, add to chain 
                # Verify is all txns is signed by right person 
                if obj.get("block").get("blockHash") not in self.chainInstance.getBlockHashes():
                    isValid = blockUtil.validateBlock(obj.get("block"))
                    print("-----------VALIDITY OF PEER NODE BLOCK ",isValid)
                    blockObj = obj.get("block")
                    if self.chainInstance.getBlockCount() == 0:
                        blockObj["prevHash"] = "0"
                    else:
                        prevHash = self.chainInstance.getLastBlock().get("blockHash")
                        blockObj["prevHash"] = prevHash

                    self.chainInstance.addBlock(blockObj) 
                    print("******************************************")
                    print("MINED/// A NEW BLOCK ====> ", obj.get("block").get("blockHash"))
                    print("BLOCK CONTENTS ====>",obj.get("block"))
                    print("******************************************")
                    self.stateInstance.setCurrentState("1")
                    msg = self.createProtocolPayload("a", None)
                    return msg
                else :
                    self.stateInstance.setCurrentState("1")
                    msg = self.createProtocolPayload("a", None)
                    return msg
    #CHNAGE _ ADD PREV BLOCK HASH TP CURRENT OBJ 
                              
        else: 
            print("Invalid message format.")

    # def executeStates(self):
    #     while True:
    #         state = self.stateInstance.getCurrentState()
    #         if state == states.MINING:
    #             # print("+++++++InsideMining")
    #             msg = self.protocolInstance.createProtocolPayload("a", None)
    #             self.peerInstance.broadcastMessage(msg)
    #         elif state == states.GBH:
    #             # print("+++++++InsideGBH")
    #             msg = self.protocolInstance.createProtocolPayload("h", None)
    #             self.peerInstance.broadcastMessage(msg)
    #         # time.sleep(20)
    def getPeersPK(self):
        return self.pk

    def createProtocolPayload(self, opId, payloadObject):
        # Define the message components
        stx = '\x02'  # Start of Text (STX)
        opid = opId   # Operation Identifier
        obj = payloadObject  # Payload Object
        etx = '\x03'  # End of Text (ETX)

        # Construct the message
        payload = json.dumps(obj)  # Convert the payload object to JSON string
        opid_obj_len = len(opid) + len(payload)  # Calculate the length of OPID + OBJ
        msg_len = opid_obj_len.to_bytes(2, byteorder='big')  # Convert length to 2 bytes

        # Concatenate all components to form the message
        # message = str(stx) + str(msg_len) + str(opid.encode()) + str(payload.encode()) + str(etx)
        message = []
        message.append(stx)
        message.append(str(msg_len))
        message.append(str(opid))
        message.append(payload)
        message.append(etx)
        # Display the message
        # print(message)
        # print("STX:", stx)
        # print("Message Length:", msg_len)
        # print("Operation ID:", opid)
        # print("Payload Object:", payload)
        # print("ETX:", message[-1])
        # print("ETX:", etx)
        return json.dumps(message)

    # def getMessages(self):
    #     return self.opid, self.obj

# objp = {"Key":"val","key2":"val2","Key3":"val","key4":"val2"}
# pI = Protocol()
# msg = pI.createProtocolPayload("a", objp)
# pI.processIncomingMessage(msg)
# # # '\x00\x0f''z''{"Key": "val"}'
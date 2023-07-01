import json
import blockUtil
import state
# import configStartUtils
states = state.allStates
emptyObj = json.dumps({})
class Protocol:
    def __init__(self, cI, sI) -> None:
        self.temp = None
        self.chainInstance = cI
        self.stateInstance = sI
    def processIncomingMessage(self, jsonMsg):
        message = json.loads(jsonMsg)
        if message[0] == '\x02' and message[-1] == ('\x03'):
            stx = message[0]
            msg_len = message[1]
            opid = message[2]
            # print("//",message[1:3])
            # print(">>>",message[14:-2])
            obj = json.loads(message[3])
            
            # Print the extracted components
            # print("STX:", stx)
            # print("Message Length:", msg_len)
            # print("Operation ID:", opid)
            print("111111111Payload Object:", obj)
            # print("ETX:", message[-1])
            if opid == "a": # GET_COUNT
                print("====GET_COUNT====")
                blockCount = self.chainInstance.getBlockCount()
                payloadObj = {"blocks": blockCount}
                msg = self.createProtocolPayload("c", json.dumps(payloadObj)) 
                print("=======",msg)
                return msg 
            elif opid == "c":
                obj = json.loads(obj)
                peerBlockCount = int(obj.get("blocks"))
                localBlockCount = int(self.chainInstance.getBlockCount())
                print("||||||",localBlockCount,peerBlockCount)
                if peerBlockCount > localBlockCount:
                    
                    self.stateInstance.setCurrentState("2") # Check state instance impl
                    print("========= REQUEST NEW BLOCK HASHES")
                    msg = self.createProtocolPayload("b", emptyObj)# Here or in stateActions()?
                    print(msg)
                    return msg 
                elif peerBlockCount == localBlockCount:
                    self.stateInstance.setCurrentState("1")
                    msg = self.createProtocolPayload("a", None)
                    return msg
                else :
                    block = self.chainInstance.getLastBlock()
                    self.stateInstance.setCurrentState("1")
                    payloadObj = {"block": block}
                    msg = self.createProtocolPayload("z",  payloadObj)
                    return msg 
                    # msg = self.createProtocolPayload("a", None)
            elif opid == "b":
                state = self.stateInstance.getCurrentState()
                if state == states.GBH:
                    self.stateInstance.setCurrentState("3")
                blockHashes = self.chainInstance.getBlockHashes()
                payloadObj = {"blockHashes": blockHashes}
                msg = self.createProtocolPayload("h",  json.dumps(payloadObj))  #BLOCK_HASHES
                return msg 
                
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
                msg = self.createProtocolPayload("x",  payloadObj)
                return msg 
            elif opid == "x":
                #Validate block , make state change, add to chain 
                # Verify is all txns is signed by right person 
                isValid = blockUtil.validateBlock(obj.get("block"))
                #Replace with exceptions 
                print("-----------VALIDITY OF PEER NODE",isValid)
                if isValid:
                    self.chainInstance.addBlock(obj.get("block")) 
                    print("******************************************")
                    print("MINED A NEW BLOCK ====> ", obj.get("block").get("blockHash"))
                    print("BLOCK CONTENTS ====>",obj.get("block"))
                    print("******************************************")
                    msg = self.createProtocolPayload("a", None)
                    return msg


                # None
            elif opid == "z":
                block = obj
                #Validate block , make state change, add to chain 
                # Verify is all txns is signed by right person 
                isValid = blockUtil.validateBlock(obj.get("block"))
                print("-----------VALIDITY OF PEER NODE",isValid)
                self.chainInstance.addBlock(obj.get("block"))
                msg = self.createProtocolPayload("a", None)
                return msg

                              
        else: 
            print("Invalid message format.")

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

# objp = {"Key":"val","key2":"val2","Key3":"val","key4":"val2"}
# pI = Protocol()
# msg = pI.createProtocolPayload("a", objp)
# pI.processIncomingMessage(msg)
# # # '\x00\x0f''z''{"Key": "val"}'
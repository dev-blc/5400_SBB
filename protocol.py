import json

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
            # print("Payload Object:", obj)
            # print("ETX:", message[-1])
            if opid == "a": # GET_COUNT
                blockCount = self.chainInstance.getBlockCount()
                payloadObj = {"blocks", blockCount}
                self.createProtocolPayload("c", payloadObj) 
            if opid == "c":
                peerBlockCount = int(obj.get("blocks"))
                localBlockCount = int(self.chainInstance.getBlockCount())
                if peerBlockCount > localBlockCount:
                    self.stateInstance.setCurrentState("2")
                
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
        message.append(str(payload))
        message.append(etx)
        # Display the message
        print(message)
        print("STX:", stx)
        print("Message Length:", msg_len)
        print("Operation ID:", opid)
        print("Payload Object:", payload)
        print("ETX:", message[-1])
        print("ETX:", etx)
        return json.dumps(message)

# objp = {"Key":"val","key2":"val2","Key3":"val","key4":"val2"}
# pI = Protocol()
# msg = pI.createProtocolPayload('z', objp)
# pI.processIncomingMessage(msg)
# # # '\x00\x0f''z''{"Key": "val"}'
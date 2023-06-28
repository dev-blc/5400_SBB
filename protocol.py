import json

class Protocol:
    def __init__(self) -> None:
        self.temp 
    def processIncomingMessage(self, message):
        if message.startswith(chr(2)) and message.endswith(chr(3)):
            stx = message[0]
            msg_len = int.from_bytes(message[1:3], byteorder='big')
            opid = message[3]
            obj = json.loads(message[4:-1])

            # Print the extracted components
            print("STX:", stx)
            print("Message Length:", msg_len)
            print("Operation ID:", opid)
            print("Payload Object:", obj)
            print("ETX:", message[-1])
        else:
            print("Invalid message format.")

    def createProtocolPayload(self, opId, payloadObject):
        # Define the message components
        stx = chr(2)  # Start of Text (STX)
        opid = opId   # Operation Identifier
        obj = payloadObject  # Payload Object
        etx = chr(3)  # End of Text (ETX)

        # Construct the message
        payload = json.dumps(obj)  # Convert the payload object to JSON string
        opid_obj_len = len(opid.encode()) + len(payload.encode())  # Calculate the length of OPID + OBJ
        msg_len = opid_obj_len.to_bytes(2, byteorder='big')  # Convert length to 2 bytes

        # Concatenate all components to form the message
        message = stx + msg_len + opid.encode() + payload.encode() + etx
        # Display the message
        print(message)
        return message

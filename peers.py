import socket
import threading
import time
import sys

class Peers:
    def __init__(self, portNo):
        # self.walletInstance = wI
        # self.chainInstance = cI
        # self.minerInstance = mI 
        # self.dbInstance = dbI
        self.port = portNo
        self.peers = [('127.0.0.1', 5000),('127.0.0.1', 5001), ('127.0.0.1', 5002), ('127.0.0.1', 5003)]
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('127.0.0.1', self.port))
        self.sock.settimeout(1)
    def getPeers(self):
        return self.peers
    def addToPeer(self, IP, PORT):
        self.peers.append((IP, PORT))
    def broadcastMessage(self, message):
        # self.sock = socket.socket(socket.AF_INET ,socket.SOCK_DGRAM)
        for peer in self.peers:
            if(peer == ('127.0.0.1',self.port)):
                continue
            else:
                self.sock.sendto(message.encode(), peer)

    def receiver(self):
        # sock = socket.socket(socket.AF_INET ,socket.SOCK_DGRAM)
        self.sock.bind(('127.0.0.1',self.port))
        while True:
            data, address = self.sock.recvfrom(1024)
            print(f'Message [{data.decode()}] from [{address[0]}]:[{address[1]}]')
            if "exit" in data.decode():
                sys.exit()
        
import socket
import sys


# Networking Setting
host = "localhost"
port = 3000
address = (host, port)
upd_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
upd_socket.bind((address))





# Get Sent Data
def segment(data):
    data = data.decode("utf-8")
    received_syn = int(data.split()[0])
    received_seq = int(data.split()[1])
    received_ack = int(data.split()[2])
    return received_syn, received_seq, received_ack





# Receiver's handshake data
class handshake_data:
    def __init__(self, syn = 0, seq = 0, ack = 0):
        self.syn = syn
        self.seq = seq
        self.ack = ack
        self.string = str(self.syn) + " " +str(self.seq) + " " + str(self.ack)
        self.string_data = self.string.encode("utf-8")





# Hand Shake Start here
data, addr = upd_socket.recvfrom(1024)
received_syn, received_seq, received_ack = segment(data)

if received_syn == 1:
    upd_socket.sendto(handshake_data(syn=1, seq=0, ack=received_seq+1).string_data, ("localhost", 3001))

data, addr = upd_socket.recvfrom(1024)
# 把这些信息目前存着就好
received_syn, received_seq, received_ack = segment(data)
print(received_syn, received_seq, received_ack)
print("connected successful")




# Data Transfer Start Here
while True:
    data, addr = upd_socket.recvfrom(1024)
    print(data)










# Create A File For Accepting File
# path = sys.argv[1]
# file = open("data.txt", "w")
# file.close()





# CLOSE CONNECTION
upd_socket.close()





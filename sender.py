import socket
import sys

# Reading Target File
filePath = sys.argv[3]
filePath = "/Users/keiichi/Desktop/9331_project/content/9331txt1.txt"
print(filePath)



# # Reading File and add to content
content = ""
with open(filePath) as file:
    for line in file:
        content += line



# # Networking Setting
host = sys.argv[1]
port = int(sys.argv[2])
client_socket = socket.socket()
client_socket.connect((host, port))



# Receving Any FeedBack From Receiver
while content:
    client_socket.send(content.encode('utf-8'))
    # It can receive the file send from Receiver (In Byte Type)
    data = client_socket.recv(1024)
    break
client_socket.close()



import socket
import sys


# Networking Setting
host = ''
port = 2052
address = (host, port)



# Socket Programing Initialization
upd_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
upd_socket.bind((address))
upd_socket.listen(1)
conn, addr = upd_socket.accept()



# Prepare for receive data
content = ""



# Receive Data From Sender
while True:
    # The Content of Received Data
    data = conn.recv(1024)
    if not data:
        print("There is no data come")
        break
    else:
        # Transfer Bytes File To String
        content += data.decode('utf-8')
        # TRY: receiver send a data to sender
        conn.send(data)
        break



# Create a File For Content
# path = "/Users/keiichi/Desktop/9331_project/data.txt"
file = open("data.txt", "w")
file.write(content)
file.close()



# CLOSE CONNECTION
conn.close()





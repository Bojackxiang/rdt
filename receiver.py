import socket
import sys


# Networking Setting
host = 'localhost'
port = 3102
address = (host, port)





# Hand Shake Start here
# Receive Data From Sender
upd_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
upd_socket.bind((address))
# Trying To Receive Data Countinusous

while True:
    print("accepting data")
    data, addr = upd_socket.recvfrom(1024)
    # byte data to string data
    print(data.decode('utf-8'))
    if data.decode('utf-8') == "10":
        print("there is a 10")
        break
    upd_socket.sendto("back message".encode("UTF-8"), (address))
    print("sending data")
    data, addr = upd_socket.recvfrom(1024)
    print("it reach end")
    break

    # number = data.decode("UTF-8")





# receive data from sender, add 1 to it and send back the total sum

# receive 1024 byte at a time
# number = int(data.decoded("UTF-8")) + 1
# print("I just received a data" + data)
# data = str(number)
# print("now i want to send a data", data)
# upd_socket.send(data.encode('UTF-8'))




# Prepare for receive data
# content = ""



# Receive Data From Sender
# while True:
#     # The Content of Received Data
#     # data = conn.recv(1024)
#     if not data:
#         print("There is no data come")
#         break
#     else:
#         # Transfer Bytes File To String
#         content += data.decode('utf-8')
#         # TRY: receiver send a data to sender
#         conn.send(data)
#         break



# Create a File For Content
# path = "/Users/keiichi/Desktop/9331_project/data.txt"
# file = open("data.txt", "w")
# file.write(content)
# file.close()



# CLOSE CONNECTION
upd_socket.close()





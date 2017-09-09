import socket
import sys

# Reading Target File
# filePath = sys.argv[3]
# filePath = "/Users/keiichi/Desktop/9331_project/content/9331txt1.txt"
# print(filePath)



# # Reading File and add to content
# content = ""
# with open(filePath) as file:
#     for line in file:
#         content += line



# # Networking Setting (SUCCESS)
# host = sys.argv[1]
# port = int(sys.argv[2])
host = "localhost"
port = 3102
addr = (host, port)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# client_socket.bind(addr)
mss = 10
# log_file = open("log_file.txt")



# Three Way Handshake Start here
def three_way_handshake(host, port):
    # s : SYN -> R:
    # r : SYN, ACK -> s
    # s : ACK -> Receiver
    # Done
    syn_number = 200
    ack_number = 0
    fin_number = 0
    new_syn_number = 0
    new_ack_number = 0

    # send data to receiver
    print("sending data")
    client_socket.sendto(str(syn_number).encode("UTF-8"), (host, port))

    print("receiving data")
    data, addr = client_socket.recv(1024)
    print("the receving data is "+ data)

three_way_handshake(host, port)





# only send a number to receiver at the beginning (SUCCESS)
# data = 20
# client_socket.sendto(data.encode("UTF-8"), addr)
# print("I just send a data to receiver")





#Trying To Receive Data From Sender (TESTING)
# data, addr = client_socket.recvfrom(1024)
# print(data)




# Receving Any FeedBack From Receiver
# while content:
    # client_socket.send(content.encode('utf-8'))
    # # It can receive the file send from Receiver (In Byte Type)
    # data = client_socket.recv(1024)
    # break





client_socket.close()



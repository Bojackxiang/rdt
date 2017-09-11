import socket
import time


# Parameters
path = "/Users/keiichi/Desktop/9331_project/content/9331txt2.txt"
mss = 10
receiver_ip = "localhost"
receiver_port = 3000
receiver_address = (receiver_ip, receiver_port)
time_out = 100
# Create A Log File
log_text = open("Sender_log.txt", "w")


# # Networking Setting (SUCCESS)
host = "localhost"
port = 3001
addr = (host, port)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.bind(addr)
# log_file = open("log_file.txt")





def segment(data):  # Used For Transfer Accepted Data
    data = data.decode("utf-8")
    received_syn = int(data.split()[0])
    received_seq = int(data.split()[1])
    received_ack = int(data.split()[2])
    return received_syn, received_seq, received_ack





class handshake_data:   # Used for HandShake And Following Data Transfering And Header Data
    def __init__(self, syn = 0, seq = 0, ack = 0):
        self.syn = syn
        self.seq = seq
        self.ack = ack
        self.string = str(self.syn) +" "+ str(self.seq) + " " + str(self.ack)
        self.string_data = self.string.encode("utf-8")





# Three Way Handshake Start here
def three_way_handshake(host, port):
    # s : SYN -> R:
    # r : SYN, ACK -> s
    # s : ACK -> Receiver
    # Done
    sequence_number = 0
    send_data_pack1 = handshake_data(syn=1, seq=sequence_number)
    client_socket.sendto(send_data_pack1.string_data, ("localhost", 3000))
    log_text.writelines( "snd %2.3f" %((time.time()%10)))
    received_data_pack1, addr = client_socket.recvfrom (1024)
    received_syn, received_seq, received_ack = segment(received_data_pack1)
    if received_syn == 1 & received_ack == 1:
        client_socket.sendto(handshake_data(syn=1, seq=received_seq+1, ack = received_ack).string_data, ("localhost", 3000))
        print("connected successfully")
    else:
        print("Connection is not done")
    # Now Everything Is 1


# ========================= Now We Are Done With Three Way HandShake =========================

# We Build A Structure For Data Header
# After Three Way Hand Shake, seq = 1, ack = 1,
class trasnfering_data_header:
    def __init__(self, sequence_number=1, ack=1, fin=0, data=""):
        self.sequence_number = sequence_number
        self.ack = ack
        self.fin = fin
        self.data = data




# Main Programing Start
three_way_handshake(host, port)
# Now We Have Sequence = 1, ack number = 1
sequence_number = 1
ack_number = 1
data_list = []
file = open(path)
with open(path) as file:
    byte = file.read(mss)
    data_list.append(trasnfering_data_header(sequence_number=sequence_number, data=byte))
    sequence_number += len(byte)
    while byte:
        byte = file.read(mss)
        data_list.append(trasnfering_data_header(sequence_number=sequence_number, data=byte))
        sequence_number += len(byte)
file.close()


for item in data_list:
    print(item.sequence_number)





# Done With The File
client_socket.close()



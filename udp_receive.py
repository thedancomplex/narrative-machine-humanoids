import socket

UDP_IP = "0.0.0.0"
UDP_PORT = 8009

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data
    if((data[0]) == "M"):
	print("good")
	mot = int(data[1])
	print("motor: ",mot)
	if(data[2] == "A"):
	    val = float(data[3:len(data)].decode())
	    print("val: ",val)
	elif(data[2] == "V"):
	    vel = float(data[3:len(data)].decode())
	    print("vel: ",vel)
    if((data[0]) == "P"):
	print("net synch")

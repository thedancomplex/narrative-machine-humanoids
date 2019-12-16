import socket, sys
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while(True):
 raw_input()
 print("HI")
 s.sendto('G'*10,   ('192.168.8.204',8888))

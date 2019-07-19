import socket
import struct
import select

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("localhost",10000))
sock.settimeout(1.0)

server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ("localhost",10001)
server_sock.bind(server_address)
server_sock.listen(5)

try:
	datas = (str(server_address[0]) + "," + str(server_address[1]))	
	sock.sendall(datas)
	
except socket.error, msg:
	print msg
sock.close()

inputs = [server_sock]
outputs = []

while True:
	readable, writable, exceptional = select.select(inputs,outputs,inputs,1)
	for s in readable:
		if s is server_sock:
			connection,client_address = s.accept()
			inputs.append(connection)
		else: 
			raw_data,client_address = s.recvfrom(1024)
			if raw_data:
				print(str(raw_data))
				if str(raw_data) == "leecher_uzenet":
					s.sendall("Uzenet")
			else:
				inputs.remove(s) 
server_sock.close()			


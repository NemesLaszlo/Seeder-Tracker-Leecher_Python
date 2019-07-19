import select
import socket
import json
import datetime

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("localhost",10000))
sock.listen(5)

inputs = [sock]
outputs = []

cache = ""

while True:
	readable, writable, exceptional = select.select(inputs,outputs,inputs,1)
	for s in readable:
		if s is sock:
			connection,client_address = s.accept()
			inputs.append(connection)
		else: 
			raw_data,client_address = s.recvfrom(1024)
			if raw_data:
				data = raw_data.split(",")
				if str(data[0]) != "Lekerem":
					cache += str(data[0]) + "," + str(data[1])
					print(cache)
				else:
					s.sendall(cache)
					print("cache uritve, adat tovabbkuldve")
					cache = ""
			else:
				inputs.remove(s) 
sock.close()				
				


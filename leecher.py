import socket
import struct
import select

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("localhost",10000))
sock.settimeout(1.0)

try:
	datas = ("Lekerem")	
	sock.sendall(datas)
	solution = sock.recv(1024)
	informations = solution.split(",")
	print(informations[0] + "," + informations[1])
	
	other_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	other_sock.connect((str(informations[0]),int(informations[1])))
	other_sock.settimeout(1.0)
	datas2 = ("leecher_uzenet")	
	other_sock.sendall(datas2)
	solution = other_sock.recv(1024)
	print(str(solution))

except socket.error, msg:
	print msg
sock.close()
other_sock.close()


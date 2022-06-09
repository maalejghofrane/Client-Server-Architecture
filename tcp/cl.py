import time
import socket
# Créer une socket de streaming de la famille INET
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(),8000))
time.sleep(10)
s.send(bytes(socket.gethostname(),"utf-8"))
msg =s.recv(1024)
print(msg.decode("utf-8"))
s.close()
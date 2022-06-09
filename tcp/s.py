from os import close
import socket
# Créer une socket de streaming de la famille INET
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a public host, and a well-known port
serversocket.bind((socket.gethostname(), 8000))

# become a server socket

#serversocket en cours d'écoute 
serversocket.listen(5)

while (True):
    clientsocket, address= serversocket.accept()
    print(f'Connection from{address} has been established!')
    data = clientsocket.recv(1024)
    print(data.decode("utf-8"))
    clientsocket.send(bytes("OK!","utf-8"))
    if (len(clientsocket.recv(1))==0):
        clientsocket.close()
        print('connection closed!')
    

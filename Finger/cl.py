#----- A simple TCP client program in Python using send() function -----

import socket
import sys

 

# Create a client socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

 

# Connect to the server

clientSocket.connect(("127.0.0.1",7981));

 

# Send data to server

data = "sofien";

clientSocket.send(data.encode());

 

# Receive data from server

dataFromServer = clientSocket.recv(1024);

 

# Print to the console

print(dataFromServer.decode());
clientSocket.close()
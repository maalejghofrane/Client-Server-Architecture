#----- A simple TCP client program in Python using send() function -----
import socket
import sys
import argparse
# Construct the argument parser
ap = argparse.ArgumentParser()
# Add the arguments to the parser
ap.add_argument("-a", "--login", required=True,
   help="first operand")
ap.add_argument("-b", "--host", required=True,
   help="second operand")
args = vars(ap.parse_args())
# Create a client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
# Connect to the server
clientSocket.connect((args['host'],7980));
# Send data to server
data = args['login'];
clientSocket.send(data.encode());
# Receive data from server
dataFromServer = clientSocket.recv(1024);
# Print to the console
print(dataFromServer.decode());
clientSocket.close()
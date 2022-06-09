#----- A simple TCP based server program in Python using send() function -----
import socket
import subprocess
import os
# file descriptors r, w for reading and writing
r, w = os.pipe()
# Create a stream based socket(i.e, a TCP socket)
# operating on IPv4 addressing scheme
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
# Bind and listen
serverSocket.bind(("127.0.0.1",7980));
serverSocket.listen(4);
# Accept connections
while(True):
    try : 
        (clientConnected, clientAddress) = serverSocket.accept();
        print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]));
        dataFromClient = clientConnected.recv(1024)
        print(dataFromClient.decode())
        #Fichier 1 fingerd.log
        fichier = open("fingerd.log", "a")
        fichier.write(clientAddress[0])
        fichier.write("   ")
        fichier.write(dataFromClient.decode())
        fichier.write("\n")
        fichier.close()
        #Fichier 2 finger.pid
        f2 = open("finger.pid", "a")
        f2.write("  Le pid=")
        data = str(int(os.getpid()))
        f2.write(data)
        f2.write("\n")
        f2.close()
        subprocess.call(["finger",dataFromClient.decode(),'none'])
        p1 = subprocess.run(['finger',dataFromClient.decode()],capture_output=True,text=True)
        # Send some data back to the client
        if p1.stdout != '' :
            clientConnected.send(p1.stdout.encode());
        if p1.stdout == '' : 
            x = 'finger: '+dataFromClient.decode()+': no such user'
            clientConnected.send(x.encode());
        #print(p1.stdout)
        clientConnected.close()
    except:
        print("errrrrrrrrrrrrror")
        clientConnected.close()
        serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        break; 

    

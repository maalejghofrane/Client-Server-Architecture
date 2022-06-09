import socket
import sys
import time
import os
import subprocess 
import struct

print "\nWelcome to the FTP server.\n\nTo get started, connect a client."

TCP_IP = "127.0.0.1" 
TCP_PORT = 1465
BUFFER_SIZE = 1024 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()

print "\nConnected to by address: {}".format(addr)

def upld():
    # Send message once server is ready to recieve file details
    conn.send("1")
    # Recieve file name length, then file name
    file_name_size = struct.unpack("h", conn.recv(2))[0]
    file_name = conn.recv(file_name_size)
    # Send message to let client know server is ready for document content
    conn.send("1")
    # Recieve file size
    file_size = struct.unpack("i", conn.recv(4))[0]
    # Initialise and enter loop to recive file content
    start_time = time.time()
    output_file = open(file_name, "wb")
    # This keeps track of how many bytes we have recieved, so we know when to stop the loop
    bytes_recieved = 0
    print "\nRecieving..."
    while bytes_recieved < file_size:
        l = conn.recv(BUFFER_SIZE)
        output_file.write(l)
        bytes_recieved += BUFFER_SIZE
    output_file.close()
    print "\nRecieved file: {}".format(file_name)
    # Send upload performance details
    conn.send(struct.pack("f", time.time() - start_time))
    conn.send(struct.pack("i", file_size))
    return

def list_files():
    print "Listing files..."
    output = subprocess.check_output(['ls', '-l'])
    conn.send(output)
    conn.recv(BUFFER_SIZE)
    print "Successfully sent list of files"
    return



def dwld():
    conn.send("1")
    file_name_length = struct.unpack("h", conn.recv(2))[0]
    print file_name_length
    file_name = conn.recv(file_name_length)
    print file_name
    if os.path.isfile(file_name):
        # Then the file exists, and send file size
        conn.send(struct.pack("i", os.path.getsize(file_name)))
    else:
        # Then the file doesn't exist, and send error code
        print "File name not valid"
        conn.send(struct.pack("i", -1))
        return
    # Wait for ok to send file
    conn.recv(BUFFER_SIZE)
    # Enter loop to send file
    start_time = time.time()
    print "Sending file..."
    content = open(file_name, "rb")
    # Again, break into chunks defined by BUFFER_SIZE
    l = content.read(BUFFER_SIZE)
    while l:
        conn.send(l)
        l = content.read(BUFFER_SIZE)
    content.close()
    # Get client go-ahead, then send download details
    conn.recv(BUFFER_SIZE)
    conn.send(struct.pack("f", time.time() - start_time))
    return


def chdr():
    conn.send("1")
    # Recieve file name length, then file name
    path_name_size = struct.unpack("h", conn.recv(2))[0]
    path = conn.recv(path_name_size)
    # Send message to let client know server is ready for document content
    conn.send("1")
    # Recieve file size
    print "\nRecieved new path: {}".format(path)
    os.chdir(path)
    return



def quit():
    # Send quit conformation
    conn.send("1")
    # Close and restart the server
    conn.close()
    s.close()
    exit(0)

while True:
    # Enter into a while loop to recieve commands from client
    print "\n\nWaiting for instruction"
    data = conn.recv(BUFFER_SIZE)
    print "\nRecieved instruction: {}".format(data)
    # Check the command and respond correctly
    if data == "UPLD":
        upld()
    elif data == "LIST":
        list_files()
    elif data == "DWLD":
        dwld()
    elif data == "CHDR":
        chdr()
    elif data == "QUIT":
        quit()
    # Reset the data to loop
    data = None

import socket
import sys
import os
import struct

# Initialise socket stuff
TCP_IP = "127.0.0.1" 
TCP_PORT = 1465
BUFFER_SIZE = 1024 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def conn():
    print "Sending server request..."
    try:
        s.connect((TCP_IP, TCP_PORT))
        print "Connection sucessful"
    except:
        print "Connection unsucessful. Make sure the server is online."

def upld(file_name):
    
    print "\nUploading file: {}...".format(file_name)
    try:
        # Check the file exists
        content = open(file_name, "rb")
    except:
        print "Couldn't open file. Make sure the file name was entered correctly."
        return
    try:
        s.send("UPLD")
    except:
        print "Couldn't make server request. Make sure a connection has bene established."
        return
    try:
        s.recv(BUFFER_SIZE)
        s.send(struct.pack("h", sys.getsizeof(file_name)))
        s.send(file_name)
        s.recv(BUFFER_SIZE)
        s.send(struct.pack("i", os.path.getsize(file_name)))
    except:
        print "Error sending file details"
    try:
        l = content.read(BUFFER_SIZE)
        print "\nSending..."
        while l:
            s.send(l)
            l = content.read(BUFFER_SIZE)
        content.close()
        # Get upload performance details
        upload_time = struct.unpack("f", s.recv(4))[0]
        upload_size = struct.unpack("i", s.recv(4))[0]
        print "\nSent file: {}\nTime elapsed: {}s\nFile size: {}b".format(file_name, upload_time, upload_size)
    except:
        print "Error sending file"
        return
    return

def list_files():
    print "Requesting files...\n"
    try:
        s.send("LIST")
    except:
        print "Couldn't make server request. Make sure a connection has bene established."
        return
    try:
        buffer= s.recv(BUFFER_SIZE)
        print "\nList of files : {}".format(buffer)

    except:
        print "Couldn't retrieve listing"
        return
    try:
        # Final check
        s.send("1")
        return
    except:
        print "Couldn't get final server confirmation"
        return


def dwld(file_name):
    # Download given file
    print "Downloading file: {}".format(file_name)
    try:
        # Send server request
        s.send("DWLD")
    except:
        print "Couldn't make server request. Make sure a connection has bene established."
        return
    try:
        # Wait for server ok, then make sure file exists
        s.recv(BUFFER_SIZE)
        # Send file name length, then name
        s.send(struct.pack("h", sys.getsizeof(file_name)))
        s.send(file_name)
        # Get file size (if exists)
        file_size = struct.unpack("i", s.recv(4))[0]
        if file_size == -1:
            # If file size is -1, the file does not exist
            print "File does not exist. Make sure the name was entered correctly"
            return
    except:
        print "Error checking file"
    try:
        # Send ok to recieve file content
        s.send("1")
        # Enter loop to recieve file
        output_file = open(file_name, "wb")
        bytes_recieved = 0
        print "\nDownloading..."
        while bytes_recieved < file_size:
            # Again, file broken into chunks defined by the BUFFER_SIZE variable
            l = s.recv(BUFFER_SIZE)
            output_file.write(l)
            bytes_recieved += BUFFER_SIZE
        output_file.close()
        print "Successfully downloaded {}".format(file_name)
        # Tell the server that the client is ready to recieve the download performance details
        s.send("1")
        # Get performance details
        time_elapsed = struct.unpack("f", s.recv(4))[0]
        print "Time elapsed: {}s\nFile size: {}b".format(time_elapsed, file_size)
    except:
        print "Error downloading file"
        return
    return



def chdr(path):
    print "\nChanging directory: {}...".format(path)
    try:
        s.send("CHDR")
    except:
        print "Couldn't make server request. Make sure a connection has bene established."
        return
    try:
        s.recv(BUFFER_SIZE)
        s.send(struct.pack("h", sys.getsizeof(path)))
        s.send(path)
        s.recv(BUFFER_SIZE)
        print "Path changed succesfully"
    except:
        print "Error Changing path"
        return
    return




def quit():
    s.send("QUIT")
    # Wait for server go-ahead
    s.recv(BUFFER_SIZE)
    s.close()
    print "Server connection ended"
    return

print "\n\nWelcome to the FTP client.\n\nCall one of the following functions:\nCONN           : Connect to server\nUPLD file_path : Upload file\nLIST           : List files\nDWLD file_path : Download file\nCHDR new_path : Change path\nQUIT           : Exit"

while True:
    # Listen for a command
    prompt = raw_input("\nEnter a command: ")
    if prompt[:4].upper() == "CONN":
        conn()
    elif prompt[:4].upper() == "UPLD":
        upld(prompt[5:])
    elif prompt[:4].upper() == "LIST":
        list_files()
    elif prompt[:4].upper() == "DWLD":
        dwld(prompt[5:])
    elif prompt[:4].upper() == "CHDR":
        chdr(prompt[5:])
    elif prompt[:4].upper() == "QUIT":
        quit()
        break
    else:
        print "Command not recognised; please try again"

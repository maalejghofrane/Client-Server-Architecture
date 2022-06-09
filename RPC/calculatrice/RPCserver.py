from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
#Define any functions we want available

class Calcul(SimpleXMLRPCRequestHandler) :
    rpc_paths=('/RPC2')
server = SimpleXMLRPCServer(("localhost", 8000))

server.register_introspection_functions()   
@server.register_function
def add(x,y) : 
        return (x+y)
@server.register_function
def mult(x,y) :
        return (x*y)
@server.register_function
def diff(x,y) :
        return (y-x)
@server.register_function
def quotient(x,y) :
        return (x/y)
@server.register_function
def absolu(x):
        return abs(x)
    
# Define server and Create it

print ("listening on port 8000 ... ")
#register these functions with the server instance


#exécuter la boucle principale du serveur
server.serve_forever()












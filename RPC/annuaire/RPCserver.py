from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
#Define any functions we want available

class Calcul(SimpleXMLRPCRequestHandler) :
    rpc_paths=('/RPC2')
server = SimpleXMLRPCServer(("localhost", 8000))

server.register_introspection_functions()   
Dict ={}

@server.register_function

def ajouterEntree(nom, num):
        Dict[nom] = num
        return("ajout effectué avec succes")

@server.register_function
def trouverNumero(nom):
        for key in Dict:
            if key == nom:
                return (Dict[key])


@server.register_function  
def nbNumeros():
        return len(Dict)

@server.register_function
def getAll():
    return Dict

@server.register_function
def supprimerEntree( nom):
        Dict.pop(nom);
        return ("contact %s a éte supprimé" % nom)
@server.register_function
def supprimerTout():
    Dict.clear()
    return ("repertoire vide")

    
# Define server and Create it

print ("listening on port 8000 ... ")
#register these functions with the server instance


#exécuter la boucle principale du serveur
server.serve_forever()












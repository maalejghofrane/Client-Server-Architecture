from xmlrpc.client import ServerProxy
import sys
import xmlrpc.client
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

while True :
    try:
            print('Choix de l ’ action a effectuer : ')
            print('1: Ajouter une entree dans le repertoire')
            print('2: Afficher le numero de telephone d ’une personne')
            print('3: Afficher le nombre de numeros enregistres dans le repertoire')
            print('4: Afficher le contenu de tout le repertoire')
            print('5: Supprimer du repertoire une personne et son numero')
            print('6: Effacer tout le contenu du repertoire')
            choix = input("choix=")
            if choix == "1":
                nom = input("Entrer nom \n")
                num = input("Entrer num \n")
                print(proxy.ajouterEntree(nom,num))
            elif choix == "2":
                nom = input("Entrer nom \n")
                print(proxy.trouverNumero(nom))
            elif choix == "3":
                print(proxy.nbNumeros())
            elif choix == "4":
                print(proxy.getAll())
            elif choix == "5":
                nom = input("Entrer nom \n")
                print(proxy.supprimerEntree(nom))
            elif choix == "6":
                print("Dictionnaire vide")
                print(proxy.supprimerTout())
            elif choix == "0":
                test = False
                sys.exit(0)
            else:
                print("erreur")
                test = False
                sys.exit(0)

    except xmlrpc.client.Fault as err:
            print("A fault occurred")
            print("Fault code: %d" % err.faultCode)
            print("Fault string: %s" % err.faultString)
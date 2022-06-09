from xmlrpc.client import ServerProxy



proxy = ServerProxy("http://localhost:8000/")
while True :
    try: 
        print('Choix de l ’ action a effectuer : ')
        print('1: addition de deux entiers' )
        print('2: la multiplication de deux entier ')
        print('3: différence de deux entiers' )
        print('4: quotient de deux entiers' )
        print('5: la valeur absolu' )
        choix = input("choix=")
        if choix == "1":
                nb1 = input("Entrer nombre 1 \n")
                nb2 = input("Entrer nombre 2 \n")
                print(proxy.add(int(nb1),int(nb2)))
        elif choix == "2":
                nb1 = input("Entrer nombre 1 \n")
                nb2 = input("Entrer nombre 2 \n")
                print(proxy.mult(int(nb1),int(nb2)))
        elif choix == "3":
                nb1 = input("Entrer nombre 1 \n")
                nb2 = input("Entrer nombre 2 \n")
                print(proxy.diff(int(nb1),int(nb2)))
        elif choix == "4":
                nb1 = input("Entrer nombre 1 \n")
                nb2 = input("Entrer nombre 2 \n")
                print(proxy.quotient(int(nb1),int(nb2)))
        elif choix == "5":
                nb1 = input("Entrer un entier \n")
                
                print(proxy.absolu(int(nb1)))
    
    except:
        print("Oops! error")
    
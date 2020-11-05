#compter le nombre de zéro

print("\n")

def binaire():

    n = [1,0,1,0,0,0,1,1,1]                                     #Faire une saisie la liste de nombre

    x = n.count(1) % 2                                          #Compter le nobre de un et faire un modulo par 2 pour avoir un reste

    print("\n")
    print("Votre séquence nombre entier binaire est :", n)      #Afficher n
    print("\n")
    print("Il y a :",n.count(1), " un.")                        #Compter et afficher le nombre de 1
    print("\n")

    if x == 0:                                                  #SI modulo == 0
        print("pair")                                           #Afficher pair

    else:                                                       #SINON
        print("impair")                                         #Afficher impair


    
binaire()                                                       #Executer le programme

#Donner le signe d’un produit de 2 nombres

print("\n")
print("Vérifiez si votre calcul est positif ou négatif.")

def prog():

    print("\n")
    a = input("Entrez un premier nombre : ")     #Première saisie
    print("\n")
    b = input("Entrez un second nombre : ")      #Deuxième saisie
    print("\n")

    try:                                         #Instruction à executer si il n'y a pas d'erreur
        x = int(a)                               #Changer la saisie 'a' en une variable de nombre en 'x'
        y = int(b)                               #Changer la saisie 'b' en une variable de nombre en 'y'
        
        calcul = x * y                           #Calculer le produit de 'x' et 'y'


        if calcul >= 0:                          #Si le résultat est suppérieur ou égal à 0 alors exercuter les instructions suivantes :
            print( x,"*", y, "=", calcul)        #Afficher le résultat du calcul
            print("Votre résultat est positif.") #Afficher que le résultat est positif
            print("\n")

        else:                                    #Si le résultat est strictement inférrieur à 0 alors exercuter les instructions suivantes :
            print( x,"*", y, "=", calcul)        #Afficher le résultat du calcul
            print("Votre résultat est négatif.") #Afficher que le résultat est positif
            print("\n")

    except ValueError:                           #Instruction à executer si il y a une erreur, si les saisies ne sont pas des nombres
        print("Il y a une erreur, saisissez à nouveaux vos nombres.")#Afficher le message d'erreur 
        print("\n")

        return prog()                    #Retourner à la saisie de nombre 'a' et 'b'


prog()                                   #Executer le programme
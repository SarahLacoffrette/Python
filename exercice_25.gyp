#Le programme indique ensuite si l’entier positif est pair ou impair ? Le programme vérifie et redemande l’entier si ce n’est pas un entier positif.

def prog():

    print("\n")
    x = input("Entrez un nombre : ")                                    #Saisie de valeur
    print("\n")

    try:
        X = int(x)       
                                                                        #Instruction à executer si il n'y a pas d'erreur
        if X > 0:                                                       #Si la valeur est positif, executer les instructions

            y = X % 2                                                   #Y est le résultat de 'X' diviser par 2

            if y == 0:                                                  #SI 'y' est égal à 0, exercuter les instructions suivantes :
                print("Votre nombre est paire")                         #Afficher le message
                print("\n")

            else:                                                       #SINON 'y' est n'égal à 0, exercuter les instructions suivantes :
                print("Votre nombre est impaire")                       #Afficher le message
                print("Saisissez à nouveau votre nombre.")
                print("\n")
                return prog()                                           #Retourner à la saisie de nombre 'x'

        else:                                                           #SINON (le nombre est négatif) executer les instructions suivantes
            print("Votre nombre doit être positif, recommencez")        #Afficher le message
            print("\n")    
            return prog()                                               #Retourner à la saisie de nombre

    except ValueError:                                                  #Instruction à executer si il y a une erreur, si les saisies ne sont pas des nombres
        print("Il y a une erreur, saisissez à nouveau votre nombre.")   #Afficher le meesage d'erreur
        return prog()                                                   #Retourner à la saisie de nombre 'x'


prog()                                                                  #Exercuter le programme




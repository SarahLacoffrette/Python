#Faire la somme des carrées des entiers compris en 1 et X.

def prog():

    print("\n")
    x = input("Entrez un nombre suppérieur à 1 : ")                     #Saisie de valeur
    print("\n")

    try:
        X = int(x)                                                      #Instruction à executer si il n'y a pas d'erreur

        calcul = 0

        if X > 1:                                                       #SI 'X' est suppérieur à 1, exercuter les instructions suivantes :
            
            for i in range(1, X + 1):
                y = i ** 2                                        #FORMULE DE LA SOMME DES CARRÉ : 1/6 n (n + 1)(2n + 1)
                calcul = calcul + y 


            print("La somme des carrées des entiers compris en 1 et", x, "est de :", calcul) #Afficher le résultat
            print("\n")

        else:                                                           #SINON si 'X' est infférieur ou égal à O, exercuter les instructions suivantes :
            print("Votre nombre doit être strictement suppérieur à 0.") #Afficher un message
            return prog()                                               #Retourner à la saisie de nombre 'x'

    except ValueError:                                                  #Instruction à executer si il y a une erreur, si les saisies ne sont pas des nombres
        print("Il y a une erreur, saisissez à nouveau votre nombre.")   #Afficher le meesage d'erreur
        return prog()                                                   #Retourner à la saisie de nombre 'x'


prog()                                                                  #Exercuter le programme


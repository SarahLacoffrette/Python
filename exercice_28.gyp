#compter le nombre de zéro

print("\n")

def binaire():

    n = input("Entrez un nombre entier : ")                             #Faire une saisie de nombre

    try:
        n = int(n)                                                      #La saisie 'n' devient une varible nombre
        x = bin(n)                                                      #Convertir en binaire '0b....'
        x = x[2 ::]                                                     #Ne sélectionner qu'à partir de l'index 2

        print("\n")
        print("Votre nombre entier est :", n)                           #Afficher n
        print("\n")
        print("En binaire le résultat est :", x)                        #Afficher x
        print("\n")
        print("Il y a :",x.count('0'), " zéro.")                        #Compter et afficher le nombre de zéro
        print("\n")

    except ValueError:                                                  #Instruction à executer si il y a une erreur, si la saisies n'est' pas un nombre
        print("Vous n'avez pas saisie un nombre entier, recommencez.")  #Afficher message d'erreur
        return binaire()                                                #Retourner à la saisie de nombre 'ligne'


binaire()                                                               #Executer le programme
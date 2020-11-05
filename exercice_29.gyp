#dire si le nombre binaire est pair ou non

print("\n")

def binaire():


    try:                                                                #Instruction à executer si il n'y a pas d'erreur
        n = int(input("Entrez un nombre entier bianire : "), 2)                                 #La saisie 'n' devient une varible nombre 
        print("\n")

        x = n % 2                                                       #'x' est le résultat de 'n' diviser par 2

        if x == 0:                                                      #SI 'x' est égal à 0, exercuter les instructions suivantes :
            print("Votre nombre binaire est paire", "(%s)" % n)         #Afficher le message paire (+ valeur)
            print("\n")

        else:                                                           #SINON 'x' est n'égal à 0, exercuter les instructions suivantes :
            print("Votre nombre binaire est impaire", "(%s)" % n)       #Afficher le message impaire (+ valeur)
            print("\n")

    except ValueError:                                                  #Instruction à executer si il y a une erreur, si la saisies n'est' pas un nombre
        print("Vous n'avez pas saisie un nombre binaire entier, recommencez.")  #Afficher message d'erreur
        return binaire()                                                #Retourner à la saisie de nombre 'ligne'


binaire()                                                               #Executer le programme

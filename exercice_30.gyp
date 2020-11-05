#Demander à l’utilisateur le nombre de ligne et le programme dessine une pyramide.

print("\n")
print("Nous allons réaliser une pyramide d'étoile.")

def pyramide():

    print("\n")
    ligne = input("Entrez le nommbre de ligne pour la dessiner : ")                 #Faire une saisie de nombre
    print("\n")

    try:                                                                            #Instruction à executer si il n'y a pas d'erreur

        x = int(ligne)                                                              #La saisie 'ligne' devient une varible nombre
        etoile = 1
        e = x - 1                                                                   #L'espace entre le début de la ligne et l'étoile

        for i in range(x):                                                          #Executer les instructions pour 'x' lignes
            print(e * ' ',etoile * "*")                                             #Afficher le nombre l'espace et le nombre n'étoile calculer
            etoile = etoile + 2                                                     #Ajouter 2 étoiles pour avoir un effet quinconce
            e = e - 1                                                               #Ajouter un espace 

    except ValueError:                                                              #Instruction à executer si il y a une erreur, si la saisies n'est' pas un nombre
        print("Il y a une erreur, vous n'avez pas saisie un nombre, recommencez.")  #Afficher message d'erreur
        return pyramide()                                                           #Retourner à la saisie de nombre 'ligne'

pyramide()                                                                          #Executer le programme





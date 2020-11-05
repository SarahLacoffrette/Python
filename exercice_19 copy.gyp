#Importer le module de maths

print("\n")

def maths():

    try:

        #Faire saisir à l'utilisateur une valeur

        x = int(input("Entrez la valeur pour calculer sa racine carré: "))

        #FORMULE DE LA RACINE CARRÉ = x ** 1/2

        calcul = x ** (1/2)

        #Afficher le résultat 

        print("La racine carré de :", x,"est :", "%.2f" % calcul)

        #pour afficher seulement 2 chiffre après la virgule, on utilise : "%.2f" % x  (x étant le nombre décimal)

    except ValueError:

        print("Vous n'avez pas saisie un nombre entier, recommencez.")  
        print("\n")
        
        #Afficher message d'erreur

        return maths()

        #Retourner à la saisie de nombre 'x'


maths()

#Executer le programme

print("\n")
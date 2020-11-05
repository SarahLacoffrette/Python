#Faire saisir à l'utilisateur une valeur

print("\n")

def calculProg():


    try:
        r = float(input("entrez le rayon du cercle à calculer (en cm): "))

        #FORMULE DE PÉRIMÈTRE D'UN CERCLE : 2pi * r

        pi = 3.14159265359

        calcul = 2 * pi * r

        #Afficher le résultat 

        print("Le périmètre du cercle est de :", "%.2f" % calcul, "cm")

        #pour afficher seulement 2 chiffre après la virgule, on utilise : "%.2f" % x  (x étant le nombre décimal)

    except ValueError:

        print("Vous n'avez pas saisie un nombre entier, recommencez.")  
        print("\n")
        
        #Afficher message d'erreur

        return calculProg()                                                
        
        #Retourner à la saisie de nombre 'r'


calculProg() 

#Executer le programme


print("\n")

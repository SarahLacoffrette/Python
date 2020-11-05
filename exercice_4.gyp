
def saisie():

    try: 
        
        print("\n")

        #Faire la saisie d'un entier

        saisie = int(input("Entrez un entier : "))

        #afficher la saisie 

        print("La valeur saisie est : ",saisie)

    except ValueError:
        
         print("Errreur")
         print("\n")

         #message d'erreur

         return saisie()

         #Recommencer la saisie

saisie()

#Executer le programme


def time():

    #Faire la saisie en secondes

    print("\n")

    secondes = input("Entrez votre temps en seconde à convertir : ")

    try:
        sec = int(secondes)

        #calcul heure

        heure = sec // 3600

        reste_Heure = sec % 3600 #Le reste de l'heure

        #calcul minutes

        minute = reste_Heure // 60

        #Reste des minutes -> secondes

        secondes = reste_Heure % 60

        #Afficher le résultat

        print("\n")

        print("Le temps est de :", heure, "heures ", minute, "minute(s)", secondes, "seconde(s).")

    except ValueError:
        print("\n")
        print("Il y a une erreur de saisie, recommencez. ")
        return time()

        
time()
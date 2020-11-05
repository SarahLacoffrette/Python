#Faire un jeu du pendu sans limite de tentative



print("\n")
word = input("Entrez un mot : ")            #Saisie du mot pour l'utilisateur 1

print("\n")

word = word.lower()

x = word.isalpha()

#if x == True :
    #game(hide, word, wordV2, essay)

#else:
    #return 

wordV2 = word                               #Avoir deux fois la mot pour un le modifier et l'autre reste intact

L = len(word)                               #Compte du nombre de caractère de la chaîne

hide = '*' * L                              #Faire un nouvelle variable en mot 'caché' par des étoiles par le nombre de cacractère de word

print(hide)                                 #Afficher le mot caché  

essay = 10                                  #Le nombre de tentative




def game(hide, word, wordV2, essay):        #Definir une fonction ayant pour paramètre le mot caché (hide), officiel(word), brouillon(wordV2), et les tentatives(essay)

    while essay == 0:                       #QUAND le nombre de tentative est égal à zéro

        print("Vous avez perdu")            #Afficher perdu

        break                               #Stopper le programme

    else :                                  #SINON, le nombre de tentative n'est pas égal à zéro, executer les instructions

        choice = input("Entrez une lettre : ")              #Faire la saisie d'une lettre à l'utilisateur 2
        choice = choice.lower()                             #Mettre la lettre en minuscule
        star = "*"                                          #Etoile cachée   

        if choice in word or choice in wordV2:              #SI la lettre est dans 'word' ou 'wordV2'alors exectuter les instructions
            
            if choice in wordV2 and choice in word:         #SI la lettre est dans 'word' alors exectuter les instructions
                #print("vrai")  ##Vérification
                a = wordV2.index(choice)                    #Indexer la position de la lettre 'choice' dans le mot 'wordV2'
                hide = hide[:a] + choice + hide[a + 1:]     #Aller à la position 'a' et changer l'étoile '*' en lettre de 'choice'
                print(hide)                                 #Afficher le mot caché

                wordV2 = wordV2[:a] + star + wordV2[a + 1:] #Aller à la position 'a' et changer la lettre de 'choice' en étoile '*'

                #print(wordV2) #Vérification

                if hide == word :                           #SI le mot caché et égal au mot initial
                    print("gagner")                         #Afficher Gagner

                else:                                       #SINON continuer la partie
                    return game(hide, word, wordV2, essay)  #Retourner à la saisie 'choice'

                
            elif choice not in wordV2 and choice in word:   #SINON SI 'choice' n'est pas dans 'wordV2' mais dans 'word'

                print("deja fait")                          #Afficher message

                if hide == word :                           #SI le mot caché et égal au mot initial
                    print("gagner")                         #Afficher Gagner

                else:                                       #SINON continuer la partie
                    return game(hide, word, wordV2, essay)  #Retourner à la saisie 'choice'

            else:                                           #SINON continuer la partie
                return game(hide, word, wordV2, essay)      #Retourner à la saisie 'choice'

        else:                                               #SI la lettre n'est pas dans le word, alors executer les instructions 
            #print("Faux") #Vérification

            essay -= 1                                      #Enlever une tentative pour un échec

            print("Il reste %s tentatives" % essay)         #Afficher message avec reste de tentative

            return game(hide, word, wordV2, essay)          #Retourner à la saisie 'choice'

game(hide, word, wordV2, essay)                             #Executer le programme


#Affiche e1 dès que e1 > e2.

def start():

    e1 = 0
    e2 = 100

    while e1 < e2:              #TANT QUE 'e1' est infférieur à 'e2', excuter les instructions suivantes :
        e1 = e1 + 1             #Incrémenter e1 de 1 
        e2 = e2 - 2             #Décrémenter e2 de 2
        #print(e1, e2)          #(A afficher pour vérifier le programme)

        if e1 > e2:             #SI 'e1' est suppérieur à 'e2', excuter les instructions suivantes :
            print("e1 > e2")    #Afficher le message
            print("e1 =", e1, "> e2 =", e2) #afficher le résultat
            break               #Stopper la boucle WHILE


start()
#Faire la somme et la multiplication des 100 premiers entier positifs.

s = 0                           #Valeur à additionner
m = 1                           #Valeur à multiplier

print("\n")

for x in range(1, 101):         #Répéter l'action de 1 à 100 fois
    m = m * x                   #Pour multiplier
    s = s + x                   #Pour additionner
    print(m, "----------", s)   #Afficher le résultat





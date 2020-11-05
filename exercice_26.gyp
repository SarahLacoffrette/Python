# faire afficher 30 étoiles sur une ligne et 2 chiffre après virgule du nombre 34.30480

etoile = "*"
valeur = 34.30480

print("\n")

print("{}".format("%.2f" % valeur)) #Afficher le format "valeur" avec 2 chiffre après virgule
print("{}".format(etoile) * 30)     #Afficher 30 étoiles

print("\n")
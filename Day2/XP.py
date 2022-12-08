print("EXERCICE 8")

pizza = []
print("Entrez les différentes garnitures de votre pizza et tapez 'quitter' pour marquer la fin de votre liste :")

price = 10
garn = ""
while garn != 'quitter':
    garn = input()
    if garn != 'quitter':
        print("Vous avez ajouté ", garn, "dans votre liste")
        pizza.append(garn)
    price += 2.5
    if 'quitter' == garn:
        break

print("Votre pizza est composé de ces différentes garnitures :",pizza, "et coûtera :", price-2.5)
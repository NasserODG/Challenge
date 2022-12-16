# Demande une chaîne à l'utilisateur
chaine = input("Entrez une chaîne : ")

# Initialise la nouvelle chaîne
nouvelle_chaine = ""

# Parcours chaque caractère de la chaîne
for i in range(len(chaine)):
  # Si le caractère actuel est différent du précédent, ajoute-le à la nouvelle chaîne
  if i == 0 or chaine[i] != chaine[i-1]:
    nouvelle_chaine += chaine[i]

# Affiche la nouvelle chaîne
print(nouvelle_chaine)

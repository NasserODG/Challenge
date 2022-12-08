print("Exercice 11")

sandwich_orders = ["Pastrami sandwich", "Tuna sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches=[]  # ma liste vide de sandwiches finis
k=0     # k nous permettra de determiner le nombre exact de sandwiches préparés
print("INFO!!! la charcuterie n'a plus de pastrami")

# processus pour montrer les supprimer les sandwiches deja faits

    #suppression des pastramis
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
    
while sandwich_orders !=[]:
    sw=input("Quel sandwiche avez vous fini de preparer? ")
    if sw in sandwich_orders:
        sandwich_orders.remove(sw)
        finished_sandwiches.append(sw)
        k=k+1
        
# afficher les chandwiches faits sans les Pastamis
for i in range(0, k):
    print("I made your",finished_sandwiches[i])
    
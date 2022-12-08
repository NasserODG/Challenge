print("Exercice 10")

sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches=[]  # ma liste vide de sandwiches finis
k=0     # k nous permettra de determiner le nombre exact de sandwiches préparés

# processus pour montrer les sandwiches deja faits
while sandwich_orders !=[]:
    sw=input("Quel sandwiche avez vous fini de preparer? ")
    if sw in sandwich_orders:
        sandwich_orders.remove(sw)
        finished_sandwiches.append(sw)
        k=k+1
        
# afficher les chandwiches faits
for i in range(0, k):
    print("I made your",finished_sandwiches[i])
    



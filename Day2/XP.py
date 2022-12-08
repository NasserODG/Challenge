print("EXERCICE 1")

my_fav_numbers = set()

my_fav_numbers.add("60")
my_fav_numbers.add("55")
my_fav_numbers.add("81")
my_fav_numbers.add("28")
print(my_fav_numbers)


my_fav_numbers.add("54")
my_fav_numbers.add("09")
my_fav_numbers.remove("09")
print(my_fav_numbers)

friend_fav_numbers={62, 70}
print(friend_fav_numbers)

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)
print("\n\n")


print("EXERCICE 2")

print("Non ceci n'est pas possible car les tuples sont immuables")
print("\n\n")

print("EXERCICE 3")

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.pop(0)
basket.pop(-1)
basket.append("Kiwi")
basket.insert(0, "Apples")
nbr = basket.count("Apples")
print(basket)
print(nbr)

basket.clear()
print(basket)

print("\n\n")


print("EXERCICE 5")

for x in range(21):
    print(x)

for x in range(0, 21, 2):
    print(x)


print("\n\n")

print("EXERCICE 6")

x = "Nasser"
while True:
    y = input("Entrer un  nom correspondant à mon nom :")
    if y == x:
        print("Vous avez réussis !!!")
        break
    else:
        y = input("Entrer un  nom correspondant à mon nom :")
print("\n\n")

print("EXERCICE 7")

fruit_pref = []
fruit_pref = input("Entrez la liste de vos fruits préférés en laissant seulement des espaces entre eux sur la même ligne :")

fruit = []
fruit = input("Entrez maintenant le nom d'un fruit :")
if fruit in fruit_pref :
    print("Vous avez choisi l'un de vos fruits préférés ! Prendre plaisir!")
else :
    print("Vous avez choisi un nouveau fruit. J'espère que vous appréciez")
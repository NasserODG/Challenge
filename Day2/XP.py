        # EXERCICE 1

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


        #EXERCICE 2

print("Non ceci n'est pas possible car les tuples sont immuables")

        #EXERCICE 3

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
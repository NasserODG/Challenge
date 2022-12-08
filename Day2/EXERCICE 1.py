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

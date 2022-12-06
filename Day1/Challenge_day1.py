word = input("Enter a 10 character string :")
while True :
    if (len(word) < 10):
        print("string not long enough")
        word = input("Enter a 10 character string :")

    elif len(word) > 10:
        print("string too long")
        word = input("Enter a 10 character string :")

    else :
        break
print("\n",word + " have exactly 10 characters")
first_carac = word[0]
last_carac = word[-1]
print("\nThe first character is ", first_carac,"\nAnd the last character is", last_carac)

wrd=""
print("Construct your string character by character :")
for x in word:
    wrd += x
    print("\t",wrd)
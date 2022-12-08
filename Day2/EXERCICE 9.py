print("1_2_3 ")
P=0      #initialisation du prix
nb=int(input("Bonjour! Vous etes au nombre de: "))  #initialisation du nombre de la famille

#Cout a payer en fonction de l'age des membres de la famille
for i in range(0,nb):
    age=int(input("Entrer votre l'age de la personne ?: "))
    print("Personne suivante!")
    if age<3:
        #Billet gratuit
        P=P+0
        
    elif 3<age<=12:
        #Billet coute 10 dollars
        P=P+10
        
    elif age>12:
        #Billet coute 15 dollars
        P=P+15    
 
    
print("Pour tout les (",nb,") personne(s), le montant s'eleve à ",P, "\n\n")


print("4") 
P=0      #initialisation du prix
nb=int(input("Bonjour! Vous etes au nombre de ?: "))  #initialisation du nombre de la famille
Name=[]     #liste des noms enregistrés
k=nb
#Cout a payer en fonction de l'age des membres de la famille
for i in range(0,nb):
    name=input("Entrer votre nom: ")
    age=int(input("Entrer votre age: "))
    Name.append(name)
    print("Enregistré! Passer a la personne suivante...")
    
    
    # verification de l'age

    if 16<=age<=21:
        #Billet coute 10 dollars
        P=P+10
    else:
        #Billet gratuit
        print("Vous n'etes pas autorisé a regarder ce film")
        k=k-1
        
        Name.remove(name) #suppression du nom
           
print(Name)    
print("Pour tout les (",k,") personne(s), le montant s'eleve à ",P)

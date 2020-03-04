divisionPartieEntiere = 10 // 3 


monAge = 21
montant = 299.99
helloWord = "Hello World !"

maSoeur1Age = 21
maSoeur2Age = 17

#permutation
maSoeur1Age,maSoeur2Age = maSoeur2Age,maSoeur1Age

#multi association
prix1 = prix2 = 9.99

type(montant)

print("prix1 =", prix1, "et prix2 =", prix2)

if montant > 200:
    print("trop cher wsh")
elif montant > 100:
    print("cho vo")
else:
    print("po cher")

nom = imput("Saisissez votre nom :")
print("Hello ", nom, "!")

if nom == "Simon" or nom = "simon":
    print("Wsh")
else: 
    print("Bien le bonjour")

i = 0
while i < 7:
    print("Passer la vitesse ", i+=1)

decompte = "3210"
for compte in decompte:
    print(compte)

print("boom")

while 1: 
    lettre = input("Tapez 'Q' pour quitter : ")
    if lettre == "Q":
        print("Fin de la boucle")
        break #ou continue

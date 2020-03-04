from random import randrange

HEADER = '\033[95m'
OKBLUE = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

nbNumero = 8
grille = []
resultat = []
i = 0

while i < nbNumero:
    numero = input("Choisissez un numéro à jouer (1-49) : ")
    if len(numero) == 0:
        numero = randrange(50)
    try: 
        numero = int(numero)
        assert numero > 0 and numero < 50
        grille.append(numero)
    except: 
        print("Entrée invalide")
    else: 
        resultat.append(randrange(50))
        i+=1

print(OKBLUE + "Votre grille : " + str(grille) + ENDC)
print(OKGREEN + "Le tirage : " + str(resultat) + ENDC)

nbSame = nbNumero-len(set(grille) - set(resultat))

print("Vous avez ", nbSame, " numéros !")

if nbSame == nbNumero:
    print("GG bro t riche")
elif nbSame > (nbNumero / 2):
    print("gg 50%")
elif nbSame > 0:
    print("c deja ca")
else:
    print("Try again")

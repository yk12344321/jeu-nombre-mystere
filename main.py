import random


def cycle(x):
    compteur =0
    nrb = random.randint(1, x)
    while True:
        try:
            rep = int(input("Quel nombre penses-tu être le bon ? "))
        except ValueError:
            print("Entre un nombre valide !")
            continue
        compteur += 1
        if rep > nrb:
            print("Plus petit !")
        elif rep < nrb:
            print("Plus grand !")
        else:
            print("Bravo ! Tu as gagné en", compteur, "essais !")
            break


def jeux():
    while True:
        try:
            lvl = int(input("Choisis la difficulté entre 1 et 3 : "))
            if lvl == 1:
                cycle(50)
            elif lvl == 2:
                    cycle(100)
            elif lvl == 3:
                    cycle(500)
            else:
                print("Mets une valeur entre 1 et 3 !")
            while True:
                try:
                    choix = int(input("Voulez-vous rejouer ? (oui=1, non=2) : "))
                
                    if choix == 1:
                        break  # Sort de cette boucle pour relancer le jeu
                
                    elif choix == 2:
                        print("Fin du jeu")
                        exit()
                
                    else:
                        print("Choix invalide, recommence !")
                except ValueError:
                    print("Entre un nombre valide !")
                           
        except ValueError:
            print("Entre un nombre valide !")

jeux()
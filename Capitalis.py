import pandas as pd
import sys
import time

df = pd.read_csv('liste_clean.csv')
df.head()

rejouer = True
max_parties = 0

# Mode multijoueur
print()
nb_joueurs = int(input("Combien de joueurs participent ? "))
print()
joueurs = []
scores = []
for i in range(nb_joueurs):
    nom_joueur = input("Nom du joueur {} : ".format(i + 1))
    joueurs.append(nom_joueur)
    scores.append(0)

while rejouer:
    print()
    max_parties = int(input("Combien de manche(s) voulez-vous jouer ? "))

    for partie in range(1, max_parties + 1):
        print()
        print("Manche", partie)
        print()
        sys.stdout.flush()
        time.sleep(1)  # Attend une seconde pour une pause dramatique

        pays_joues = []  # Liste des pays déjà joués dans la manche

        for i in range(nb_joueurs):
            joueur = joueurs[i]
            score = scores[i]

            pays = df.sample().iloc[0]  # Sélectionne un pays au hasard depuis le DataFrame

            while pays["NOM"] in pays_joues:
                pays = df.sample().iloc[0]  # Sélectionne un autre pays si celui-ci a déjà été joué

            pays_joues.append(pays["NOM"])  # Ajoute le pays à la liste des pays joués

            print("C'est à", joueur, "de jouer.")
            print()
            sys.stdout.flush()
            time.sleep(0.5)  # Attend 0.5 seconde pour une pause dramatique

            print(pays["NOM"])
            sys.stdout.flush()
            time.sleep(0.5)
            print()
            print("Quelle est la capitale de ce pays ?")
            print()
            sys.stdout.flush()
            time.sleep(0.5)

            nom = input()

            compteur_essais = 1
            essais_max = 3

            if nom.strip() == '':
                print("Dommage, la réponse était", pays['CAPITALE'])
                print()
                score -= 1  # Décrémente le score de -1 en cas de réponse vide
            else:
                
                while True:
                    nom = input("Essaie encore : ")
                    if nom.lower() == pays['CAPITALE'].lower():
                        print("Bravo, c'est gagné !")
                        score += 1  # Incrémente le score en cas de bonne réponse
                        break  # Sort de la boucle pour passer au joueur suivant ou à la manche suivante
                    elif nom.strip() == '':
                        print("Dommage, la réponse était", pays['CAPITALE'])
                        score -= 1  # Décrémente le score de -1 en cas de réponse vide
                        break  # Sort de la boucle pour passer au joueur suivant ou à la manche suivante
                    elif compteur_essais == essais_max:
                        print("Plus d'essais. La réponse était", pays['CAPITALE'])
                        score -= 1  # Décrémente le score de -1 en cas d'échec d'essais
                        break  # Sort de la boucle pour passer au joueur suivant ou à la manche suivante
                    else:
                        compteur_essais += 1

            print("Score actuel pour", joueur + ":", score)
            print()

            scores[i] = score  # Met à jour le score dans la liste des scores

        print("Scores après la manche", partie)
        print()
        for i in range(nb_joueurs):
            joueur = joueurs[i]
            score = scores[i]
            print("Score de", joueur + ":", score)
        print()
        sys.stdout.flush()
        time.sleep(1)  # Attend une seconde avant de passer à la prochaine manche

    print("Scores finaux")
    print()
    for i in range(nb_joueurs):
        joueur = joueurs[i]
        score = scores[i]
        print("Score de", joueur + ":", score)
    print()
    sys.stdout.flush()
    time.sleep(1)  # Attend une seconde avant de demander si les joueurs veulent rejouer

    choix_rejouer = input("Voulez-vous rejouer ? (Oui/Non) ")
    print()
    sys.stdout.flush()

    if choix_rejouer.lower() != "oui":
        print("Merci à bientôt !")
        sys.stdout.flush()
        time.sleep(1)  # Attend une seconde avant de quitter le programme
        rejouer = False

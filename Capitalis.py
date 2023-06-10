import pandas as pd
import random
import sys
import time

def jeu_departement(nom_joueur, score, deps_joues):
    deps = pd.read_csv('depts_fr_clean.csv')
    departement = deps.sample().iloc[0]

    while departement['nom_departement'] in deps_joues:
        departement = deps.sample().iloc[0]

    deps_joues.append(departement['nom_departement'])

    print("C'est au tour de", nom_joueur)
    print()
    print(departement['code_departement'])
    print()
    print('A quel département correspond ce numéro ?')
    print()

    nom = input()

    compteur_essais = 0
    essais_max = 3

    if nom.strip() == '':
        print("Dommage, la réponse était", departement['nom_departement'])
        print()
        score -= 1
    else:
        while compteur_essais < essais_max:
            compteur_essais += 1
            if nom.lower() == departement['nom_departement'].lower():
                print('Bonne réponse !')
                score += 1
                break
            elif nom.strip() == '':
                print("Dommage, la réponse était", departement['nom_departement'])
                score -= 1
                break
            elif compteur_essais == essais_max:
                print("Plus d'essais. La réponse était", departement['nom_departement'])
                score -= 1
                break
            else:
                print('Essaie encore')
                nom = input()

    return score

df = pd.read_csv('liste_clean.csv')
df.head()

rejouer = True
max_parties = 0

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
    scores = [0] * nb_joueurs

    print()
    max_parties = int(input("Combien de manche(s) voulez-vous jouer ? "))
    print()
    jeu_choisi = input("Choisissez le jeu (1. Capitales, 2. Départements français) : ")

    for partie in range(1, max_parties + 1):
        print("Manche", partie)
        print()
        sys.stdout.flush()
        time.sleep(1)

        scores_manche = [0] * nb_joueurs

        pays_joues = []
        deps_joues = []

        for i in range(nb_joueurs):
            joueur = joueurs[i]
            score = scores_manche[i]

            if jeu_choisi == "1":
                pays = df.sample().iloc[0]

                while pays["NOM"] in pays_joues:
                    pays = df.sample().iloc[0]

                pays_joues.append(pays["NOM"])

                print("C'est à", joueur, "de jouer.")
                print()
                sys.stdout.flush()
                time.sleep(0.5)

                print(pays["NOM"])
                sys.stdout.flush()
                time.sleep(0.5)
                print()
                print("Quelle est la capitale de ce pays ?")
                print()
                sys.stdout.flush()
                time.sleep(0.5)

                nom = input()

                compteur_essais = 0
                essais_max = 3

                if nom.strip() == '':
                    print("Dommage, la réponse était", pays['CAPITALE'])
                    print()
                    score -= 1
                else:
                    while compteur_essais < essais_max:
                        compteur_essais += 1
                        if nom.lower() == pays['CAPITALE'].lower():
                            print('Bonne réponse !')
                            score += 1
                            break
                        elif nom.strip() == '':
                            print("Dommage, la réponse était", pays['CAPITALE'])
                            score -= 1
                            break
                        elif compteur_essais == essais_max:
                            print("Plus d'essais. La réponse était", pays['CAPITALE'])
                            score -= 1
                            break
                        else:
                            print('Essaie encore')
                            nom = input()
            elif jeu_choisi == "2":
                score = jeu_departement(joueur, score, deps_joues)

            print("Score actuel pour", joueur + ":", score)
            print()

            scores_manche[i] = score

        for i in range(nb_joueurs):
            scores[i] += scores_manche[i]

        print("Scores après la manche", partie)
        print()
        for i in range(nb_joueurs):
            joueur = joueurs[i]
            score = scores[i]
            print("Score de", joueur + ":", score)
        print()
        sys.stdout.flush()
        time.sleep(1)

    max_score = max(scores)
    winners = [joueur for joueur, score in zip(joueurs, scores) if score == max_score]
    num_winners = len(winners)

    if num_winners == 1:
        print("The winner is", winners[0] + "!")
    else:
        print("It's a tie! The winners are:")
        for winner in winners:
            print(winner)

    print("Scores finaux")
    print()
    for i in range(nb_joueurs):
        joueur = joueurs[i]
        score = scores[i]
        print("Score de", joueur + ":", score)
    print()
    sys.stdout.flush()
    time.sleep(1)

    choix_rejouer = input("Voulez-vous rejouer ? (Oui/Non) ")
    print()
    sys.stdout.flush()

    if choix_rejouer.lower() != "oui":
        print("Merci à bientôt !")
        sys.stdout.flush()
        time.sleep(1)
        rejouer = False

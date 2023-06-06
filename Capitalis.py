import pandas as pd
import random
import sys
import time

def jeu_departement(nom_joueur, score):
    deps = pd.read_csv('depts_fr_clean.csv')
    departement = deps.sample().iloc[0]
    
    print("C'est au tour de", nom_joueur)
    print(departement['code_departement'])
    print('A quel département correspond ce numéro ?')
    print()
    
    nom = input()

    compteur_essais = 0
    essais_max = 3

    if nom.strip() == '':
        print("Dommage, la réponse était", departement['nom_departement'])
        print()
        score -= 1  # Décrémente le score de -1 en cas de réponse vide
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
    scores = [0] * nb_joueurs  # Réinitialiser les scores des joueurs avant chaque nouvelle partie

    print()
    max_parties = int(input("Combien de manche(s) voulez-vous jouer ? "))
    jeu_choisi = input("Choisissez le jeu (1. Capitales, 2. Départements français) : ")

    for partie in range(1, max_parties + 1):
        print("Manche", partie)
        print()
        sys.stdout.flush()
        time.sleep(1)  # Attend une seconde pour une pause dramatique

        scores_manche = [0] * nb_joueurs  # Scores individuels de la manche

        pays_joues = []  # Liste des pays déjà joués dans la manche
        deps_joues = []  # Liste des numéros de département déjà joués dans la manche

        for i in range(nb_joueurs):
            joueur = joueurs[i]
            score = scores_manche[i]  # Score individuel de la manche

            if jeu_choisi == "1":
                pays = df.sample().iloc[0]  # Sélectionne un pays au hasard depuis le DF

                while pays["NOM"] in pays_joues:
                    pays = df.sample().iloc[0]  # Sélectionne un autre pays si celui-ci a déjà été joué

                pays_joues.append(pays["NOM"])  # Ajoute le pays à la liste des pays joués

                print("C'est à", joueur, "de jouer.")
                print()
                sys.stdout.flush()
                time.sleep(0.5)  # Attend 0.5 secondes

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
                    score -= 1  # Décrémente le score de -1 en cas de réponse vide
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
                score = jeu_departement(joueur, score)

            print("Score actuel pour", joueur + ":", score)
            print()

            scores_manche[i] = score  # Mettre à jour le score individuel de la manche

        for i in range(nb_joueurs):
            scores[i] += scores_manche[i]  # Ajouter le score individuel de la manche au score total du joueur

        print("Scores après la manche", partie)
        print()
        for i in range(nb_joueurs):
            joueur = joueurs[i]
            score = scores[i]
            print("Score de", joueur + ":", score)
        print()
        sys.stdout.flush()
        time.sleep(1)  # Attend une seconde avant de passer à la prochaine manche

    # Determine the winner
    max_score = max(scores)
    winners = [joueur for joueur, score in zip(joueurs, scores) if score == max_score]
    num_winners = len(winners)

    # Display the winner
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
    time.sleep(1)  # Attend une seconde avant de demander si les joueurs veulent rejouer

    choix_rejouer = input("Voulez-vous rejouer ? (Oui/Non) ")
    print()
    sys.stdout.flush()

    if choix_rejouer.lower() != "oui":
        print("Merci à bientôt !")
        sys.stdout.flush()
        time.sleep(1)  # Attend une seconde avant de quitter le programme
        rejouer = False

import pygame
import pandas as pd
import random
import sys
import time

def afficher_texte(texte, x, y, taille=30, couleur=(255, 255, 255)):
    font = pygame.font.Font(None, taille)
    surface_texte = font.render(texte, True, couleur)
    screen.blit(surface_texte, (x, y))

def jeu_departement(nom_joueur, score):
    deps = pd.read_csv('depts_fr_clean.csv')
    departement = deps.sample().iloc[0]
    
    afficher_texte("C'est au tour de " + nom_joueur, 50, 50)
    afficher_texte(departement['code_departement'], 50, 100)
    afficher_texte('A quel département correspond ce numéro ?', 50, 150)
    
    nom = ''
    input_actif = True

    while input_actif:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_actif = False
                elif event.key == pygame.K_BACKSPACE:
                    nom = nom[:-1]
                else:
                    nom += event.unicode

        screen.fill((0, 0, 0)) 
        afficher_texte("C'est au tour de " + nom_joueur, 50, 50)
        afficher_texte(departement['code_departement'], 50, 100)
        afficher_texte('A quel département correspond ce numéro ?', 50, 150)
        afficher_texte(nom, 50, 200)
        pygame.display.flip()

    if nom.strip() == '':
        afficher_texte("Dommage, la réponse était " + departement['nom_departement'], 50, 250)
        score -= 1
    else:
        if nom.lower() == departement['nom_departement'].lower():
            afficher_texte('Bonne réponse !', 50, 250)
            score += 1
        else:
            afficher_texte('Mauvaise réponse. La réponse était ' + departement['nom_departement'], 50, 250)
            score -= 1

    pygame.display.flip()
    time.sleep(2)

    return score

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jeu de géographie")

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

                afficher_texte("C'est à " + joueur + " de jouer.", 50, 50)
                afficher_texte(pays["NOM"], 50, 100)
                afficher_texte("Quelle est la capitale de ce pays ?", 50, 150)

                nom = ''
                input_actif = True

                while input_actif:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                input_actif = False
                            elif event.key == pygame.K_BACKSPACE:
                                nom = nom[:-1]
                            else:
                                nom += event.unicode

                    screen.fill((0, 0, 0))
                    afficher_texte("C'est à " + joueur + " de jouer.", 50, 50)
                    afficher_texte(pays["NOM"], 50, 100)
                    afficher_texte("Quelle est la capitale de ce pays ?", 50, 150)
                    afficher_texte(nom, 50, 200)
                    pygame.display.flip()

                if nom.strip() == '':
                    afficher_texte("Dommage, la réponse était " + pays['CAPITALE'], 50, 250)
                    score -= 1
                else:
                    if nom.lower() == pays['CAPITALE'].lower():
                        afficher_texte('Bonne réponse !', 50, 250)
                        score += 1
                    else:
                        afficher_texte('Mauvaise réponse. La réponse était ' + pays['CAPITALE'], 50, 250)
                        score -= 1

                pygame.display.flip()
                time.sleep(2)

            elif jeu_choisi == "2":
                score = jeu_departement(joueur, score)

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
        print("Le gagnant est", winners[0] + "!")
    else:
        print("Égalité ! Les gagnants sont :")
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
        print("Merci et à bientôt !")
        sys.stdout.flush()
        time.sleep(1)
        rejouer = False

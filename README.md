Jeu des capitales pour des soirées endiablées.

Composition des fichiers:

- liste = Liste d'origine trouvée en ligne
- list_clean = Liste nettoyée
- Nettoyage data = Jupyter notebook de nettoyage des données
- depts_fr = Liste origine pour les départements FR
- depts_fr_clean = Liste nettoyée
- Nettoyage depts = Jupyter notebook de nettoyage des données
- Capitalis.py = Jeu à lancer dans la ligne de commande voici les étapes à suivre:
- Visuel.py = test de mise en place d'un visuel sous python

Installation

Prérequis: Python et le module Pandas doivent être installés 

- I/ Ouvrir la ligne de commande (ctrl + r)
- II/ Placer vous dans le dossier dans lequel se trouve l'ensemble des fichiers de ce repo (cd c/user/etc...)
- III/ Taper la commande suivante : "python Capitalis.py"

Une fois le jeu lancé, sélectionnez le nombre de joueurs et ajoutez les noms. Enfin choisissez le nombre de manches que vous souhaitez effectuer
(1 manche = 1 capitale à deviner par joueur).

Informations complétementaires: une réponse vide sera comptabilisée comme "je ne sais pas", un point sera déduit du score et la main passera au joueur suivant.
Une bonne réponse vaut 1 point, une mauvaise vaut -1, il est possible d'avoir des scores négatifs. Les scores sont affichés à la fin de chaque manque 
et à la fin de la partie.
Le jeu peut se jouer en solo.


**Update 06/06/2023**: Ajout d'un mode départements français, sur le même principes que les capitales, un numéro s'affiche, à vous de trouver à quel département il appartient. Le système de scoring fonctionne de la même façon que pour les capitales.

#Prochaine étape: 

- création d'un visuel
- création d'un fichier .exe

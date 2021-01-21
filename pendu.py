# pylint: disable=unused-variable
# pylint: enable=too-many-lines
# -*- coding: utf-8 -*-
"""
VSCode c'est quand même mieux !
"""
import fonction # Deuxième fichier indispensable
import random # Pour prendre un mot aléatoire dans la liste de mot 
import getpass # Pour saisir le mot 
import sys # Pour pouvoir arrêter le programme 

numEcran = 0 # Nombre de tentative. Le nom est très mauvais mais on m'a dit de respecter les consignes. -_- 

mot = fonction.definirMotRecherche() 
print(mot)
motEnCours = ["_" for i in mot] # Mettre autant de tirets qu'il y a de lettres dans le mot correct dans le mot trouvé

motEnCours[0] = mot[0] # On donne généreusement la première lettre du mot à trouver par l'utilisateur
print(motEnCours) 

while fonction.motDecouvert(motEnCours) == False: # Tant que l'utilisateur n'a pas trouvé (utilisation de la fonction motDecouvert pour savoir s'il reste un ou plusieurs tirets dans le mot à trouver)
    char = input("Quelle lettre voulez-vous essayer ?   ").upper() # On demande à l'utilisateur une lettre que l'on stocke en majuscule

    result = fonction.chercheLettreDansMot(mot, char, motEnCours) # On appelle la fonction chercheDansMot() et l'on stocke le résultat dans un tableau avec comme premier élément le mot découvert et comme deuxième élément si une ou plusieurs lettre ont été trouvé
    motEnCours = result[0] # la première variable retournée dans result est le mot en court de découverte

    print(motEnCours) # On affiche à l'utilisateur le mot en cours de découverte

    if result[1] == False: # SI la lettre proposée par l'utilisateur n'est pas dans le mot à découvrir
        numEcran += 1 # On incrémente la variable permettant l'affichage du pendu
        
        if fonction.dessinPendu(numEcran) == "perdu": # On appelle la fonction pour afficher l'état du pendu
            sys.exit() # Si la fonction retourne "perdu", alors on quitte le programme

print("VOUS AVEZ GAGNE !") # Lorsque l'on a quitté la boucle while (ce qui veut dire que la fonction vérifiant la victoire retourne True), alors on affiche que l'utilisateur à gagné
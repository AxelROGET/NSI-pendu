import random
import sys
import getpass

def dessinPendu(tentatives):
    """
        Affiche dans la console le dessin du pendu.
        tentatives : int avec le nombre de tentatives
    """
    if tentatives==0:
        print("==============\n")
    if tentatives==1:
        print(" ||/")
        for i in range(5):
            print(" ||")
        print("/||           ")
        print("==============\n")
    if tentatives==2:
        print("==============")
        print(" ||/")
        for i in range(5):
            print(" ||")
        print("/||           ")
        print("==============\n")
    if tentatives==3:
        print("==============")
        print(" ||/     |")
        for i in range(5):
            print(" ||")
        print("/||           ")
        print("==============\n")
    if tentatives==4:
        print("==============")
        print(" ||/     |")
        print(" ||      O")
        for i in range(4):
            print(" ||")
        print("/||           ")
        print("==============\n")
    if tentatives==5:                    
        print("==============")
        print(" ||/     |")
        print(" ||      O")
        print(" ||    ----- ")
        for i in range(3):
            print(" ||")
        print("/||           ")
        print("==============\n")
    if tentatives==6:
        print("==============")
        print(" ||/     |")
        print(" ||      O")
        print(" ||    ----- ")
        print(" ||      |")
        for i in range(2):
            print(" ||")
        print("/||           ")
        print("==============\n")
    if tentatives==7:
        print("==============")
        print(" ||/     |")
        print(" ||      O")
        print(" ||    ----- ")
        print(" ||      |")
        print(" ||     / \ ")
        print(" ||")
        print("/||           ")
        print("==============\n")
        print("VOUS AVEZ PERDU")
        return "perdu"

def definirMotRecherche():
    """
        Demander à l'utilisteur combien il y a de joueurs.
        S'il n'y a qu'un joueur, il va prendre un mot aléatoirement dans une liste.
        S'il y a deux joueurs ou plus, demander à un des joueurs de sélectionner un mot à la main.

        Pas de variables requises.
    """
    if input("Entrez le nombre de joueurs (s'il y a un joueur, le mot à trouver sera choisi aléatoirement. S'il y a plusieurs joueurs, le mot sera à entrer) :") == "1":
        # S'il n'y a qu'un joueur :
        f = open("liste.txt", "r") # On ouvre le document liste.txt
        dictionnaire = [i[0:len(i)-1] for i in f] # On stocke chaque mot dans un tableau sans prendre le dernier caractère pour chaque pour ignore \n

        return [i for i in random.choice(dictionnaire)] # prendre un mot aléatoire et découper ce mot dans un tableau
    
    else: # S'il y a plusieurs joueurs :
        mot = getpass.getpass(prompt="Saisir un mot : ").upper() # Demander à un des joueurs de saisir un mot 

        return [i for i in mot] # Retourner un tableau dans lequel le mot envoyé est découpé

def chercheLettreDansMot(mot, lettre, motEnCours):
    """
        retourne le mot en cours de recherche avec les lettres trouvées ainsi que si la lettre sélectionnée est bonne.
        [motEnCours (list), correct (bool)]
    """
    correct = False
    for i in range(len(mot)): # Pour chaque lettre du mot à trouver :
        if mot[i] == lettre and motEnCours[i] == '_': # Si la lettre entrée est la même que celle du mot à trouver :
            motEnCours[i] = lettre # On modifie motEnCours pour mettre la lettre à celle entrée
            correct = True # La lettre entrée est correct
    return [motEnCours, correct] # On retourne motEnCours et si le joueur a bon

def motDecouvert(motEnCours):
    """
        Renvoie true si le mot à découvrir ne contient pas de tiret donc que le mot est trouvé entièrement.
        Envoie false dans le cas contraire.
    """
    if "_" in motEnCours: # Si il y a un tiret dans le mot en cours
        return False # Retourner que le joueur n'a pas trouvé
    else: return True # Retourner que le joueur à gagné

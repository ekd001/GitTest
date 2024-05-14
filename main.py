from afficher_sinistre import afficher_sinistre
from validation_attente import *
from valider_demande import *
from information_client import *
from sinistre import *
import os

def lancement():
    start = True
    while(start):
        print("LES OPERATIONS\n")
        print("1-Afficher les damandes en attente\n")
        print("2-Valider les demandes\n")
        print("3-Informations du client\n")
        print("4-Afficher le dernier dossier sinistre\n")
        print("5-Enrégistrer un dossier sinistre\n")
        print("6-Quitter\n")

        x = (int)(input("Entrer votre choix : "))
        if(x == 1 ):
            validation_attente()
            os.system('cls')
            lancement()
        elif(x==2):
            valider_demande()
            lancement()
        elif(x==3):
            info_client()
            lancement()
        elif(x==4):
            afficher_sinistre()
            lancement()
        elif(x==5):
            sinistre()
            lancement()
        elif(x==6):
            break
        else:
            lancement()

lancement()
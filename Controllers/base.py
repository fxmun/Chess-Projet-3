from typing import List
import datetime
import random

from Models.base import Tournoi
from Models.base import Joueur
from Models.base import List_joueur
from Models.base import List_match
from Models.base import Tour
from Models.base import Ctrl_temps
from Models.base import Match
from Models.base import Tirage
from Models.base import Resultat
from Models.base import Tri
from Views.creation import Creation


class Initialise:
    """initialisation du tournoi"""
    
    colect = Creation.prompt_create_tournoi(Creation)
    nom = colect['nom']
    lieu = colect['lieu']
    date = colect['date']
    description = colect['description']
    
    def __init__(self, view):
        """a une vue"""
        self.view = view
        return

    def run(self):
        """debute le tournoi."""
        return
    
    def create_tournoi(nom, lieu, date, description):
        """creation d'un tournoi en mémoire"""
        tournoi = Tournoi(nom, lieu, date,description)
        return tournoi
    tournoi = create_tournoi(nom, lieu, date, description)
    Creation.show_tournoi(tournoi)
    
    def edit_joueurs():
        """édition des joueurs par la vue"""
        joueurs = []
        view = Creation()
        for one in range(8):
            joueur = view.prompt_create_joueur()
            joueurs.append(joueur)
        return joueurs
    global joueurs
    joueurs = edit_joueurs()
    
    def create_joueurs(joueurs):
        """création des joueurs en mémoire"""    
        for player in joueurs:
            i = joueurs.index(player)
            joueurs[i] = Joueur(player[0], player[1], player[2], player[3], player[4])
            #print(joueurs[i])
        list_joueur = []
        l = len(joueurs)
        i = 0
        while i <= l-1:
            list_joueur.append(i)
            i += 1
        return list_joueur, joueurs
    global list_joueur
    list_joueur, joueurs = create_joueurs(joueurs)
    #print(list_joueur)
    Creation.show_joueurs(joueurs)

    def create_list_joueur(list_joueur):
        """creation d'une liste de joueurs en mémoire"""
        list_joueur = List_joueur(list_joueur)
        return list_joueur
    list_joueur = create_list_joueur(list_joueur)
    print(list_joueur)           

    def edit_temps_game():
        """edition de la cadence des matchs par la vue"""
        view = Creation()
        cadence = view.prompt_create_cadence()
        return cadence
    cadence = edit_temps_game()
    #print(cadence)

    def create_cadence(cadence):
        """creation en mémoire de la cadence"""
        if cadence =='1':
            cadence = Ctrl_temps(True, False, False)
        elif cadence == '2':
            cadence = Ctrl_temps(False, True, False)
        elif cadence == '3':
            cadence = Ctrl_temps(False, False, True)
        else:
            pass
        return cadence
    cadence = create_cadence(cadence)
    print(cadence)
    
class Rank:
    """classement des joueurs"""
    def __init__(self, list_joueur, joueurs):
        self.list_joueur = list_joueur
        self.joueurs = joueurs
        pass

    def init_classement():
        """initialisation du classement en fonction du parametre "classement" de "create_joueurs" edité par la vue"""
        rangs = []
        for i in joueurs:
            rang = i.classement
            rangs.append(rang)
        return rangs
    rangs = init_classement()
    #print(rangs)

    def create_classement(rangs):
        """création du classement en mémoire"""

        pass

class Build:
    """constuit le tournoi"""
    def __init__(self, list_joueur, nombre_tour = 4):
        pass

    def create_round_1():
        liste = list_joueur.list_joueur
        #print(liste)
        for nb in liste:
            list_1 = list_joueur.list_joueur
            pairs = []
            tirages = []
            parties = []
            while len(list_1):
                pair = List_match(list_1[0], list_1[1])
                pairs.append(pair)
                tirage = Tirage(list_1[0], list_1[1])
                tirages.append(tirage)
                partie = Match(list_1[0], list_1[1])
                parties.append(partie)
                list_1 = list_1[2:]  
            #print(pairs)
            #print(tirages)
            #print(parties)
            nom_tour = "Round " + str(liste.index(nb))
            begin_time = datetime.datetime.now()
            end_time = datetime.datetime.now()
            tour = Tour(nom_tour, begin_time, end_time)
            #print(nom_tour, begin_time, end_time)
            return  pairs, tirages, parties, tour
            pass

    global parties
    pairs, tirages, parties, tour = create_round_1()
    print(pairs)
    print(tirages)
    print(parties)
    print (tour)

    def create_other_round():
        pass


class Play:
    """jouer les rencontres"""
    def __init__(self, parties, score):
        self.parties = parties
        self.score = score
        
    def edit_resultat():
        """score aléatoire initié par la vue"""
        score = Creation.prompt_edit_result()
        points = [0, 0.5, 1]
        alea = random.choice(points)
        if alea == 0:
            score.append(0)
            score.append(1)
        elif alea == 0.5:
            score.append(0.5)
            score.append(0.5)
        elif alea == 1:
            score.append(1)
            score.append(0)
        pass
        return score
    score = edit_resultat()
    #print(score)

    def create_resultat(score):
        """creation du resultat en memeoire"""
        resultats = []
        for jeu in parties:
            resultat = Resultat(jeu, score[0], score[1])
            resultats.append(resultat)
        return resultats
    resultats = create_resultat(score)
    print(resultats)
    
    """crée les tours du tournoi"""
    '''half_1 = []
    #all = len(list_joueur)
    #sub = all / 2
    half_1.append(list_joueur[:-4])
    half_2 = []
    half_2.append(list_joueur[4:])
    return half_1, half_2
    half_1, half_2 = create_round()
    #print(half_1)
    #print(half_2)
    pass'''     
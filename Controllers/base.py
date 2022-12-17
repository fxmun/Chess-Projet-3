from typing import List
import datetime
import random

from Models.base import Tournoi
from Models.base import Joueur
from Models.base import List_joueur
from Models.base import Ctrl_temps
from Models.base import Classement
from Models.base import List_match
from Models.base import Tirage
from Models.base import Tour
from Models.base import Resultat
from Models.base import Tri
from Views.creation import Creation
from Models.base import Table_joueur

class Initialise:
    """initialisation du tournoi"""
    def __init__(self, view):
        """a une vue"""
        self.view = view
        return

    def run(self):
        """debute le tournoi."""
        return
    
    def edit_tournoi():
        """édition des caractéristiques du tournoi"""
        view = Creation
        tournoi = view.prompt_create_tournoi(view)
        return tournoi
    
    tournoi = edit_tournoi()
    #print(tournoi)

    def create_tournoi(tournoi):
        """creation d'un tournoi en mémoire"""
        tournoi = Tournoi(tournoi[0], tournoi[1], tournoi[2], tournoi[3])
        return tournoi
    
    tournoi = create_tournoi(tournoi)
    print(tournoi)
    
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
    #print(joueurs)
    
    def create_joueurs(joueurs):
        """création des joueurs en mémoire"""    
        
        for caracterise in joueurs:
            i = joueurs.index(caracterise)
            joueurs[i] = Joueur(caracterise[0], caracterise[1], caracterise[2], caracterise[3], caracterise[4])
        return joueurs    
    
    joueurs = create_joueurs(joueurs)
    print(joueurs)

    def edit_list_joueurs():
        """edition de la liste des joueurs"""     
        list_joueur = []
        l = len(joueurs)
        i = 0
        while i <= l-1:
            list_joueur.append(i)
            i += 1
        return list_joueur
    
    global list_joueur
    list_joueur = edit_list_joueurs()
    #print(list_joueur)

    def create_list_joueur(list_joueur):
        """creation d'une liste de joueurs en mémoire"""
        list_joueur = List_joueur(list_joueur)
        return list_joueur
    
    list_joueur = create_list_joueur(list_joueur)
    print(list_joueur)           

    def edit_cadence():
        """edition de la cadence des matchs par la vue"""
        view = Creation()
        cadence = view.prompt_create_cadence()
        return cadence
    cadence = edit_cadence()
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
        rangs = Classement(rangs)
        return rangs
    
    rangs = create_classement(rangs)
    print(rangs)

class Build:
    """constuit le tournoi"""
    def __init__(self, list_joueur, nombre_tour = 4):
        pass
    
    def edit_round():
        tours = []
        for tour in range(4):
            numero_tour = range(4).index(tour)
            tours.append(numero_tour)
        return tours
    tours = edit_round()

    def create_round(tours):
        liste = Rank.init_classement()
        for joueur in liste:
            pairs = []
            tirages = []
            while len(liste):
                i = 0
                if len(liste) > 4:
                    j = 4
                elif len(liste) == 4:
                    j = 2
                elif len(liste) == 2:
                    j = 1
                else:
                    pass    
                pair = List_match(liste[i], liste[j])
                j -= 1
                pairs.append(pair)
                couleurs = ['blanc', 'noir']
                couleur = random.choice(couleurs)
                if couleur == 'blanc':
                    tirage = Tirage(couleurs[0], couleurs[1])
                    tirages.append(tirage)
                elif couleur == 'noir':
                    tirage = Tirage(couleurs[1], couleurs[0])
                    tirages.append(tirage)
                else:
                    pass
                
                liste = liste[2:]  
            #print(pairs)
            #print(tirages)
            
            nom_tour = "Round " + str(tours[0])
            begin_time = datetime.datetime.now()
            end_time = datetime.datetime.now()
            tour = Tour(nom_tour, begin_time, end_time)
            #print(nom_tour, begin_time, end_time)
            return  pairs, tirages, tour
            pass

    global pairs
    pairs, tirages, tour = create_round(tours)
    print(pairs)
    print(tirages)
    print (tour)

    def create_other_round():
        pass


class Play:
    """jouer les rencontres"""
    def __init__(self, pairs, score):
        self.tour = tour
        self.score = score
        
    def edit_resultat():
        """score aléatoire initié par la vue"""
        score = Creation.prompt_edit_result()
        points = [0, 0.5, 1]
        for jeu in pairs:
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
        for jeu in pairs:
            resultat = Resultat(jeu, score[0], score[1])
            resultats.append(resultat)
            score = score[2:]
        return resultats
    resultats = create_resultat(score)
    print(resultats)
    
    def create_new_classement(joueurs, resultats):
        """creation du classement après le premier tour"""
        noms = []
        scores = []
        i = 0
        for pair in pairs:
            nom_1 = joueurs[i].nom
            noms.append(nom_1)
            i += 1
            nom_2 = joueurs[i].nom
            noms.append(nom_2)
            #print(nom_1, nom_2)
            i += 1
        
        for resultat in resultats:
            i = resultats.index(resultat)
            resultat = resultats[i].pts_joueur_1
            scores.append(resultat)
            resultat = resultats[i].pts_joueur_2
            scores.append(resultat)
        
        new_classement = Tri(noms, scores)
        return new_classement
    new_classement = create_new_classement(joueurs, resultats)
    print(new_classement)

    def create_table_joueur(new_classement):
        """creation en memoire d'un tableau du score de chaque joueur"""
        noms = new_classement.name
        scores = new_classement.resultat
        table_joueurs = []
        for nom in noms:
            i = noms.index(nom)
            table_joueur = Table_joueur(noms[i], scores[i])
            table_joueurs.append(table_joueur)
        return table_joueurs
    table_joueurs = create_table_joueur(new_classement)
    print(table_joueurs)

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
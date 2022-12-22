from typing import List
import datetime
from operator import itemgetter
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
from Models.base import Table_joueur
from Views.creation import Creation

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
        tournoi = Tournoi(tournoi[0], tournoi[1], tournoi[2], tournoi[3], tournoi[4])
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

    def nom_par_classement():
        """restitue un classement initial par nom"""
        noms = []
        classements = []
        results = []
        for nom in joueurs:
            i = joueurs.index(nom)
            j = joueurs[i].nom
            noms.append(j)
            k = joueurs[i].classement
            classements.append(k)
        results = [x for _ , x in sorted(zip(classements,noms), reverse = True)]
        return results

    global results
    results = nom_par_classement()
    print(results)

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
        gamers = []
        rangs = []
        for i in joueurs:
            gamer = i.nom
            rang = i.classement
            gamers.append(gamer)
            rangs.append(rang)
        tri_rangs = [x for _ , x in sorted(zip(rangs,gamers), reverse = True)]
        return tri_rangs

    global tri_rangs
    tri_rangs = init_classement()
    #print(tri_rangs)

    def create_classement(tri_rangs):
        """création du classement en mémoire"""
        obj_rangs = Classement(tri_rangs)
        return obj_rangs
    
    obj_rangs = create_classement(tri_rangs)
    print(obj_rangs)

class Build:
    """constuit le tournoi"""
    def __init__(self):
        pass
    
    def create_round_1(tri_rangs):   
        liste = tri_rangs
        pairs = []
        suite = []
        tirages = []
        while liste:
            if len(liste) == 8:
                i = liste[0]
                j = liste[4]
                pair = List_match(i, j)
                pairs.append(pair)
                suite.append(i)
                suite.append(j)
                liste.pop(0)
                liste.pop(3)
                
            elif len(liste) == 6:
                i = liste[0]
                j = liste[3]
                pair = List_match(i, j)
                pairs.append(pair)
                suite.append(i)
                suite.append(j)
                liste.pop(0)
                liste.pop(2)     

            elif len(liste) == 4:
                i = liste[0]
                j = liste[2]
                pair = List_match(i, j)
                pairs.append(pair)
                suite.append(i)
                suite.append(j)
                liste.pop(0)
                liste.pop(1)

            elif len(liste) == 2:
                i = liste[0]
                j = liste[1]
                pair = List_match(i, j)
                pairs.append(pair)
                suite.append(i)
                suite.append(j)
                liste.pop(0)
                liste.pop(0)
                
            else:
                pass
                
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
            
            #print(pairs)
            #print(tirages)
                
        nom_tour = "Round 0"
        begin_time = datetime.datetime.now()
        end_time = datetime.datetime.now()
        tour = Tour(nom_tour, begin_time, end_time)
        #print(nom_tour, begin_time, end_time)
        return  pairs, suite, tirages, tour

    global pairs
    global suite
    pairs, suite, tirages, tour = create_round_1(tri_rangs)
    print(pairs)
    print(suite)
    print(tirages)
    print (tour)

class Play:
    """jouer les rencontres"""
    def __init__(self, pairs, suite):
        self.pairs = pairs
        self.suite = suite
        
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
            #print(jeu)
            #print(alea)
            #print(score)
            pass
        
        return score
    score = edit_resultat()
    print(score)

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
    
    def create_classement_partie(suite, score):
        """creation du classement après le premier tour"""
        noms = []
        scores = []
        for one in suite:
            i = suite.index(one)
            nom = suite[i]
            noms.append(nom)
            #print(nom)
        
        for one in score:
            i = score.index(one)
            point = score[i]
            scores.append(point)
            #print(point)
        
        tri_scores = sorted(range(len(scores)), key=lambda k: scores[k], reverse=True)
        tri_joueurs = list(itemgetter(*tri_scores)(noms))
        #new_classement = Tri(noms, scores)
        #tri_joueurs = [x for _ , x in sorted(zip(scores,noms), reverse = True)]
        #print(tri_joueurs)
        return tri_joueurs
    global tri_joueurs
    tri_joueurs = create_classement_partie(suite, score)
    print(tri_joueurs)
    
    def create_table_joueur(suite, score):
        """creation en memoire d'un tableau du score de chaque joueur"""
        table_joueurs = []
        while len(suite): 
            table_joueur = Table_joueur(suite[0], score[0])
            table_joueurs.append(table_joueur)
            suite = suite[1:]
            score = score[1:]
            #print(suite)
            #print(score)
            #print(table_joueur)
        return table_joueurs
    table_joueurs = create_table_joueur(suite, score)
    print(table_joueurs)

class Other_round:
    """établie les trois derniers tours"""
    def __init__(self):
        pass

    def liste_matchs_effectues(tri_joueurs):
        """incrémente les matchs effectués"""
        matchs_effectues = []
        matchs_effectues.append(tri_joueurs)
        #print(matchs_effectues)
        return matchs_effectues

    matchs_effectues = liste_matchs_effectues(tri_joueurs)
    print(matchs_effectues)

    def create_other_pairs(matchs_effectues):
        """creation des trois derniers tours"""
        pass
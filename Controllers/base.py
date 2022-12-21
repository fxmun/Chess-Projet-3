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
        tirages = []
        while liste:
            if len(liste) == 8:
                i = liste[0]
                j = liste[4]
                pair = List_match(i, j)
                pairs.append(pair)
                liste.pop(0)
                liste.pop(3)
                
            elif len(liste) == 6:
                i = liste[0]
                j = liste[3]
                pair = List_match(i, j)
                pairs.append(pair)
                liste.pop(0)
                liste.pop(2)     

            elif len(liste) == 4:
                i = liste[0]
                j = liste[2]
                pair = List_match(i, j)
                pairs.append(pair)
                liste.pop(0)
                liste.pop(1)

            elif len(liste) == 2:
                i = liste[0]
                j = liste[1]
                pair = List_match(i, j)
                pairs.append(pair)
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
        return  pairs, tirages, tour

    global pairs
    pairs, tirages, tour = create_round_1(tri_rangs)
    print(pairs)
    print(tirages)
    print (tour)

class Play:
    """jouer les rencontres"""
    def __init__(self, pairs, score):
        self.pairs = pairs
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
    
    def create_classement_partie(pairs, score):
        """creation du classement après le premier tour"""
        noms = []
        scores = []
        for pair in pairs:
            i = pairs.index(pair)
            nom = pairs[i]
            noms.append(nom)
            #print(nom)
        
        for un in score:
            i = score.index(un)
            point = score[i]
            scores.append(point)
            #print(point)        
        new_classement = Tri(noms, scores)
        tri_joueurs = [x for _ , x in sorted(zip(str(scores),noms), reverse = True)]
        return new_classement, tri_joueurs
    new_classement, tri_joueurs = create_classement_partie(pairs, score)
    print(tri_joueurs)
    '''
    def create_table_joueur(new_classement, pairs):
        """creation en memoire d'un tableau du score de chaque joueur"""
        noms = new_classement.name
        scores = new_classement.resultat
        print(noms)
        print(scores)
        nom = []
        score = []
        result = []
        for h in scores:
            y = scores.index(h)
            if y == 0:
                i = y
                j = noms[y].joueur_1
                k = scores[i]
                nom.append(j)
                score.append(k)
                j = noms[y].joueur_2
                i += 1
                k = scores[i]
                nom.append(j)
                score.append(k)

            elif y == 1:
                i = y
                j = noms[y].joueur_1
                i += 1
                k = scores[i]
                nom.append(j)
                score.append(k)
                j = noms[y].joueur_2
                i += 1
                k = scores[i]
                nom.append(j)
                score.append(k)

            elif y == 2:
                i = y
                j = noms[y].joueur_1
                i += 2
                k = scores[i]
                nom.append(j)
                score.append(k)
                j = noms[y].joueur_2
                i += 1
                k = scores[i]
                nom.append(j)
                score.append(k)        

            elif y == 3:
                i = y
                j = noms[y].joueur_1
                i += 3
                k = scores[i]
                nom.append(j)
                score.append(k)
                j = noms[y].joueur_2
                i += 1
                k = scores[i]
                nom.append(j)
                score.append(k)

            else:
                break    
   
        tri_joueurs = [x for _ , x in sorted(zip(score,nom), reverse = True)]
        print(nom)
        print(score)
        return tri_joueurs
    
    tri_joueurs = create_table_joueur(new_classement, pairs)
    print(tri_joueurs)'''

    '''def create_table_joueur(new_classement, pairs):
        """creation en memoire d'un tableau du score de chaque joueur"""
        noms = new_classement.name
        scores = new_classement.resultat
        table_joueurs = []
        for unit in range(8):
            #i = range(4).index(unit)
            table_joueur = Table_joueur(noms, scores)
            table_joueurs.append(table_joueur)
            print(noms)
            print(table_joueur)
        return table_joueurs
    table_joueurs = create_table_joueur(new_classement, pairs)
    print(table_joueurs)'''

class Other_round:
    """établie les trois derniers tours"""
    def __init__(self):
        pass

    def liste_matchs_effectues(pairs):
        """incrémente les matchs effectués"""
        matchs_effectues = []
        matchs_effectues.append(pairs)
        #print(matchs_effectues)
        return matchs_effectues

    matchs_effectues = liste_matchs_effectues(pairs)
    print(matchs_effectues)

    def create_other_pairs(matchs_effectues):
        """creation des trois derniers tours"""
        #new_pairs = 
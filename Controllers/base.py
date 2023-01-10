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
from Models.base import Syntese
from Views.creation import Creation


class Initialise:
    """initialisation du tournoi"""
    def __init__(self, round=0):
        """a une vue"""
        self.round = round
        return

    def __str__(self):
        """Used in print."""
        return f"{self.round}"

    def __repr__(self, round):
        """Used in print."""
        return str(self)

    def run(self):
        """debute le tournoi."""
        return

    def edit_tournoi():
        """édition des caractéristiques du tournoi"""
        tournoi = Creation.prompt_create_tournoi(Creation)
        return tournoi
    tournoi = edit_tournoi()
    # print(tournoi)

    def create_tournoi(tournoi):
        """creation d'un tournoi en mémoire"""
        tournoi = Tournoi(tournoi[0], tournoi[1], tournoi[2], tournoi[3], tournoi[4])
        print('caracteristiques du tournoi: ' + str(tournoi))
        return tournoi
    tournoi = create_tournoi(tournoi)

    def edit_joueurs():
        """édition des joueurs par la vue"""
        joueurs = []
        nombre_joueurs = Creation.prompt_create_nombre_joueurs(Creation)
        for one in range(nombre_joueurs):
            joueur = Creation.prompt_create_joueur(Creation)
            joueurs.append(joueur)
        return joueurs, nombre_joueurs
    global joueurs
    global nombre_joueurs
    joueurs, nombre_joueurs = edit_joueurs()
    # print(joueurs)
    # print(nombre_joueurs)

    def create_joueurs(joueurs):
        """création des joueurs en mémoire"""

        for caracterise in joueurs:
            i = joueurs.index(caracterise)
            joueurs[i] = Joueur(caracterise[0], caracterise[1], caracterise[2], caracterise[3], caracterise[4])
        print('caracteristiques des joueurs: ' + str(joueurs))
        return joueurs
    joueurs = create_joueurs(joueurs)

    def classement_initial():
        """restitue les scores totalises par nom"""
        noms = []
        classements = []
        results = []
        for nom in joueurs:
            i = joueurs.index(nom)
            j = joueurs[i].nom
            noms.append(j)
            k = joueurs[i].classement
            classements.append(k)
        results = [x for x in sorted(zip(classements, noms))]
        return results

    results = classement_initial()
    # print("classement initial: "+str(results))

    def create_classements_final(results):
        """création en mémoire du classement pa noms"""
        result = Syntese(results)
        print("classement initial: "+str(result))
        return result

    result = create_classements_final(results)

    def edit_list_joueurs():
        """edition de la liste des joueurs"""
        list_joueur = []
        h = len(joueurs)
        i = 0
        while i <= h-1:
            list_joueur.append(i)
            i += 1
        return list_joueur
    global list_joueur
    list_joueur = edit_list_joueurs()
    # print(list_joueur)

    def create_list_joueur(list_joueur):
        """creation d'une liste de joueurs en mémoire"""
        list_joueur = List_joueur(list_joueur)
        print('liste des joueurs par leurs indices: ' + str(list_joueur))
        return list_joueur
    list_joueur = create_list_joueur(list_joueur)

    def edit_cadence():
        """edition de la cadence des matchs par la vue"""
        cadence = Creation.prompt_create_cadence(Creation)
        return cadence
    cadence = edit_cadence()
    # print(cadence)

    def create_cadence(cadence):
        """creation en mémoire de la cadence"""
        if cadence == '1':
            cadences = Ctrl_temps(True, False, False)
        elif cadence == '2':
            cadences = Ctrl_temps(False, True, False)
        elif cadence == '3':
            cadences = Ctrl_temps(False, False, True)
        else:
            pass
        print('cadence: ' + str(cadences))
        return cadences
    cadences = create_cadence(cadence)


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
        tri_rangs = [x for _, x in sorted(zip(rangs, gamers))]
        # print(tri_rangs)
        return tri_rangs
    global tri_rangs
    tri_rangs = init_classement()
    # print(tri_rangs)

    def create_classement(tri_rangs):
        """création du classement en mémoire"""
        obj_rangs = Classement(tri_rangs)
        print('rangs: ' + str(obj_rangs))
        return obj_rangs
    obj_rangs = create_classement(tri_rangs)


round = Initialise()
# print(round)


class Build:
    """constuit le tournoi"""
    def __init__(self):
        pass

    global tournees
    tournees = []
    global all_pairs
    all_pairs = []

    def create_round(tri_rangs, nombre_joueurs, round):
        liste = tri_rangs
        pairs = []
        suite = []
        tirages = []
        if round.round == 0:
            while range(nombre_joueurs):
                i = liste[0]
                j = int(nombre_joueurs/2)
                k = liste[j]
                pair = List_match(i, k)
                pairs.append(pair)
                all_pairs.append([pair])
                suite.append(i)
                suite.append(k)
                liste.pop(0)
                h = int(j) - 1
                liste.pop(h)
                nombre_joueurs -= 2
                # print(liste)
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
        else:
            while range(nombre_joueurs):
                i = liste[0]
                j = liste[1]
                unit = []
                unit.append(i)
                unit.append(j)
                check = all(item in all_pairs for item in unit)
                print(check)
                if check is True and nombre_joueurs > 2:
                    print(liste)
                    k = liste[2]
                    print("DOUBLON DETECTE !")
                    idx1 = liste.index(i)
                    idx2 = liste.index(j)
                    idx3 = liste.index(k)
                    liste[idx1], liste[idx2], liste[idx3] = liste[idx1], liste[idx3], liste[idx2]
                else:
                    pass

                pair = List_match(i, j)
                pairs.append(pair)
                all_pairs.append([pair])
                suite.append(i)
                suite.append(j)
                liste.pop(0)
                liste.pop(0)
                nombre_joueurs -= 2
                # print(liste)

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

        # print(pairs)
        # print(tirages)

        # print(round)
        nom_tour = "Round " + str(round)
        begin_time = datetime.datetime.now()
        end_time = datetime.datetime.now()
        tour = Tour(nom_tour, begin_time, end_time)
        print('paires: ' + str(pairs))
        print('toutes les paires: ' + str(all_pairs))
        # print('suite de joueurs appaires: ' + str(suite))
        print('tirage au sort des couleurs: ' + str(tirages))
        print('definition du tour: ' + str(tour))
        tournees.append(tour)
        print(tournees)
        return pairs, suite, tirages, tour
    global pairs
    global suite
    pairs, suite, tirages, tour = create_round(tri_rangs, nombre_joueurs, round)


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
            # print(jeu)
            # print(alea)
            # print(score)
        print('score: ' + str(score))
        return score
    score = edit_resultat()

    def create_resultat(pairs, score):
        """creation du resultat en memoire"""
        resultats = []
        for jeu in pairs:
            resultat = Resultat(jeu, score[0], score[1])
            resultats.append(resultat)
            score = score[2:]
        print('resultats: ' + str(resultats))
        return resultats
    resultats = create_resultat(pairs, score)

    def create_classement_partie(suite, score, joueurs):
        """creation du classement après le premier tour"""
        noms = []
        scores = []
        index_noms = []
        print("joueurs: "+str(joueurs))
        for i in joueurs:
            j = joueurs.index(i)
            nom = suite[j]
            noms.append(nom)
            # print(nom)
            k = i.nom.index(nom)
            index_noms.append(k)
            # print(index_noms)

        for x in joueurs:
            y = joueurs.index(x)
            point = score[y]
            scores.append(point)

        for z in scores:
            u = index_noms[0]
            joueurs[u].score += z
            index_noms.pop(0)
            # print(nom)
            # print(point)

        tri_scores = sorted(range(len(scores)), key=lambda k: scores[k], reverse=True)
        tri_joueurs = list(itemgetter(*tri_scores)(noms))
        print('scores: ' + str(scores))
        print('tri_joueurs: ' + str(tri_joueurs))
        return tri_joueurs

    global tri_joueurs
    tri_joueurs = create_classement_partie(suite, score, joueurs)

    def create_table_joueur(suite, score):
        """creation en memoire d'un tableau du score de chaque joueur"""
        table_joueurs = []
        while len(suite):
            table_joueur = Table_joueur(suite[0], score[0])
            table_joueurs.append(table_joueur)
            suite = suite[1:]
            score = score[1:]
            # print(suite)
            # print(score)
            # print(table_joueur)
        print('table_joueurs: ' + str(table_joueurs))
        return table_joueurs
    table_joueurs = create_table_joueur(suite, score)

    def maj_joueurs(tri_joueurs):
        ordre = range(nombre_joueurs)
        maj_ordre = [i for i in sorted(zip(tri_joueurs, ordre))]
        print('classement joueurs tries: ' + str(maj_ordre))
        order = []
        for element in maj_ordre:
            order.append(element[1])
        print('ordre correspondant joueurs tries: ' + str(order))

        for element in order:
            i = order.index(element)
            joueurs[i].classement = element
        print('classement joueurs complet tries: ' + str(joueurs))
        return order, maj_ordre
    maj_ordre, ordre = maj_joueurs(tri_joueurs)


class Other_round:
    """établie les trois derniers tours"""
    def __init__(self):
        pass

    def __str__(self):
        """Used in print."""
        return f"{self}"

    def __repr__(self):
        """Used in print."""
        return str(self)

    def liste_matchs_effectues(tri_joueurs):
        """incrémente les matchs effectués"""
        matchs_effectues = []
        matchs_effectues.append(tri_joueurs)
        # print(matchs_effectues)
        return matchs_effectues

    matchs_effectues = liste_matchs_effectues(tri_joueurs)
    # print('matchs_effectues: ' + str(matchs_effectues))

    def create_other_round(tri_rangs, round):
        """creation des trois derniers tours"""
        rondes = []
        rates = []
        rangs = []
        paires = []
        suites = []
        draws = []
        tours = []
        scores = []
        results = []
        all_tri_joueurs = []
        all_table_joueurs = []
        for i in range(3):
            j = range(3).index(i)
            j += 1
            tourne = Initialise(j)
            rondes.append(tourne)
            cadence = Initialise.edit_cadence()
            cadences = Initialise.create_cadence(cadence)
            rates.append(cadences)
            tri_rangs = Rank.init_classement()
            tri_rangs = tri_rangs[::-1]
            # print(tri_rangs)
            obj_rangs = Rank.create_classement(tri_rangs)
            # print(obj_rangs)
            rangs.append(obj_rangs)
            pairs, suite, tirages, tour = Build.create_round(tri_rangs, nombre_joueurs, tourne)
            # print(pairs)
            paires.append(pairs)
            suites.append(suite)
            draws.append(tirages)
            tours.append(tour)
            score = Play.edit_resultat()
            scores.append(score)
            resultats = Play.create_resultat(pairs, score)
            results.append(resultats)
            tri_joueurs = Play.create_classement_partie(suite, score, joueurs)
            all_tri_joueurs.append(tri_joueurs)
            table_joueurs = Play.create_table_joueur(suite, score)
            all_table_joueurs.append(table_joueurs)
            update_joueurs = Play.maj_joueurs(tri_joueurs)

            # print(tourne)
            # print(cadences)
            # print(pairs)
            # print(suite)
            # print(tirages)
            # print(tour)
            # print(score)
            # print(resultats)
            # print(tri_joueurs)
            # print(table_joueurs)
            # print(update_joueurs)
            # print(result)
            # print(joueurs)

        return rondes, rates, rangs, paires, suites, draws, tours, scores, results, all_tri_joueurs, \
            all_table_joueurs, update_joueurs

    rondes, rates, rangs, paires, suites, draws, tours, scores, results, all_tri_joueurs, all_table_joueurs, \
        update_joueurs = create_other_round(tri_rangs, round)
    # print(rondes)
    # print(rates)
    # print(rangs)
    # print(paires)
    # print(suites)
    # print(draws)
    # print(tours)
    # print(scores)
    # print(results)
    # print(all_tri_joueurs)
    # print(all_table_joueurs)

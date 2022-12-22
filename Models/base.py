class Tournoi:
    """modele de tournoi"""
    def __init__(self, nom, lieu, date_debut, date_fin, description):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.description = description
    
    def __str__(self):
        """Used in print."""
        return f"{self.nom}, {self.lieu}, {self.date_debut}, {self.date_fin}, {self.description}"

    def __repr__(self):
        """Used in print."""
        return str(self)

class Joueur:
    """Joueurs participant au tournoi"""
    def __init__(self, nom, prenom, birth_date, genre, classement):
        self.nom = nom
        self.prenom = prenom
        self.birth_date = birth_date
        self.genre = genre
        self.classement = classement
    
    def __str__(self):
        """Used in print."""
        return f"{self.nom}, {self.prenom}, {self.birth_date}, {self.genre}, {self.classement}"

    def __repr__(self):
        """Used in print."""
        return str(self)

class List_joueur:
    """liste des joueurs sous forme d'indice d'instance de joueur"""
    def __init__(self, list_joueur):
        self.list_joueur = list_joueur
    
    def __str__(self):
        """Used in print."""
        return f"{self.list_joueur}"

    def __repr__(self):
        """Used in print."""
        return str(self)

class Ctrl_temps:
    """bullet: 6mn / 2 joueurs, blitz: 10mn / 2 joueurs, coup rapide: 40mn / 2 joueurs"""
    def __init__(self, bullet = False, blitz = False, coup_rapide = False):
        self.bullet = bullet
        self.blitz = blitz
        self.coup_rapide = coup_rapide
    
    def __str__(self):
        """Used in print."""
        return f"{self.bullet}, {self.blitz}, {self.coup_rapide}"

    def __repr__(self):
        """Used in print."""
        return str(self)

class Classement:
    """classement des joueurs par indice de la liste des joueurs"""
    def __init__(self, rang):
        self.rang = rang

    def __str__(self):
        """Used in print."""
        return f"{self.rang}"

    def __repr__(self):
        """Used in print."""
        return str(self)
      
class List_match:
    """liste des matchs de chaque tour"""
    def __init__(self, joueur_1, joueur_2):
        self.joueur_1 = joueur_1
        self.joueur_2 = joueur_2
        
    def __str__(self):
        """Used in print."""
        return f"{self.joueur_1}, {self.joueur_2}"

    def __repr__(self):
        """Used in print."""
        return str(self)

class Tirage:
    """tirage au sort blanc ou noir"""
    def __init__(self, color_joueur_1, color_joueur_2):
        self.color_joueur_1 = color_joueur_1
        self.color_joueur_2 = color_joueur_2

    def __str__(self):
        """Used in print."""
        return f"{self.color_joueur_1}, {self.color_joueur_2}"

    def __repr__(self):
        """Used in print."""
        return str(self)

class Tour:
    """tours du tournoi"""
    def __init__(self, nom_tour, begin_time, end_time):
        self.begin_time = begin_time
        self.end_time = end_time
        self.nom_tour = nom_tour

    def mark_end(self, end = False):
        pass

    def __str__(self):
        """Used in print."""
        return f"{self.nom_tour}, {self.begin_time}, {self.end_time}"

    def __repr__(self):
        """Used in print."""
        return str(self)

class Resultat:
    """resultat du tour"""
    def __init__(self, partie, pts_joueur_1, pts_joueur_2):
        self.pts_joueur_1 = pts_joueur_1
        self.pts_joueur_2 = pts_joueur_2
        self.partie = partie
    
    def __str__(self):
        """Used in print."""
        return f"{self.partie}, {self.pts_joueur_1}, {self.pts_joueur_2}"

    def __repr__(self):
        """Used in print."""
        return str(self)

class Table_joueur:
    """score par joueur"""
    def __init__(self, name, score):
        self.name = name
        self.score = score
 
    def __str__(self):
        """Used in print."""
        return f"{self.name}, {self.score}"

    def __repr__(self):
        """Used in print."""
        return str(self)
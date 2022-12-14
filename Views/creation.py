"""vue de base"""

class Creation:
    """cré le tournoi."""

    def __init__(self):
        """Initialise la vue"""
        return

    def prompt_create_tournoi(self):
        """demande la création du tournoi"""
        self.nom = input("entrez le nom du tournoi : ")
        if self.nom == '':
            print('champ obligatoire')
            self.prompt_create_tournoi(self)
            return
        
        self.lieu = input("entrez le lieu du tournoi : ")
        if self.lieu == '':
            print('champ obligatoire')
            self.prompt_create_tournoi(self)
            return
        
        self.date_debut = input("entrez la date de debut du tournoi : ")
        if self.date_debut == '':
            print('champ obligatoire')
            self.prompt_create_tournoi(self)
            return
        
        self.date_fin = input("entrez la date de fin du tournoi : ")
        if self.date_fin == '':
            print('champ obligatoire')
            self.prompt_create_tournoi(self)
            return
        
        self.description = input("entrez la description du tournoi : ")
        if self.description == '':
            print('champ obligatoire')
            self.prompt_create_tournoi(self)
            return
        
        tournoi = [self.nom, self.lieu, self.date_debut, self.date_fin, self.description]
        
        return tournoi

    def prompt_create_nombre_joueurs(self):
        """définition du nombre de joueurs"""
        try:
            self.nombre = int(input("entrez un nombre paire superieur ou egal a 8 "))
            if not int(self.nombre) or int(self.nombre) % 2 != 0 or int(self.nombre) < 8:
                print("entrez un nombre paire supérieur ou égal a 8: ")
                self.prompt_create_nombre_joueurs(self)
        except:
            print("ERREUR ! : entrez un nombre paire superieur ou egal a 8")
            self.prompt_create_nombre_joueurs(self)
        return self.nombre

    def prompt_create_joueur(self):
        """demande la création des joueurs"""
        self.nom = input("entrez le nom du joueur : ")
        if self.nom == '':
            print('champ obligatoire')
            self.prompt_create_tournoi(self)
            return self.nom

        self.prenom = input("entrez le prenom du joueur : ")
        if self.prenom == '':
            print('champ obligatoire')
            self.prompt_create_tournoi(self)
            return self.prenom

        self.birth_date = input("entrez la date de naissance du joueur : ")
        if self.birth_date == '':
            print('champ obligatoire')
            self.prompt_create_tournoi(self)
            return self.birth_date

        self.genre = input("entrez le genre du joueur : ")
        if self.genre == '':
            print('champ obligatoire')
            self.prompt_create_tournoi(self)
            return self.gender
        
        self.classement = input("entrez le classement du joueur : ")
        if self.classement == '':
            print('champ obligatoire')
            self.prompt_create_tournoi(self)
            return self.classement

        #print(self.nom, self.prenom, self.birth_date, self.genre, self.classement)
        joueur =[self.nom, self.prenom, self.birth_date, self.genre, self.classement]
        #print(joueur)
        return joueur

    def prompt_create_cadence(self):
        """choix de la cadence des matchs"""
        self.choix = input("Pour bullet tapez 1 Pour blitz tapez 2 Pour coup rapide tapez 3 : ")
        #print(self.choix)
        if self.choix == "1" or self.choix == "2" or self.choix == "3":
            return self.choix
        else:
            print("Vous devez taper 1, 2 ou 3 ! : ")    
            self.prompt_create_cadence()

        self.prompt_create_cadence()
        return choix

    def prompt_edit_result():
        """edition du resultat d'un match"""
        score = []
        return score
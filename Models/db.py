

class Db:
    """base de donnée des joueurs"""
    def __init__(self, name, surname, birth_date, gender, rank):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.gender = gender
        self.rank = rank
        pass


        
"""point d'entrée"""

from Models.base import Tournoi
from Controllers.base import Initialise
from Views.creation  import Creation
import datetime

def main():
    view = Creation()
    start = Initialise(view)
    start.run()
    return

if __name__ == "__main__":
    main()
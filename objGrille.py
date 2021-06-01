# objGrille.py

from objCase import*


class Grille:
    """L'objet Grille, contenant tout un tas d'objet Case, permet de les gérer séparemment"""

    def __init__(self, grille: list, fen, taille: int):
        """
        :param grille: une grille(list)
        :param fen: la fenêtre maître(Tk())
        :param taille: la taille du canvas(int)
        """
        print("Initialisation du canvas...")
        self.grille = grille
        self.fen = fen
        self.canvas = Canvas(fen, height=taille, width=taille, bg='white')
        self.taille = taille
        self.listeCases = []

        self.canvas.pack()

        self.initialiseCaseGrille()
        print("Canvas initialisé!")

    def initialiseCaseGrille(self):
        """Permet d'initaliser toutes les cases du canvas"""

        print("Initialisation des cases...")
        tailleCase = int(self.taille/len(self.grille))
        for x in range(0, self.taille, tailleCase):
            for y in range(0, self.taille, tailleCase):
                case = Case(self.canvas, x, y, 'empty', tailleCase)
                pos = (int(x / tailleCase), int(y / tailleCase))
                self.listeCases.append((pos, case))
        print("Cases initialisées!")
        print(self.listeCases)

    def updateGrid(self):
        """Met le canvas à jour par rapport à la grille"""
        for case in self.listeCases:
            x = case[0][0]
            y = case[0][1]
            case[1].state = self.grille[x][y]
            case[1].affiche()

    def changeState(self, pos: tuple, state: str):
        """Change l'état d'une case donnée

        :param pos: la position de la case à changer
        :param state: le nouvel etat
        """
        self.grille[pos[0]][pos[1]] = state
        self.updateGrid()

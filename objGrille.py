# objGrille.py

from objCase import *
from tkinter import ttk


class Grille:
    """L'objet Grille, contenant tout un tas d'objet Case, permet de les gérer séparemment"""

    def __init__(self, grille: list, fen, taille: int):
        """Initialisation de la grille
        :param grille: une grille(list)
        :param fen: la fenêtre maître(Tk())
        :param taille: la taille du canvas(int)
        """
        print("Initialisation du canvas...")
        self.grille = grille
        self.fen = fen
        self.canvas = Canvas(fen, height=taille, width=taille, bg='white')
        self.taille = taille
        self.listePos = []
        self.cases = []
        self.tailleCase = int(self.taille / len(self.grille))

        self.canvas.pack()

        self.initialiseCaseGrille()
        print("Canvas initialisé!")

    def initialiseCaseGrille(self):
        """Permet d'initaliser toutes les cases du canvas"""
        print("Initialisation des cases...")
        for x in range(len(self.grille)):
            for y in range(len(self.grille)):
                case = Case(self.canvas, x * self.tailleCase, y * self.tailleCase, 'empty', self.tailleCase)
                pos = (x, y)
                self.listePos.append(pos)
                self.cases.append(case)
                case.pos = pos
        print("Cases initialisées!")
        print(self.listePos)

    def updateGrid(self):
        """Met le canvas à jour par rapport à la grille"""
        for case in self.cases:
            x = case.pos[0]
            y = case.pos[1]
            case.state = self.grille[x][y]
            case.affiche()

    def changeState(self, pos: tuple, state: str):
        """Change l'état d'une case donnée

        :param pos: la position de la case à changer
        :param state: le nouvel etat
        """
        self.grille[pos[0]][pos[1]] = state
        self.updateGrid()

    def adjacentes(self, pos: tuple, diago: bool):
        """Retourne les cases adjacentes à une case spécifique
        :param pos: la position d'une case
        :param diago: Détermine si oui ou non les cases en diagonales sont prises en compte
        :return: liste des cases adjacentes
        """
        case = self.pos2Case(pos)
        return case.donneAdjacentes(self, diago)

    def pos2Case(self, pos: tuple):
        """Fait le lien entre la position et l'objet case associé
        :param pos: position d'une case
        :return: une case
        """
        for i in range(len(self.listePos)):
            if pos == self.listePos[i]:
                return self.cases[i]
        return False

    def returnCoord(self, event):
        x = int(event.x)
        y = int(event.y)
        return x, y

    def getClickedCase(self, event):
        coord = self.returnCoord(event)
        x = coord[0]
        y = coord[1]
        for case in self.cases:
            xCase = (case.pos[0] * self.tailleCase) + self.tailleCase / 2
            yCase = (case.pos[1] * self.tailleCase) + self.tailleCase / 2
            if distance((xCase, yCase), (x, y)) <= self.tailleCase / 2:
                print(case.pos)
                return case

    def cycleState(self, event):
        case = self.getClickedCase(event)
        case.cycleState()
        print(case.state)
        case.affiche()

    def clicDroit(self):
        """Fonctions à exécuter en cas de clic droit"""
        self.canvas.bind("<Button-1>", self.cycleState)

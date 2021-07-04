# objGrille.py

from objCase import *


class Grille:
    """L'objet Grille, contenant tout un tas d'objet Case, permet de les gérer séparemment"""

    def __init__(self, nbCases: int, fen, taille: int):
        """Initialisation de la grille
        :param nbCases: Le nombre de case sur une rangée
        :param fen: la fenêtre maître(Tk())
        :param taille: la taille du canvas(int)
        """
        print("Initialisation du canvas...")
        self.nbCases = nbCases
        self.fen = fen
        self.canvas = Canvas(fen, height=taille, width=taille, bg='white')
        self.taille = taille
        self.listePos = []
        self.cases = []
        self.tailleCase = int(self.taille / self.nbCases)
        self.canvas.pack()

        self.initialiseCaseGrille()
        print("Canvas initialisé!")

    def initialiseCaseGrille(self):
        """Permet d'initaliser toutes les cases du canvas"""
        print("Initialisation des cases...")
        for x in range(self.nbCases):
            for y in range(self.nbCases):
                case = Case(self.canvas, x * self.tailleCase, y * self.tailleCase, 'empty', self.tailleCase)
                pos = (x, y)
                self.cases.append(case)
                self.listePos.append(pos)
                case.pos = pos
        print("Cases initialisées!")
        print(self.listePos)

    def pos2Case(self, pos: tuple):
        """Fait le lien entre la position et l'objet case associé
        :param pos: position d'une case
        :return: une case
        """
        for i in range(len(self.listePos)):
            if pos == self.listePos[i]:
                return self.cases[i]
        return False

    def getClickedCase(self, event):
        """
        :param event: oui
        :return: la case cliquée
        """
        coord = returnCoord(event)
        for case in self.cases:
            if entreCoord(coord, case.pos0, vecAdd(case.pos0, (self.tailleCase, self.tailleCase))):
                return case

    def cycleState(self, event):
        """Change l'état dans un sens prédéfini
        :param event: oui
        """
        case = self.getClickedCase(event)
        case.cycleState()

    def clicDroit(self):
        """Fonctions à exécuter en cas de clic droit"""
        self.canvas.bind("<Button-1>", self.cycleState)

    def donneAdjacentes(self, case, diago):
        listeAdja = []

        def ajouteCase(x, y):
            """Fonction ajoutant une case à listeAdja"""
            aAjouter = self.pos2Case(vecAdd(case.pos, (x, y)))
            if aAjouter is not None:
                listeAdja.append(aAjouter)

        ajouteCase(1, 0)
        ajouteCase(-1, 0)
        ajouteCase(0, 1)
        ajouteCase(0, -1)
        if diago:
            ajouteCase(1, 1)
            ajouteCase(-1, -1)
            ajouteCase(1, -1)
            ajouteCase(-1, 1)
        return listeAdja

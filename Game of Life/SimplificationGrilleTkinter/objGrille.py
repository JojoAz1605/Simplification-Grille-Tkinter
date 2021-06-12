# objGrille.py

from objCase import *
from commonFunc import*


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
        case = self.getClickedCase(event)
        case.cycleState()
        case.affiche()

    def clicDroit(self):
        """Fonctions à exécuter en cas de clic droit"""
        self.canvas.bind("<Button-1>", self.jeuDeLaVie)

    def tour(self, *args):
        print("Un tour est lancé!")
        listeChangements = []
        for case in self.cases:
            casesAdja = self.donneAdjacentes(case, True)
            nbAdjaPleines = combienState(casesAdja, 'full')
            if case.state == 'empty' and nbAdjaPleines == 3:
                listeChangements.append((case, 'full'))
            elif case.state == 'full' and (nbAdjaPleines < 2 or nbAdjaPleines > 3):
                listeChangements.append((case, 'empty'))
        for changement in listeChangements:
            case = changement[0]
            state = changement[1]
            changeState(case, state)

    def donneAdjacentes(self, case, diago):
        listeAdja = []

        def ajouteCase(x, y):
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

    def jeuDeLaVie(self, *args):
        self.tour()
        self.canvas.after(100, self.jeuDeLaVie)

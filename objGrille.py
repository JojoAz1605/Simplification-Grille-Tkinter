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
        self.nbCases = nbCases  # le nombre de case au sur une ligne
        self.fen = fen  # la fenêtre
        self.canvas = Canvas(fen, height=taille, width=taille, bg='white')  # le canvas
        self.taille = taille  # la taille du canvas
        self.listePos = []  # la liste des positions des cases
        self.cases = []  # la liste des cases
        self.tailleCase = int(self.taille / self.nbCases)  # la taille d'une case
        self.canvas.pack()  # pack le canvas

        self.initialiseCaseGrille()  # initialise les cases
        print("Canvas initialisé!")

    def initialiseCaseGrille(self):
        """Permet d'initaliser toutes les cases du canvas"""
        print("Initialisation des cases...")
        for x in range(self.nbCases):  # parcours en x
            for y in range(self.nbCases):  # parcours en y
                # initialise les cases
                case = Case(self.canvas, x * self.tailleCase, y * self.tailleCase, 'empty', self.tailleCase)
                pos = (x, y)  # enregistre la position en tuple x, y
                self.cases.append(case)  # ajoute l'objet case
                self.listePos.append(pos)  # ajoute la position à la liste des positions
                case.pos = pos  # sauvegarde la position de la case dans la case
            self.updateAdjacentes()  # calcule les cases ajacentes
        print("Cases initialisées!")
        print(self.listePos)

    def pos2Case(self, pos: tuple):
        """Fait le lien entre la position et l'objet case associé
        :param pos: position d'une case
        :return: une case
        """
        for i in range(len(self.listePos)):  # parcours les cases
            if pos == self.listePos[i]:  # si la position est celle recherchée
                return self.cases[i]  # la retourne
        return False  # sinon retourne faux

    def getClickedCase(self, event):
        """
        :param event: le clic(en gros)
        :return: la case cliquée
        """
        coord = returnCoord(event)  # donne les coordonnées du clic
        for case in self.cases:  # parcours les cases de la grille
            # si la case est dans l'intervalle
            if entreCoord(coord, case.pos0, vecAdd(case.pos0, (self.tailleCase, self.tailleCase))):
                return case # la retourne

    def cycleState(self, event):
        """Change l'état dans un sens prédéfini
        :param event: oui
        """
        case = self.getClickedCase(event)  # prend la case cliquée
        case.cycleState()  # change l'état de la case

    def clicDroit(self):
        """Fonctions à exécuter en cas de clic droit"""
        self.canvas.bind("<Button-1>", self.cycleState)  # une fonction

    def updateAdjacentes(self):
        """Update la liste des cases adjacentes de toutes les cases
        """
        for case in self.cases:  # parcours les cases
            case.casesAdjacentes = self.donneAdjacentes(case, True)  # calcule les cases adjacentes

    def donneAdjacentes(self, case, diago):
        """Renvoie les cases adjacentes d'une case en particulier
        :param case: une case(l'objet)
        :param diago: détermine si oui ou non les cases en diagonales seront prises en compte
        :return: la liste des cases adjacentes
        """
        listeAdja = []  # liste des cases adjacentes

        def ajouteCase(x, y):
            """Fonction ajoutant une case à listeAdja"""
            aAjouter = self.pos2Case(vecAdd(case.pos, (x, y)))  # case à ajouter
            if aAjouter is not None:  # si la case n'est pas vide
                listeAdja.append(aAjouter)  # l'ajoute

        # ajoute les cases adjacentes
        ajouteCase(1, 0)
        ajouteCase(-1, 0)
        ajouteCase(0, 1)
        ajouteCase(0, -1)
        if diago:  # ajoute celles en diagonale
            ajouteCase(1, 1)
            ajouteCase(-1, -1)
            ajouteCase(1, -1)
            ajouteCase(-1, 1)
        return listeAdja  # retourne la liste des cases

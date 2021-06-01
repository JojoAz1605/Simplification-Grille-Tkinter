# objCase.py

from tkinter import *
from commonFunc import*

STATES = {
    'empty': 'white',
    'full': 'black'
}


class Case:
    def __init__(self, canvas: Canvas, posX0: int, posY0: int, state: str, taille: int):
        """
        :param canvas: le canvas sur lequel la case sera affichée
        :param posX0: position en x initiale
        :param posY0: position en y initiale
        :param state: l'état de la case(voir STATES)
        :param taille: la taille de la case
        """
        self.grille = canvas
        self.posX = posX0
        self.posY = posY0
        self.state = state
        self.taille = taille
        self.pos = (-1, -1)

        self.affiche()

    def affiche(self):
        """Affiche la case"""
        global STATES
        self.grille.create_rectangle(self.posX, self.posY, self.posX + self.taille, self.posY + self.taille, fill=STATES[self.state])

    def donneAdjacentes(self, grille):
        """Renvoie une liste des cases adjacentes
        :param grille: la grille sur laquelle évolue la case
        :return: une liste des cases se situant autour de la case
        """
        listeAdja = []
        for case in grille.cases:
            if distance(self, case) == 1:
                listeAdja.append(case)
        return listeAdja

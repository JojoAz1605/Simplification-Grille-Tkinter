# objCase.py

from tkinter import *

STATES = {
    'empty': 'white',
    'full': 'black'
}


class Case:
    def __init__(self, canvas: Canvas, posX: int, posY: int, state: str, taille: int):
        """
        :param canvas: le canvas sur lequel la case sera affichée
        :param posX: bruh
        :param posY: bruh
        :param state: l'état de la case(voir STATES)
        :param taille: la taille de la case
        """
        self.grille = canvas
        self.posX = posX
        self.posY = posY
        self.state = state
        self.taille = taille

        self.affiche()

    def affiche(self):
        """Affiche la case"""
        global STATES
        self.grille.create_rectangle(self.posX, self.posY, self.posX + self.taille, self.posY + self.taille, fill=STATES[self.state])

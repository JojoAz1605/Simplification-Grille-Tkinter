# objCase.py

from tkinter import *
from commonFunc import *

STATES = {
    'empty': 'white',
    'full': 'black',
    'dangerous': 'red'
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
        self.pos0 = (self.posX, self.posY)
        self.state = state
        self.taille = taille
        self.listOfStates = makeListOfState(STATES)
        self.pos = (-1, -1)
        self.casesAdjacentes = []

        self.affiche()

    def affiche(self):
        """Affiche la case"""
        global STATES
        # créé le rectangle représentant la case
        self.grille.create_rectangle(self.posX, self.posY, self.posX + self.taille, self.posY + self.taille, fill=STATES[self.state])

    def cycleState(self):
        """Change l'état dans un sens prédéfini"""
        oldStateIndex = indexOf(self.listOfStates, self.state)  # index de l'ancien état
        if oldStateIndex + 1 < len(self.listOfStates):  # si l'état + 1 ne dépasse pas le nombre d'état possibles
            self.state = self.listOfStates[oldStateIndex + 1]  # prend l'état suivant
        else:
            self.state = self.listOfStates[0]  # sinon prend le premier état de la liste
        self.affiche()  # affiche la case

# objCase.py

from tkinter import *
from commonFunc import *

STATES = {
    'empty': 'white',
    'full': 'black',
    'dangerous': 'red',
    'player': 'yellow'
}

ROTATION = {
    'none': 0,
    'haut': 1,
    'bas': -1,
    'droite': 2,
    'gauche': -2
}

class Case:
    def __init__(self, canvas: Canvas, posX0: int, posY0: int, state: str, taille: int, rotation: str, isFourmi=False):
        """
        :param canvas: le canvas sur lequel la case sera affichée
        :param posX0: position en x initiale
        :param posY0: position en y initiale
        :param state: l'état de la case(voir STATES)
        :param taille: la taille de la case
        :param rotation: la direction de la case, dans quel sens elle est tournée
        """
        self.grille = canvas
        self.posX = posX0
        self.posY = posY0
        self.pos0 = (self.posX, self.posY)
        self.state = state
        self.taille = taille
        self.listOfStates = makeListOfState(STATES)
        self.pos = (self.posX, self.posY)
        self.rotation = ROTATION[rotation]
        self.isFourmi = isFourmi

        self.affiche()

    def affiche(self):
        """Affiche la case"""
        global STATES
        self.posX = self.pos[0]
        self.posY = self.pos[1]
        self.grille.create_rectangle(self.posX, self.posY, self.posX + self.taille, self.posY + self.taille, fill=STATES[self.state])

    def cycleState(self):
        """Change l'état dans un sens prédéfini"""
        oldStateIndex = indexOf(self.listOfStates, self.state)
        if oldStateIndex + 1 < len(self.listOfStates):
            self.state = self.listOfStates[oldStateIndex + 1]
        else:
            self.state = self.listOfStates[0]
        self.affiche()

    def changeRotation(self, rotation: str):
        self.rotation = ROTATION[rotation]
        self.affiche()

    def avance(self):
        if self.rotation == 0 or not self.isFourmi:
            return False
        elif self.rotation == 1:
            self.pos = vecAdd(self.pos, (0, -self.taille))
        elif self.rotation == -1:
            self.pos = vecAdd(self.pos, (0, self.taille))
        elif self.rotation == 2:
            self.pos = vecAdd(self.pos, (self.taille, 0))
        elif self.rotation == -1:
            self.pos = vecAdd(self.pos, (-self.taille, 0))
        self.affiche()

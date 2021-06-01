# objCase.py

from tkinter import *

STATES = {
    'empty': 'white',
    'full': 'black'
}


class Case:
    def __init__(self, canvas, posX, posY, state, taille):
        self.grille = canvas
        self.posX = posX
        self.posY = posY
        self.state = state
        self.taille = taille

        self.affiche()

    def affiche(self):
        global STATES
        self.grille.create_rectangle(self.posX, self.posY, self.posX + self.taille, self.posY + self.taille, fill=STATES[self.state])
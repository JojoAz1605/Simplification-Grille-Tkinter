# objGrille.py

from tkinter import*
from objCase import*


class Grille:
    def __init__(self, grille, fen, taille):
        print("Initialisation du canvas")
        self.grille = grille
        self.fen = fen
        self.canvas = Canvas(fen, height=taille, width=taille, bg='white')
        self.taille = taille

        self.canvas.pack()

        self.dessine()
        print("Canvas initialisée!")

    def dessine(self):
        tailleCase = int(self.taille/len(self.grille))
        for x in range(0, self.taille, tailleCase):
            for y in range(0, self.taille, tailleCase):
                Case(self.canvas, x, y, 'empty', tailleCase)

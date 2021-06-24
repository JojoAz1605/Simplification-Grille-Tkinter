# fourmiDeLangton.py

from objGrille import*

NB_CASES = 20
TAILLE_CANVAS = 500

fenMain = Tk()  # création de la fenêtre

unCanvas = Grille(NB_CASES, fenMain, TAILLE_CANVAS)  # création du canvas en instanciant un objet Grille
unCanvas.clicDroit()

fenMain.mainloop()  # lance la fenêtre

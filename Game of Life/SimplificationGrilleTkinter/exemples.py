# exemples.py

from objGrille import*
from commonFunc import*

NB_CASES = 20
TAILLE_CANVAS = 500

laGrille = creeGrille(NB_CASES, 'empty')  # création de la grille

fenMain = Tk()  # création de la fenêtre

unCanvas = Grille(laGrille, fenMain, TAILLE_CANVAS)  # création du canvas en instanciant un objet Grille
unCanvas.changeState((10, 10), 'full')  # change la case (10, 10), et la remplie
unCanvas.clicDroit()


for caseAdja in unCanvas.adjacentes((10, 10), True):
    print(caseAdja.pos, caseAdja.state)

fenMain.mainloop()  # lance la fenêtre

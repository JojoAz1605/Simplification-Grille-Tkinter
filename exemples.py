# exemples.py

from objGrille import*
from commonFunc import*

NB_CASES = 20
TAILLE_CANVAS = 500

fenMain = Tk()  # création de la fenêtre

unCanvas = Grille(NB_CASES, fenMain, TAILLE_CANVAS)  # création du canvas en instanciant un objet Grille
changeState(unCanvas.pos2Case((10, 10)), 'full')  # change la case (10, 10), et la remplie
unCanvas.clicDroit()

for caseAdja in unCanvas.donneAdjacentes(unCanvas.pos2Case((10, 10)), True):
    print(caseAdja.pos, caseAdja.state, end=' | ')

fenMain.mainloop()  # lance la fenêtre

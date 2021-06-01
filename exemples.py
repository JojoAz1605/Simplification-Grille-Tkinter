# exemples.py

from objGrille import*
from commonFunc import*

TAILLE_CASE = 20
TAILLE_CANVAS = 500

verifTailles(TAILLE_CASE, TAILLE_CANVAS)  # vérifie si les tailles sont bonnes

laGrille = creeGrille(TAILLE_CASE, 'empty')  # création de la grille

fenMain = Tk()  # création de la fenêtre

unCanvas = Grille(laGrille, fenMain, TAILLE_CANVAS)  # création du canvas en instanciant un objet Grille
unCanvas.changeState((10, 10), 'full')  # change la case (10, 10), et la remplie

for caseAdja in unCanvas.adjacentes((9, 10)):
    print(caseAdja.pos, caseAdja.state)

fenMain.mainloop()  # lance la fenêtre

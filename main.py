# main.py

from objGrille import*
from commonFunc import*

TAILLE_CASE = 20
TAILLE_CANVAS = 500

if TAILLE_CANVAS % TAILLE_CASE != 0:
    print("La taille des cases n'est pas un diviseur de la taille du canvas...\nVous auriez pu prendre:")
    for i in range(1, TAILLE_CANVAS):
        if TAILLE_CANVAS % i == 0:
            print(i, end=", ")
    exit()

laGrille = creeGrille(TAILLE_CASE, 'empty')  # création de la grille

fenMain = Tk()  # création de la fenêtre

unCanvas = Grille(laGrille, fenMain, TAILLE_CANVAS)  # création du canvas en instanciant un objet Grille
unCanvas.changeState((10, 10), 'full')  # change la case (10, 10), et la remplie
print(unCanvas.grille[10][10])

fenMain.mainloop()  # lance la fenêtre

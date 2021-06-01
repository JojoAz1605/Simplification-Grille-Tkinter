# main.py

from objGrille import*
from commonFunc import*

tailleCase = 20
tailleCanvas = 500

if tailleCanvas % tailleCase != 0:
    print("La taille des cases n'est pas un diviseur de la taille du canvas...\nVous auriez pu prendre:")
    for i in range(1, tailleCanvas):
        if tailleCanvas % i == 0:
            print(i, end=", ")
    exit()

laGrille = creeGrille(tailleCase, 'empty')

fenMain = Tk()

unCanvas = Grille(laGrille, fenMain, tailleCanvas)

fenMain.mainloop()

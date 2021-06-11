# GameOfLifeMain.py

from objGrille import*

NB_CASES = 10
TAILLE_CANVAS = 500

laGrille = creeGrille(NB_CASES, 'empty')

fenGameOfLifeMain = Tk()
leCanvas = Grille(laGrille, fenGameOfLifeMain, TAILLE_CANVAS)

leCanvas.changeState((1, 2), 'full')
leCanvas.changeState((3, 1), 'full')
leCanvas.changeState((3, 2), 'full')
leCanvas.changeState((3, 3), 'full')
leCanvas.changeState((2, 3), 'full')

leCanvas.clicDroit()

fenGameOfLifeMain.mainloop()

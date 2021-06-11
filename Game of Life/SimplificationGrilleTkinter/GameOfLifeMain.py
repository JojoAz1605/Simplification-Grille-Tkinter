# GameOfLifeMain.py

from objGrille import*

NB_CASES = 20
TAILLE_CANVAS = 500

laGrille = creeGrille(NB_CASES, 'empty')

fenGameOfLifeMain = Tk()
leCanvas = Grille(laGrille, fenGameOfLifeMain, TAILLE_CANVAS)

leCanvas.changeState((10, 10), 'full')
leCanvas.changeState((11, 10), 'full')
leCanvas.changeState((12, 10), 'full')


leCanvas.clicDroit()

fenGameOfLifeMain.mainloop()

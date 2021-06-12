# GameOfLifeMain.py

from objGrille import*

NB_CASES = 20
TAILLE_CANVAS = 500

laGrille = creeGrille(NB_CASES, 'empty')

fenGameOfLifeMain = Tk()
leCanvas = Grille(laGrille, fenGameOfLifeMain, TAILLE_CANVAS)

changeState(leCanvas.pos2Case((1, 2)), 'full')
changeState(leCanvas.pos2Case((3, 1)), 'full')
changeState(leCanvas.pos2Case((3, 2)), 'full')
changeState(leCanvas.pos2Case((3, 3)), 'full')
changeState(leCanvas.pos2Case((2, 3)), 'full')

leCanvas.clicDroit()

fenGameOfLifeMain.mainloop()

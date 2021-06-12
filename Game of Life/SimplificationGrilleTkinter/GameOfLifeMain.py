# GameOfLifeMain.py

from objGrille import*
from random import randint

NB_CASES = 15
TAILLE_CANVAS = 500

laGrille = creeGrille(NB_CASES, 'empty')

fenGameOfLifeMain = Tk()
leCanvas = Grille(laGrille, fenGameOfLifeMain, TAILLE_CANVAS)

# changeState(leCanvas.pos2Case((1, 2)), 'full')
# changeState(leCanvas.pos2Case((3, 1)), 'full')
# changeState(leCanvas.pos2Case((3, 2)), 'full')
# changeState(leCanvas.pos2Case((3, 3)), 'full')
# changeState(leCanvas.pos2Case((2, 3)), 'full')

for i in range(randint(0, NB_CASES**2)):
    x = randint(3, NB_CASES-4)
    y = randint(3, NB_CASES-4)

    changeState(leCanvas.pos2Case((x, y)), 'full')

leCanvas.clicDroit()

fenGameOfLifeMain.mainloop()

# commonFunc.py

def creeGrille(taille, state):
    grille = [state]*taille
    for i in range(taille):
        grille[i] = [state]*taille
    return grille

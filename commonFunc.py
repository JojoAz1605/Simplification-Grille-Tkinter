# commonFunc.py

def creeGrille(taille: int, state: str):
    """Créé une grille d'une taille donnée, avec un état donné
    :param taille: la taille de la grille
    :param state: l'état des cases(voir STATES)
    :return: la grille
    """
    grille = [state]*taille
    for i in range(taille):
        grille[i] = [state]*taille
    return grille

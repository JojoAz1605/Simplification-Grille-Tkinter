# commonFunc.py

from math import sqrt


def creeGrille(taille: int, state: str):
    """Créé une grille d'une taille donnée, avec un état donné et la renvoie
    :param taille: la taille de la grille
    :param state: l'état des cases(voir STATES)
    :return: la grille
    """
    grille = [state] * taille
    for i in range(taille):
        grille[i] = [state] * taille
    return grille


def distance(case1, case2):
    """
    :param case1: une Case
    :param case2: une Case
    :return: la distance entre les deux cases
    """
    x1 = case1.pos[0]
    y1 = case1.pos[1]
    x2 = case2.pos[0]
    y2 = case2.pos[1]

    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

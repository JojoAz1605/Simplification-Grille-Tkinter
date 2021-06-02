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


def distanceCases(case1, case2):
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


def distance(pos1, pos2):
    x1 = pos1[0]
    y1 = pos1[1]
    x2 = pos2[0]
    y2 = pos2[1]

    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def indexOf(liste: list, val):
    """retourne l'index d'un élement dans une liste, renvoie False si non présent
    :param liste: une liste de trucs
    :param val: une valeur à rechercher dans la liste
    :return: l'index de la valeur
    """
    for i in range(len(liste)):
        if liste[i] == val:
            return i
    return False

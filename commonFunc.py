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


def vecDiff(vec1: tuple, vec2: tuple):
    """Fait la différence entre deux vecteurs
    :param vec1: Un premier vecteur
    :param vec2: Un deuxième vecteur
    :return: la différence entre les deux
    """
    return vec1[0] - vec2[0], vec1[1] - vec2[1]


def vecAdd(vec1: tuple, vec2: tuple):
    """Fait la somme de deux vecteurs
        :param vec1: Un premier vecteur
        :param vec2: Un deuxième vecteur
        :return: la différence entre les deux
        """
    return vec1[0] + vec2[0], vec1[1] + vec2[1]


def entre(x: int, val1: int, val2: int):
    """Retourne si oui ou non, un nombre x est compris entre val1 et val2, les deux sont inclus
    :param x: Un nombre
    :param val1: Plus petit nombre
    :param val2: plus grand nombre
    :return: Si oui ou non x est compris dans l'intervalle
    """
    if val2 > val1:
        return False
    else:
        return val1 <= x <= val2


def entreCoord(coord: tuple, val1Coord: tuple, val2Coord: tuple):
    """Retourne si oui ou non des coordonnées coord se trouvent dans un espace carré à partir de valCoord
    :param coord: les coordonnées d'un point
    :param val1Coord: les coordonnées d'un premier point
    :param val2Coord: les coordonnées d'un deuxième point
    :return: Si oui ou non un point se trouve entre les deux coordonnées
    """
    x = coord[0]
    y = coord[1]
    xVal1 = val1Coord[0]
    yVal1 = val1Coord[1]
    xVal2 = val2Coord[0]
    yval2 = val2Coord[1]
    return entre(x, xVal1, xVal2) and entre(y, yVal1, yval2)


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

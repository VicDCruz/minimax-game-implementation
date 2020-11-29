"""
Archivo para crear el algoritmo MinMax para automatizar un juego
"""
from Gameboard import Gameboard
from Tictactoe import *


def getMoves(chip, movements):
    """
    TODO: Generar todos los movimientos posibles dado una ficha
    """
    pass


def getChildren(snapshot, isPlayer, movements):
    """
    Obtener todos los movimientos posibles dado un snapshot
    """
    output = []
    for i in range(snapshot.totalChips):
        chip = snapshot.getChip(isPlayer, i)
        for move in getMoves(chip, movements):
            if isPlayer:
                tmp = Gameboard(snapshot.width, snapshot.height,
                                snapshot.setChip(move), snapshot.chips2)
            else:
                tmp = Gameboard(snapshot.width, snapshot.height,
                                snapshot.chips1, snapshot.setChip(move))
            output.append(tmp)
    return output


def minimax(snapshot, depth, isMaximizing, checkScore, movements):
    """
    Implementación básica de Minimax que genera un árbol de decisión
    Un snapshot implica una fotografía del tablero, con sus fichas actuales\n
    Obtenido de https://www.javatpoint.com/mini-max-algorithm-in-ai
    """
    if depth == 0:
        return checkScore(snapshot, isMaximizing)
    if isMaximizing:
        maxScore = float('-inf')
        for child in getChildren(snapshot, True, movements):
            score = minimax(child, depth - 1, False, score, movements)
            maxScore = max(score, maxScore)
        return maxScore
    else:
        minScore = float('inf')
        for child in getChildren(snapshot, False, movements):
            score = minimax(child, depth - 1, True, score, movements)
            minScore = min(score, minScore)
        return minScore


if __name__ == "__main__":
    s = Score()
    minimax(None, 3, True, s.random, None)

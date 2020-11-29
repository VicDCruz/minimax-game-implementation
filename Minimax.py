"""
g.print()
Archivo para crear el algoritmo MinMax para automatizar un juego
"""
from Gameboard import Gameboard
from Tictactoe import *


def minimax(snapshot, depth, isMaximizing, checkScore, getChildren):
    """
    Implementación básica de Minimax que genera un árbol de decisión
    Un snapshot implica una fotografía del tablero, con sus fichas actuales\n
    Obtenido de https://www.javatpoint.com/mini-max-algorithm-in-ai
    """
    if depth == 0:
        return checkScore(snapshot.board.copy(), snapshot.player, snapshot.opponent)
    if isMaximizing:
        maxScore = float('-inf')
        for child in getChildren(snapshot, snapshot.player):
            maxScore = max(minimax(child, depth - 1, False,
                                   checkScore, getChildren), maxScore)
        return maxScore
    else:
        minScore = float('inf')
        for child in getChildren(snapshot, snapshot.opponent):
            minScore = min(minimax(child, depth - 1, True,
                                   checkScore, getChildren), minScore)
        return minScore


if __name__ == "__main__":
    print("==== Tablero 3x3 ====")
    g = Gameboard(3, 3, "X", "O")
    g.addChip(True, 0, 0)
    g.addChip(False, 1, 1)
    g.addChip(False, 2, 2)
    g.addChip(True, 0, 2)
    g.print()
    print(minimax(g, 3, True, evaluate, generateMoves))
    # g.print()

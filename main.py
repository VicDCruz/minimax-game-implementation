"""
Archivo para crear el algoritmo MinMax para automatizar un juego
"""
from Gameboard import Gameboard


def getMoves(chip, movements):
    """
    TODO: Generar todos los movimientos posibles dado una ficha
    """
    
    return 
    
    pass


def getChildren(snapshot, isPlayer1, movements):
    """
    Obtener todos los movimientos posibles dado un snapshot
    """
    output = []
    for i in range(snapshot.totalChips):
        chip = snapshot.getChip(isPlayer1, i)
        for move in getMoves(chip, movements):
            if isPlayer1:
                tmp = Gameboard(snapshot.width, snapshot.height,
                                snapshot.setChip(move), snapshot.chips2)
            else:
                tmp = Gameboard(snapshot.width, snapshot.height,
                                snapshot.chips1, snapshot.setChip(move))
            output.append(tmp)
    return output


def minimax(snapshot, depth, isMaximizing, checkScore, movements, alpha, beta):
    """
    Implementación básica de Minimax que genera un árbol de decisión
    Un snapshot implica una fotografía del tablero, con sus fichas actuales
    Obtenido de https://www.javatpoint.com/mini-max-algorithm-in-ai
    """
    
    score = 0
    if depth == 0:
        return checkScore(snapshot)
    if isMaximizing:
        maxScore = float('-inf')
        for child in getChildren(snapshot, True, movements):
            score = minimax(child, depth - 1, False, score, movements, alpha, beta)
            maxScore = max(score, maxScore)      
            
            # Alpha-beta
            if maxScore >= beta:
                return maxScore
            if maxScore > alpha:
                alpha = maxScore
            
        return maxScore
    else:
        minScore = float('inf')
        for child in getChildren(snapshot, False, movements):
            score = minimax(child, depth - 1, True, score, movements)
            minScore = min(score, minScore)
            
            # Alpha-beta
            if minScore <= alpha:
                return minScore
            if minScore < beta:
                beta = minScore
                
        return minScore

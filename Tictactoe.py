"""
Programa que implementa reglas básicas para jugar el juego de Gato (Tic-Tac-Toe)
"""
SCORE = 10


def evaluate(board, chip1, chip2):
    """
    Evaluar el tablero actual\n
    chip1 es el jugador que pierde (-SCORE) o gana (-SCORE)
    """
    # Victoria para chip1 en una fila
    for row in range(0, 3):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            if board[row][0] == chip1:
                return SCORE
            elif board[row][0] == chip2:
                return -SCORE

    # Victoria para chip1 en una columna
    for col in range(0, 3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            if board[0][col] == chip1:
                return SCORE
            elif board[0][col] == chip2:
                return -SCORE

    # Victoria para chip1 en una diagonal
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == chip1:
            return SCORE
        elif board[0][0] == chip2:
            return -SCORE

    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] == chip1:
            return SCORE
        elif board[0][2] == chip2:
            return -SCORE

    # Else if none of them have won then return 0
    return 0

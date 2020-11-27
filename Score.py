import random
from Gameboard import Gameboard
from Chip import Chip


def count(snapshot, isPlayer1):
    output = 0
    for i in range(snapshot.totalChips):
        chip = snapshot.getChip(isPlayer1, i)
        if chip.onGameboard:
            output += 1
    return output / snapshot.totalChips * 100


def check(snapshot, isPlayer1):
    def countVertical(chips):
        rows = {}
        maximum = 0
        for chip in chips:
            if chip.onGameboard:
                if chip.x in rows:
                    rows[chip.x] += 1
                else:
                    rows[chip.x] = 1
                maximum = max(maximum, rows[chip.x])
        return maximum / len(chips) * 100

    def countHorizontal(chips):
        columns = {}
        maximum = 0
        for chip in chips:
            if chip.onGameboard:
                if chip.y in columns:
                    columns[chip.y] += 1
                else:
                    columns[chip.y] = 1
                maximum = max(maximum, columns[chip.y])
        return maximum / len(chips) * 100

    def countDiagonal(chips):
        diagonals = {}
        maximum = 0
        for chip in chips:
            if chip.onGameboard:
                minimum = min(chip.x, chip.y)
                key = "{0}|{1}".format(
                    chip.x - minimum, chip.y - minimum)
                if key in diagonals:
                    diagonals[key] += 1
                else:
                    diagonals[key] = 1
                maximum = max(maximum, diagonals[key])
        return maximum / len(chips) * 100

    if isPlayer1:
        chips = snapshot.chips1
    else:
        chips = snapshot.chips2
    lst = [countVertical(chips), countHorizontal(
        chips), countDiagonal(chips)]
    return sum(lst) / len(lst)


class Score:
    """
    Generador de funciones para evaluar y calificar una movida\n
    El rango está evaluado entre 0 a 100, donde 100 es la mejor puntuación posible
    """

    def random(self):
        """
        Regresa una función que crea puntaciones aleatorias
        """
        def rand(snapshot, isPlayer1):
            return random.uniform(0, 100)
        return rand

    def countByPieces(self):
        """
        Regresa una función que cuenta el número de piezas de un jugador
        """
        return count

    def checkPatterns(self):
        """
        Obtener una puntación basada en ver si se llego a un patrón\n
        o qué tan cerca está de obtener uno
        """
        return check


if __name__ == "__main__":
    s = Score()
    rand = s.random()
    for x in range(10):
        print("Número aleatorio: {}".format(rand(x, True)))
    player1 = []
    for i in range(3):
        tmp = Chip(0, i, random.randint(0, 1) == 0, 'Rojo')
        player1.append(tmp)
    board = Gameboard(3, 3, player1, [])
    board.print()
    count = s.countByPieces()
    print(count(board, True))
    check = s.checkPatterns()
    print(check(board, True))


class Gameboard:
    """
    Simulación de un tablero de juegos
    """

    def __init__(self, width, height, player, opponent):
        """
        Constructor de la clase Gameboard
        """
        self.height = height
        self.width = width
        self.board = []
        for x in range(height):
            self.board.append([])
            for y in range(width):
                self.board[x].append("\t")
        self.player = player + "\t"
        self.opponent = opponent + "\t"

    def addChip(self, isPlayer, x, y):
        """
        Añadir una nueva ficha al tablero, dependiendo del jugador
        """
        if 0 <= x and x < self.height and 0 <= y and y < self.width:
            if isPlayer:
                if self.board[x][y] == "\t":
                    self.board[x][y] = self.player
            else:
                if self.board[x][y] == "\t":
                    self.board[x][y] = self.opponent
        else:
            print("Movimiento fuera de rango")

    def print(self):
        """
        Imprimir el estado actual del tablero
        """
        base = 8 * self.width
        print(base * "-")
        for x in range(self.height):
            output = ""
            for y in range(self.width):
                output = output + self.board[x][y] + "|"
            print("|" + output)
            print(base * "-")


if __name__ == "__main__":
    print("==== Tablero 3x3 ====")
    g1 = Gameboard(3, 3, "X", "O")
    g1.addChip(True, 0, 0)
    g1.addChip(False, 1, 1)
    g1.addChip(False, 2, 2)
    g1.addChip(True, 0, 2)
    g1.print()
    print("==== Tablero 4x7 ====")
    g2 = Gameboard(4, 7, "X", "O")
    g2.addChip(True, 0, 0)
    g2.addChip(False, 1, 1)
    g2.addChip(False, 2, 2)
    g2.addChip(True, 0, 2)
    g2.print()
    print("==== Tablero 7x3 ====")
    g3 = Gameboard(7, 3, "X", "O")
    g3.addChip(True, 0, 0)
    g3.addChip(False, 1, 1)
    g3.addChip(False, 2, 2)
    g3.addChip(True, 0, 2)
    g3.print()

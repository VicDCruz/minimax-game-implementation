from Chip import Chip


class Gameboard:
    """
    Simulación de un tablero de juegos
    """

    def __init__(self, width, height, chips1, chips2):
        """
        Constructor de la clase Gameboard
        """
        self.heigth = height
        self.width = width
        self.chips1 = chips1
        self.chips2 = chips2
        self.totalChips = len(chips1)

    def getChip(self, isPlayer1, index):
        """
        Obtener una ficha específica de un jugador
        """
        if isPlayer1:
            return self.chips1[index]
        return self.chips2[index]

    def setChip(self, isPlayer1, index, chip):
        """
        Cambiar ficha de un jugador y devolver copia
        """
        if isPlayer1:
            output = self.chips1[:]
        else:
            output = self.chips2[:]
        output[index] = chip
        return output

    def moveChip(self, x, y, chip):
        """
        Mover una ficha en el tablero
        """
        if 0 <= x and x < self.width and 0 <= y and y < self.heigth:
            chip.x = x
            chip.y = y
        else:
            print("Error: Coordenadas incorrectas")

    def print(self):
        """
        Imprimir el estado actual del tablero
        """
        board = self.heigth * [self.width * ["\t"]]
        for chip in self.chips1:
            if chip.onGameboard:
                board[chip.x][chip.y] = chip.figure
        for chip in self.chips2:
            if chip.onGameboard:
                board[chip.x][chip.y] = chip.figure
        base = 4 * self.width
        print(base * "-")
        for y in range(self.heigth):
            output = ""
            for x in range(self.width):
                output = output + board[y][x] + "|"
            print("|" + output)
            print(base * "-")


if __name__ == "__main__":
    print("==== Tablero 3x3 ====")
    g1 = Gameboard(3, 3, [Chip(1,1,True,'x')], [Chip(1,2,True,'o')])
    g1.print()
    print("==== Tablero 4x7 ====")
    g2 = Gameboard(4, 7, [], [])
    g2.print()
    print("==== Tablero 7x3 ====")
    g3 = Gameboard(7, 3, [], [])
    g3.print()

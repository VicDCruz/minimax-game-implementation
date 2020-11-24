class Chip:
    """
    Representación de una ficha para el tablero de juego
    """

    def __init__(self, x, y, onGameboard, figure):
        """
        Constructor de Chip
        """
        self.x = x
        self.y = y
        self.onGameboard = onGameboard
        self.figure = figure

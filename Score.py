import random

class Score:
    """
    Generador de funciones para evaluar y calificar una movida\n
    El rango está evaluado entre 0 a 100, donde 100 es la mejor puntuación posible
    """

    def random(self):
        """
        Regresa una función que crea puntaciones aleatorias
        """
        return lambda x: random.randint(0, 100)

if __name__ == "__main__":
    s = Score()
    rand = s.random()
    for x in range(10):
        print("Número aleatorio: {}".format(rand(x)))

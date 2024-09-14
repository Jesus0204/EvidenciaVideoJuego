"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import shuffle
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2  # Lista de números del 0 al 31 duplicados
state = {'mark': None}  # Mantiene el estado de la tile seleccionada
hide = [True] * 64  # Estado de ocultamiento de las tiles


def square(x, y):
    """Dibuja un cuadrado blanco con borde negro en (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convierte las coordenadas (x, y) en el índice de una tile."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convierte el índice de una tile en coordenadas (x, y)."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Actualiza el estado del juego basado en un clic en (x, y)."""
    spot = index(x, y)
    mark = state['mark']

    # Si no hay una tile seleccionada o no coinciden, marca la nueva tile
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False  # Revela la tile seleccionada
        hide[mark] = False  # Revela la tile previamente seleccionada
        state['mark'] = None


def draw():
    """Dibuja el tablero de tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    # Dibuja las tiles ocultas
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    # Dibuja el número de la tile seleccionada
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
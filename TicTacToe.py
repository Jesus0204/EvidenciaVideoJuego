from turtle import (update, up, goto, down, circle, setup,
                    hideturtle, tracer, done, onscreenclick)

from freegames import line

"""
Dibuja la cuadricula del juego.

Parámetros:
    Ninguno.

Valor de Retorno:
    Ninguno.
"""


def grid():
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


"""
Dibuja una 'X' en la cuadricula del juego.

Parámetros:
    x (int): Coordenada de eje X de la celda donde se dibujará la 'X'.
    y (int): Coordenada eje Y de la celda donde se dibujará la 'X'.

Valor de Retorno:
    Ninguno.
"""


def drawx(x, y):
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)


"""
Dibuja una 'O' en la cuadricula del juego.

Parámetros:
    x (int): Coordenada de eje X de la celda donde se dibujará la 'O'.
    y (int): Coordenada eje Y de la celda donde se dibujará la 'O'.

Valor de Retorno:
    Ninguno.
"""


def drawo(x, y):
    up()
    goto(x + 67, y + 5)
    down()
    circle(62)


"""
Redondea un valor hacia abajo al inicio de la celda de la cuadricula
con tamaño de 133 unidades.

Parámetros:
    value (int): Coordenada (eje X o Y) que se desea redondear hacia abajo.

Valor de Retorno:
    int: Coordenada redondeada hacia abajo al inicio de la celda
    correspondiente en la cuadricula.
"""


def floor(value):
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()

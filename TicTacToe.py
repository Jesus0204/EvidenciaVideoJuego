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


# Diccionario que mantiene el estado de juego.
# Se inicia con 0 (el jugador que juega con X)
state = {'player': 0}
# Los jugadores del juego. X es el cero, y O es el uno.
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


# Configura la ventana de de 420x420 en la pantalla
setup(420, 420, 370, 0)
# Esconde el cursor para que no se vea mientras se dibuja el juego
hideturtle()
# Desactiva la animación en la actualización de dibujos
tracer(False)
# Llama a la función de grid
grid()
# Actualiza la pantalla con método de turtle
update()
# Cuando se hace click en la pantalla llama la función tap
onscreenclick(tap)
# Permite que la ventana del juego se quede abierta
done()

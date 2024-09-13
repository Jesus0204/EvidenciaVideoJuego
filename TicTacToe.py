from turtle import (update, up, goto, down, circle, setup,
                    hideturtle, tracer, done, onscreenclick,
                    color, width)

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
    color('red')
    width(5)

    centrado = 20
    line(x + centrado, y + centrado, x + 133 - centrado, y + 133 - centrado)
    line(x + centrado, y + 133 - centrado, x + 133 - centrado, y + centrado)


"""
Dibuja una 'O' en la cuadricula del juego.

Parámetros:
    x (int): Coordenada de eje X de la celda donde se dibujará la 'O'.
    y (int): Coordenada eje Y de la celda donde se dibujará la 'O'.

Valor de Retorno:
    Ninguno.
"""


def drawo(x, y):
    color('blue')
    width(5)

    up()
    goto(x + 67, y + 25)
    down()
    circle(45)


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


"""
Maneja el evento de clic del usuario para dibujar
una 'X' o una 'O' en la casilla seleccionada.

Parámetros:
    x (int): Coordenada horizontal del clic.
    y (int): Coordenada vertical del clic.

Valor de Retorno:
    Ninguno.
"""


def tap(x, y):
    # Redondea la coordenada X con la función
    x = floor(x)
    # Redondea la coordenada Y con la función
    y = floor(y)
    # Obtiene al jugador actual
    player = state['player']
    # Selecciona si se sibuja una X o una O
    draw = players[player]
    # Llama la función seleccionada para dibujar
    draw(x, y)
    # Actualiza la pantalla con método de turtle
    update()
    # Cambia al siguiente jugador del diccionario
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

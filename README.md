# EvidenciaVideoJuego

## TicTacToe - Jesús Alejandro Cedillo Zertuche A01705442

### Comentarios
Para cada función se agregó un comentario del siguiente estilo: 
```
Descripción de función

Parámetros:
    nombreParametro (tipo de variable): Descripción de la variable.

Valor de Retorno:
    nombreVariable (tipo de variable): Descripción de la variable de retorno.
```

Esto permite describir lo que hace la función de una manera clara. De igual forma se agregaron comentarios individuales a las secciones de código que no pertenecían a la función para poder entender el código de manera simple. 

### Color y tamaño de X y O
Para claridad del juego, se definió el color rojo para las X y el color azul para las O. De igual forma se modificó la manera en la que se dibujaba la X y la O. En la X se introdujo un offset para centrar el contenido, mientras que en la O se redujo el tamaño del circulo y subió en el eje y para centrarlo. Para ver estos cambios por favor busca las funciones

1. ```def drawx(x, y):```
2. ```def drawo(x, y):```

### Validación de casilla ocupada
El juego antes no se validaba si una casilla estaba ocupada, por lo que se podía insertar tanto X como Os en la misma casilla. Para cambiar esto, primero se introdujo una lista con el estado de casa casilla del tablero. Esta lista se inicializa de la siguiente manera: 
```python
boardState = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
```

Después, lo que se tenía que hacer era traducir el lugar donde se daba click a la casilla. Para esto se definió una nueva función. La función se ve así: 
```python
def get_cell(x, y):
    # Determina la columba basada en el valor de x
    if x == 66.0:
        col = 2
    elif x == -67.0:
        col = 1
    elif x == -200.0:
        col = 0

    # Determina la fila basada en el valor de y
    if y == 66.0:
        row = 0
    elif y == -67.0:
        row = 1
    elif y == -200.0:
        row = 2

    return int(row), int(col)
```

Finalmente, en las funciones de drawx y drawo cambie el estado del tablero. En ambas funciones agregue lo siguiente: 
```python
  # Sacas el número de la columna en la que se dio click
    row, col = get_cell(x, y)

    # Cambias el estado del tablero a 1 cuando se inserte la X
    boardState[row][col] = 1
```
Y esas fueron todas las modificaciones que hice en está evidencia :)
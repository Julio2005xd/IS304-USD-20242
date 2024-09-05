'''
 * Crea un programa capaz de gestionar una pieza de Tetris.
 * - La pantalla de juego tiene 10 filas y 10 columnas representadas por símbolos 🔲
 * - La pieza de tetris a manejar será la siguiente (si quieres, puedes elegir otra):
 *   🔳
 *   🔳🔳🔳
 * - La pieza aparecerá por primera vez en la parte superior izquierda de la pantalla de juego.
 *   🔳🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔳🔳🔳🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 * - Debes desarrollar una función capaz de desplazar y rotar la pieza en el tablero,
 *   recibiendo una acción cada vez que se llame, mostrando cómo se visualiza en la pantalla  de juego.
 * - Las acciones que se pueden aplicar a la pieza son: derecha, izquierda, abajo, rotar.
 * - Debes tener en cuenta los límites de la pantalla de juego.
'''
from typing import Any


class Tetris ():
    def __init__(self, filas, columnas) -> None:
        self.__filas = filas
        self.__columnas = columnas
    
    def getfilas(self):
        return self.__filas
    
    def getcolumnas(self):
        return self.__columnas

    tablero = [['🔲' for _ in range(tablero.getcolumnas())] for _ in range(tablero.getfilas())]

# Definir la pieza de Tetris (coordenadas relativas)
    pieza = [(0, 0), (1, 0), (1, 1), (1, 2)]

# Función para imprimir el tablero
    def imprimir_tablero(tablero):
        for fila in tablero:
            print(''.join(fila))
        print()

    for (x, y) in pieza:
        tablero[x][y] = '🔳'

    imprimir_tablero(tablero)
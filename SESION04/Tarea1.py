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
from typing import List, Tuple
import time
import keyboard

class Tetris:
    def __init__(self, filas: int, columnas: int) -> None:
        self.__filas = filas
        self.__columnas = columnas
        self.__tablero = self.generar_tablero()
    
    def set_filas(self, filas: int) -> None:
        self.__filas = filas
        
    def set_columnas(self, columnas: int) -> None:
        self.__columnas = columnas
    
    def get_filas(self) -> int:
        return self.__filas
    
    def get_columnas(self) -> int:
        return self.__columnas
    
    def generar_tablero(self) -> List[List[str]]:
        return [['🔲' for _ in range(self.__columnas)] for _ in range(self.__filas)]
    
    def imprimir_tablero(self) -> None:
        for fila in self.__tablero:
            print(''.join(fila))
    
    def colocar_pieza(self, pieza: List[Tuple[int, int]], simbolo: str) -> None:
        for (x, y) in pieza:
            self.__tablero[x][y] = simbolo
    
    def limpiar_pieza(self, pieza: List[Tuple[int, int]]) -> None:
        for (x, y) in pieza:
            self.__tablero[x][y] = '🔲'
    
    
    def es_valida(self, pieza):
        for x, y in pieza:
            if x < 0 or x >= self.__filas or y < 0 or y >= self.__columnas or self.__tablero[x][y] != ' ':
                return False
        return True
    
    def eliminar_lineas_completas(self):
        nuevas_filas = [fila for fila in self.__tablero if ' ' in fila]
        lineas_eliminadas = self.__filas - len(nuevas_filas)
        nuevas_filas = [[' ' for _ in range(self.__columnas)] for _ in range(lineas_eliminadas)] + nuevas_filas
        self.__tablero = nuevas_filas

def main() -> None:
    filas = 10
    columnas = 10
    
    juego = Tetris(filas, columnas)
    pieza = [(0, 0), (1, 0), (1, 1), (1, 2)]
    juego.colocar_pieza(pieza, '🔳')
    juego.imprimir_tablero()
    
    while True:
        movimiento = input("Por favor digite su siguiente accion: ")
        juego.limpiar_pieza(pieza)  # Limpiar la posición anterior de la pieza

        if movimiento == 'a':
            nueva_pieza = pieza = [(x + 1, y - 1) for (x, y) in pieza]
            if juego.es_valida(nueva_pieza):
                pieza = nueva_pieza
        elif movimiento == 'd':
            nueva_pieza = pieza = [(x + 1, y + 1) for (x, y) in pieza]
            if juego.es_valida(nueva_pieza):
                pieza = nueva_pieza
        elif movimiento == 's':
            nueva_pieza = pieza = [(x + 2, y) for (x, y) in pieza]
            if juego.es_valida(nueva_pieza):
                pieza = nueva_pieza

        if any(y == 9 for (y, _) in pieza):  # Check if any coordinate reaches 10
            juego.colocar_pieza(pieza, '🔳')  # Colocar la pieza en su nueva posición
            juego.imprimir_tablero()
            pieza = [(0, 0), (1, 0), (1, 1), (1, 2)]  # Generate new piece
            juego.colocar_pieza(pieza, '🔳')  # Colocar la nueva pieza en la posición inicial
        else:
            juego.colocar_pieza(pieza, '🔳')  # Colocar la pieza en su nueva posición
            juego.imprimir_tablero()

        time.sleep(0.5)

if __name__ == "__main__":
    main()
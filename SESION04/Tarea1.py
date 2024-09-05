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
    
    def colocar_pieza(self, pieza: List[Tuple[int, int]], simbolo: str) -> None:
        for (x, y) in pieza:
            self.__tablero[x][y] = simbolo
    
    def imprimir_tablero(self) -> None:
        for fila in self.__tablero:
            print(''.join(fila))
        print()

def main() -> None:
    filas = 10
    columnas = 10
    
    juego = Tetris(filas, columnas)
    
    pieza = [(0, 0), (1, 0), (1, 1), (1, 2)]

    juego.colocar_pieza(pieza, '🔳')

    juego.imprimir_tablero()

if __name__ == "__main__":
    main()

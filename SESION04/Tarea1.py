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
import random

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
        print()
    
    def colocar_pieza(self, pieza: List[Tuple[int, int]], simbolo: str) -> None:
        for (x, y) in pieza:
            self.__tablero[x][y] = simbolo
    
    def limpiar_pieza(self, pieza: List[Tuple[int, int]]) -> None:
        for (x, y) in pieza:
            self.__tablero[x][y] = '🔲'
    
    def es_valida(self, pieza: List[Tuple[int, int]]) -> bool:
        for x, y in pieza:
            if x < 0 or x >= self.__filas or y < 0 or y >= self.__columnas or self.__tablero[x][y] != '🔲':
                return False
        return True
    
    def eliminar_lineas_completas(self) -> None:
        nuevas_filas = [fila for fila in self.__tablero if '🔲' in fila]
        lineas_eliminadas = self.__filas - len(nuevas_filas)
        if lineas_eliminadas > 0:
            print()
        nuevas_filas = [['🔲' for _ in range(self.__columnas)] for _ in range(lineas_eliminadas)] + nuevas_filas
        self.__tablero = nuevas_filas
        
    def rotar_pieza(self, pieza: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        pivote = pieza[0]
        nueva_pieza = []
        for x, y in pieza:
            nuevo_x = pivote[0] - (y - pivote[1])
            nuevo_y = pivote[1] + (x - pivote[0])
            nueva_pieza.append((nuevo_x, nuevo_y))
        return nueva_pieza
    
    def tablero_lleno(self) -> bool:
        return all(celda != '🔲' for celda in self.__tablero[0])

def main() -> None:
    filas = 10
    columnas = 10
    
    juego = Tetris(filas, columnas)
    pieza = [(0, 0), (1, 0), (1, 1), (1, 2)]
    juego.colocar_pieza(pieza, '🔳')
    juego.imprimir_tablero()
    
    while True:
        movimiento = input("Por favor digite su siguiente acción (a: izquierda, d: derecha, s: abajo, r: rotar): ")
        juego.limpiar_pieza(pieza)

        if movimiento == 'a':
            nueva_pieza = [(x+1, y-1) for (x, y) in pieza]
            if juego.es_valida(nueva_pieza):
                pieza = nueva_pieza
        elif movimiento == 'd':
            nueva_pieza = [(x+1, y+1) for (x, y) in pieza]
            if juego.es_valida(nueva_pieza):
                pieza = nueva_pieza
        elif movimiento == 's':
            nueva_pieza = [(x+1, y) for (x, y) in pieza]
            if juego.es_valida(nueva_pieza):
                pieza = nueva_pieza
        elif movimiento == 'r':
            nueva_pieza = juego.rotar_pieza(pieza)
            if juego.es_valida(nueva_pieza):
                pieza = nueva_pieza
        
        if not juego.es_valida([(x+1, y) for (x, y) in pieza]):  
            juego.colocar_pieza(pieza, '🔳')  
            juego.eliminar_lineas_completas()
            
            if juego.tablero_lleno():  
                juego.imprimir_tablero()
                print("Tablero lleno. Fin del juego.")
                break
            numero_aleatorio = random.randint(0, columnas-3)  
            pieza = [(0, numero_aleatorio), (1, numero_aleatorio), (1, numero_aleatorio + 1), (1, numero_aleatorio + 2)]
            if not juego.es_valida(pieza):  
                juego.imprimir_tablero()
                print("No se puede colocar una nueva pieza. Fin del juego.")
                break
        else:
            juego.colocar_pieza(pieza, '🔳')  
        
        juego.imprimir_tablero()

if __name__ == "__main__":
    main()
from typing import List, Tuple
import random

class Tetris:
    def __init__(self, filas: int, columnas: int) -> None:
        self.__filas = filas
        self.__columnas = columnas
        self.__tablero = self.generar_tablero()
    
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
            if not (0 <= x < self.__filas and 0 <= y < self.__columnas) or self.__tablero[x][y] != '🔲':
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
        return [(pivote[0] - (y - pivote[1]), pivote[1] + (x - pivote[0])) for x, y in pieza]
    
    def tablero_lleno(self) -> bool:
        return any(celda != '🔲' for celda in self.__tablero[0])

def generar_nueva_pieza(columnas: int) -> List[Tuple[int, int]]:
    numero_aleatorio = random.randint(0, columnas - 3)
    return [(0, numero_aleatorio), (1, numero_aleatorio), (1, numero_aleatorio + 1), (1, numero_aleatorio + 2)]

def main() -> None:
    filas = 10
    columnas = 10
    
    juego = Tetris(filas, columnas)
    pieza = generar_nueva_pieza(columnas)
    pieza = [(0, 0), (1, 0), (1, 1), (1, 2)]
    juego.colocar_pieza(pieza, '🔳')
    juego.imprimir_tablero()
    
    while True:
        movimiento = input("Por favor digite su siguiente acción (a: izquierda, d: derecha, s: abajo, r: rotar): ")
        juego.limpiar_pieza(pieza)

        if movimiento == 'a':
            nueva_pieza = [(x+1, y-1) for (x, y) in pieza]
        elif movimiento == 'd':
            nueva_pieza = [(x+1, y+1) for (x, y) in pieza]
        elif movimiento == 's':
            nueva_pieza = [(x+1, y) for (x, y) in pieza]
        elif movimiento == 'r':
            nueva_pieza = juego.rotar_pieza(pieza)
        else:
            nueva_pieza = pieza

        if juego.es_valida(nueva_pieza):
            pieza = nueva_pieza
        
        if not juego.es_valida([(x+1, y) for (x, y) in pieza]):
            juego.colocar_pieza(pieza, '🔳')
            juego.eliminar_lineas_completas()
            
            if juego.tablero_lleno():
                juego.imprimir_tablero()
                print("Tablero lleno. Fin del juego.")
                break
            
            pieza = generar_nueva_pieza(columnas)
            if not juego.es_valida(pieza):
                juego.imprimir_tablero()
                print("No se puede colocar una nueva pieza. Fin del juego.")
                break
        else:
            juego.colocar_pieza(pieza, '🔳')
        
        juego.imprimir_tablero()

if __name__ == "__main__":
    main()
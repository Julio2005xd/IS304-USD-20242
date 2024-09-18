'''Realizar un programa que permita llenar una lista, mostrar la lista con los numeros primos menos o iguales a un numero entero dado por 
el usuario utilice almenos una clase que sea de encapsulamiento '''

class NumerosPrimos:
    def __init__(self, numero) -> None:
        self.__numero = numero

    def __es_primo(self, num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def __obtener_primos_hasta(self, n):
        primos = []
        for num in range(2, n + 1):
            if self.__es_primo(num):
                primos.append(num)
        return primos

    def obtener_primos(self):
        return self.__obtener_primos_hasta(self.__numero)

class main:
    print("Por favor digite un numero")
    numero = int(input())
    numeros_primos = NumerosPrimos(numero)
    print(numeros_primos.obtener_primos())

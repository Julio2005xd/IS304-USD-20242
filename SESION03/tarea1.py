'''
Tarea para antes de la  próxima clase:
Crear un programa en Python que cree una clase denominada CuentaBancaria. Agregar encapsulamiento y sobrecarga del constructor de clase, asi como los métodos get y set requeridos para gestionar los atributos de dicha clase.
Los atributos de la clase debern ser: __numeroCta, __nombreCliente, __fechaApertura, __saldo.
Agregar metodos para aperturar cuentas, realizar consignaciones y retiros controlados (es decir, no permitir consignaciones negativas, ni retiros superiores al saldo, las aperturas deben exigir un valor inicial mínimo de 100 mil pesos).
Crear un menú para crear objetos y realizar las diversas operaciones referidas.

'''
class CuentaBancaria:
    __numeroCta = 0
    __nombreCliente = ""
    __fechaApertura = "00/00/0000"
    __saldo = 0
    def __init__(self, __numeroCta, __nombreCliente, __fechaApertura, __saldo) -> None:
        self.__numeroCta = __numeroCta
        self.__nombreCliente = __nombreCliente
        self.__fechaApertura = __fechaApertura
        self.__saldo = __saldo
    
    def mostrar_info(self):
        print(f"Número de cuenta: {self.__numeroCta}")
        print(f"Titular: {self.__nombreCliente}")
        print(f"Saldo: {self.__saldo}")
    
class Menu:
    def __init__(self):
        self.cuentas = []
    
    def aperturar_Cuenta(self, numero_cuenta, titular, fechaApertura = 0, saldo_inicial=0):
        nueva_cuenta = CuentaBancaria(numero_cuenta, titular, fechaApertura, saldo_inicial)
        self.cuentas.append(nueva_cuenta)
        print(f"Cuenta para {titular} con fecha de creacion de cuenta {fechaApertura} y numero de cuenta {numero_cuenta} ha sido aperturada con éxito.")

mi_banco = Menu()
mi_banco.aperturar_Cuenta("123456789", "Juan Pérez", "2/3/2024", 2000)


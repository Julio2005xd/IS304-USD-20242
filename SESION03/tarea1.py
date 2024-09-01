'''
Tarea para antes de la  próxima clase:
Crear un programa en Python que cree una clase denominada CuentaBancaria. Agregar encapsulamiento y sobrecarga del constructor de clase, asi como los métodos get y set requeridos para gestionar los atributos de dicha clase.
Los atributos de la clase debern ser: __numeroCta, __nombreCliente, __fechaApertura, __saldo.
Agregar metodos para aperturar cuentas, realizar consignaciones y retiros controlados (es decir, no permitir consignaciones negativas, ni retiros superiores al saldo, las aperturas deben exigir un valor inicial mínimo de 100 mil pesos).
Crear un menú para crear objetos y realizar las diversas operaciones referidas.

'''
from datetime import date

class CuentaBancaria:
    numeroCta = 0
    nombreCliente = ""
    fechaApertura = ""
    saldo = 0
    def __init__(self, numeroCta, nombreCliente, fechaApertura, saldo) -> None:
        self.__numeroCta = numeroCta
        self.__nombreCliente = nombreCliente
        self.__fechaApertura = fechaApertura
        self.__saldo = saldo
    
    def get_numeroCta(self):
        return self.__numeroCta
    def get_nombreCliente(self):
        return self.__nombreCliente
    def get_fechaApertura(self):
        return self.__fechaApertura
    def get_saldo(self):
        return self.__saldo
        
class Menu:
    def __init__(self):
        self.cuentas = []
    
    def aperturar_Cuenta(self, numeroCta, nombreCliente):
        obtenerFecha = date.today()
        obtenerFecha.strftime("%d/%m/%Y")
        nueva_cuenta = CuentaBancaria(numeroCta, nombreCliente, obtenerFecha, 0)
        self.cuentas.append(nueva_cuenta)
        print(f"Cuenta para {nueva_cuenta.get_nombreCliente()} con fecha de creacion de cuenta {nueva_cuenta.get_fechaApertura()} y numero de cuenta {nueva_cuenta.get_numeroCta()} ha sido aperturada con éxito con un saldo inicial de:{nueva_cuenta.get_saldo()}$.")

mi_banco = Menu()
print("Banco")
numeroCta = input(f"Por favor digite el numero de cuenta")
nombreCliente = input(f"Por favor digite el nombre del titular de cuenta")
mi_banco.aperturar_Cuenta(numeroCta, nombreCliente)
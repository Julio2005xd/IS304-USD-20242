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
    
    @classmethod
    def aperturarCuenta(cls):
        numeroCta = input(f"Por favor digite el numero de cuenta")
        nombreCliente = input(f"Por favor digite el nombre del titular de cuenta")
        obtenerFecha = date.today()
        obtenerFecha.strftime("%d/%m/%Y")
        nueva_cuenta = CuentaBancaria(numeroCta, nombreCliente, obtenerFecha, 0)
        print(f"Cuenta para {nueva_cuenta.get_nombreCliente()} con fecha de creacion de cuenta {nueva_cuenta.get_fechaApertura()} y numero de cuenta {nueva_cuenta.get_numeroCta()} ha sido aperturada con éxito con un saldo inicial de:{nueva_cuenta.get_saldo()}$.")
        
    def set_saldo(self, nuevoSaldo):
        if nuevoSaldo > 0:
            self.__saldo += nuevoSaldo
        else:
            print("El saldo no puede ser negativo")        
    def consignaciones(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
        else:
            print("La cantidad a depositar debe ser positiva")     

cuentas = []

cuenta1 = CuentaBancaria(123456789, "Juan Lopez", "2023-08-01", 200000)
cuenta2 = CuentaBancaria(987654321, "Maria Perez", "2022-11-22", 150000)
cuenta3 = CuentaBancaria(234567890, "Carlos Gomez", "2020-01-05", 300000)
cuenta4 = CuentaBancaria(345678901, "Ana Martinez", "2019-03-11", 250000)
cuenta5 = CuentaBancaria(456789012, "Pedro Rodriguez", "2024-06-18", 100000)
cuenta6 = CuentaBancaria(567890123, "Laura Sanchez", "2024-04-25", 500000)
cuenta7 = CuentaBancaria(678901234, "Sofia Jimenez", "2018-12-09", 120000)
cuenta8 = CuentaBancaria(789012345, "Luis Fernandez", "2023-09-11", 180000)

cuentas.extend([cuenta1, cuenta2, cuenta3, cuenta4, cuenta5, cuenta6, cuenta7, cuenta8])

print("Bienvenido al banco")
opcion = input("Digite 1 si es un nuevo usuario o 2 si es un cliente del banco")
if opcion == "1":
    nueva_cuenta = CuentaBancaria.aperturarCuenta()
    cuentas.append(nueva_cuenta)
elif opcion == "2":
    cuenta_encontrada = None
    
    while True:
        numCuenta = input("Por favor, digite el número de su cuenta: ")
        
        for cuenta in cuentas:
            if str(cuenta.get_numeroCta()) == numCuenta:
                cuenta_encontrada = cuenta
                break
        
        if cuenta_encontrada:
            print(f"Bienvenid@ {cuenta_encontrada.get_nombreCliente()}, su saldo actual esta en: {cuenta_encontrada.get_saldo()}$")
            break  
        else:
            print("Número de cuenta no encontrado, por favor vuelva a intentarlo.")
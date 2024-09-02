'''
Programa de sistema de banco
'''
from datetime import date

class CuentaBancaria:
    def __init__(self, numeroCta, nombreCliente, fechaApertura, saldo) -> None:
        self.__numeroCta = numeroCta
        self.__nombreCliente = nombreCliente
        self.__fechaApertura = fechaApertura
        self.__saldo = saldo
    
    def set_numeroCta(self, numeroCta):
        self.__numeroCta = numeroCta
    
    def set_nombreCliente(self, nombreCliente):
        self.__nombreCliente = nombreCliente
    
    def set_fechaApertura(self, fechaApertura):
        self.__fechaApertura = fechaApertura
    
    def set_saldo(self, saldo):
        if saldo >= 0:
            self.__saldo = saldo
        else:
            print("El saldo no puede ser negativo.")
    
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
        while True:
            numeroCta = input("Por favor, ingrese el número de cuenta: ")
            if not numeroCta.isdigit():
                print("El número de cuenta debe contener solo dígitos.")
                continue
            
            nombreCliente = input("Por favor, ingrese el nombre del titular de la cuenta: ")
            
            while True:
                try:
                    saldo = int(input("Por favor, ingrese el saldo inicial de su nueva cuenta (mínimo $100000): "))
                    if saldo >= 100000:
                        break
                    else:
                        print("Por favor, ingrese una cantidad igual o superior a $100000 para abrir su nueva cuenta.")
                except ValueError:
                    print("El saldo debe ser un número entero.")
            
            obtenerFecha = date.today().strftime("%d/%m/%Y")
            nueva_cuenta = cls(numeroCta, nombreCliente, obtenerFecha, saldo)
            print(f"Cuenta para {nueva_cuenta.get_nombreCliente()} con fecha de creación {nueva_cuenta.get_fechaApertura()} y número de cuenta {nueva_cuenta.get_numeroCta()} ha sido aperturada con éxito con un saldo inicial de: ${nueva_cuenta.get_saldo()}.")
            nueva_cuenta.menu()
            return nueva_cuenta
    
    def consignaciones(self, cantidad):
        if cantidad > 0:
            nuevo_saldo = self.get_saldo() + cantidad
            self.set_saldo(nuevo_saldo)
            print(f"Consignación exitosa. Su nuevo saldo es: {self.get_saldo()}$.")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if cantidad <= self.get_saldo():
            nuevo_saldo = self.get_saldo() - cantidad
            self.set_saldo(nuevo_saldo)
            print(f"Retiro exitoso. Su nuevo saldo es: {self.get_saldo()}$.")
        else:
            print("La cantidad a retirar es mayor a su saldo actual.")
            
    def menu(self):
        while True:
            print("(1) Realizar consignación")
            print("(2) Realizar retiro")
            print("(3) Consultar saldo")
            print("(4) Salir")
            opcion = input("Seleccione la acción que desea realizar: ")
            
            if opcion == '1':
                while True:
                    try:
                        cantidad = int(input("Ingrese la cantidad que desea consignar: "))
                        if cantidad > 0:
                            self.consignaciones(cantidad)
                            break
                        else:
                            print("Por favor, ingrese un número positivo.")
                    except ValueError:
                        print("Entrada no válida, por favor ingrese un número entero.")
            elif opcion == '2':
                while True:
                    try:
                        cantidad = int(input("Ingrese la cantidad a retirar: "))
                        if cantidad >= 0:
                            self.retirar(cantidad)
                            break
                        else:
                            print("Por favor, ingrese un número positivo.")
                    except ValueError:
                        print("Entrada no válida, por favor ingrese un número entero.")
            elif opcion == '3':
                print(f"Su saldo actual es: {self.get_saldo()}$.")
            elif opcion == '4':
                print("Gracias por usar el banco. Hasta luego.")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

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

print("Bienvenido al banco. Por favor, seleccione una opción:")
while True:
    print ("(1) Abrir cuenta")
    print ("(2) Iniciar sesión")
    print ("(3) Salir")
    opcion = input()
    if opcion == "1":
        nueva_cuenta = CuentaBancaria.aperturarCuenta()
        cuentas.append(nueva_cuenta)
    elif opcion == "2":
        cuenta_encontrada = None
    
        while True:
            numCuenta = input("Por favor, ingrese el número de su cuenta: ")
        
            for cuenta in cuentas:
                if str(cuenta.get_numeroCta()) == numCuenta:
                    cuenta_encontrada = cuenta
                    break
        
            if cuenta_encontrada:
                print(f"Bienvenido/a {cuenta_encontrada.get_nombreCliente()}, su saldo actual es: ${cuenta_encontrada.get_saldo()}.")
                cuenta_encontrada.menu()
                break  
            else:
                print("Número de cuenta no encontrado, por favor intente de nuevo.")
    elif opcion == "3":
        print ("Gracias por usar nuestros servicios, hasta luego")
        break
    else:
        print("Opción no válida, por favor intente de nuevo.")
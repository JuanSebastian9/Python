class Persona:
    def __init__(self,name,edad):       #costructor (init)  que se llame a el mismo (self) mandar el nombre y la edad
          self.name = name
          self.edad = edad              #elegir el parametro self.edad es igual a edad

    def saludar(self):                  #crear la funcion de saludar se va incovar a el mismo (self)
        print(f"Hola,mi nombre es {self.name} y tengo {self.edad}")   #formato para que lo llene el

persona1 = Persona("ana","25")
persona2 = Persona("Luis","30")

persona1.saludar()
persona2.saludar()


class banco:
    def __init__(self,account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def depositar(self,monto):
        if self.is_active:
            self.balance += monto
            print(f"Se ha depositado {monto}. Saldo actual: {self.balance}")
        else:
            print("No se puede depositar, Cuenta inactiva")

    def retirar(self,monto):
            if self.is_active:
                if monto <= self.balance:
                    self.balance -= monto
                    print(f"Se ha retirado {monto}. Saldo actual: {self.balance}")
            else:
                print("No se puede depositar, Cuenta inactiva")

    def desactivar_cuenta (self):
            self.is_activar = False
            print(f"La cuenta ha sido desactivada.")

    def activar_cuenta(self):
            self.is_activar = True
            print(f"La cuenta ha sido activada.")

account1 = banco("Ana",500)
account2 = banco ("Luis",1000)

#Llamada a los métodos.
account1.depositar(200)
account2.depositar(100)
account1.desactivar_cuenta()
account1.depositar(50)
account1.desactivar_cuenta()
account1.depositar(50)

#ejemplo de assert
#suma 
def suma(numero1, numero2):
  return numero1 + numero2

assert suma(5, 7) == 12

#multiplicacion 
def multiplicacion(numero1,numero2):
  return numero1 * numero2

assert multiplicacion(5, 2) == 10
assert multiplicacion(5, 5) == 25
assert multiplicacion(5, 8) == 40


#1 ejemplo para que escriba el usuario 

marca = input("Elige una marca de celular: ")

if marca.lower() == "lg":
    print("Celular disponible")
else:
    print("Celular no disponible")

#2 ejemplo de f

def saludar(self):                  #crear la funcion de saludar se va incovar a el mismo (self)
        print(f"Hola,mi nombre es {self.name} y tengo {self.edad}")   #formato para que lo llene el


#3 ejemplo de def,if, else , class


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


#7 ejemplo de return

def make_negative(numero):
    return -abs(numero)  #retomamos para que me lo devuleva abs en negativo

# Ejemplo de uso
print(make_negative(5))  # Output: -5
print(make_negative(-3)) # Output: -3


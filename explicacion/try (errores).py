
try:
    valor = int(input("Ingresa un número: "))
    resultado = 10 / valor
    print(f"El resultado es {resultado}")
except ValueError:
    print("Por favor, ingresa un número válido.") # Si el usuario ingresa "a(ningun numero)":
except ZeroDivisionError:
    print("No se puede dividir por cero.")# Si el usuario ingresa "0":
except:
    print('Ha sucedido algo extraño, ¡lo siento!')


#2 ejemplo dentro de un class
class CuentaBancaria:
    def __init__(self, balance):
        self.balance = balance

    def retirar(self, cantidad):
        try:
            if cantidad > self.balance:
                # Si intentan retirar más de lo que hay en la cuenta, lanzamos una excepción
                raise ValueError("Saldo insuficiente")
            self.balance -= cantidad
            print(f"Has retirado {cantidad}. Nuevo saldo: {self.balance}")
        except ValueError as e:
            # Capturamos la excepción y mostramos un mensaje de error
            print(f"Error: {e}")
        except Exception as e:
            # Capturamos cualquier otra excepción no anticipada
            print(f"Ha ocurrido un error inesperado: {e}")

#ejemplo 
try:
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)        
except:
    print('No se que hacer con', value)

# Crear una instancia de la cuenta bancaria
cuenta = CuentaBancaria(100)

# Intentar retirar una cantidad mayor a la que hay en la cuenta
cuenta.retirar(150)  # Esto lanzará un ValueError

#3 ejemplos 

try:
    edad = int(input("Introduce tu edad: "))
    print(f"Tu edad es {edad}")
except ValueError:
    print("Error: Debes introducir un número.")
except Exception as e:
    print("capturamos otro error")


#ejemplo 

try:
    divisor = int(input("Ingresa un número divisor: "))
    resultado = 100 / divisor
    print(f"El resultado es {resultado}")
except ValueError:
    print("Error: Debes introducir un número válido.")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")

#ejemplo

try:
    nombre = input("Introduce tu nombre: ")
    print(f"Hola, {nombre}!")
except Exception as e:
    print(f"Ha ocurrido un error: {e}")

    #4 ejemplo de try,except,input


try:
    valor = int(input("Ingresa un número: "))
    resultado = 10 / valor
    print(f"El resultado es {resultado}")
except ValueError:
    print("Por favor, ingresa un número válido.")
except ZeroDivisionError:
    print("No se puede dividir por cero.")

#juego de numero mayor gana


#opciones
import random
opciones = ["1","2","3","4","5","6"]
#determinar ganador
def determinar_ganador(usuario, computadora):           
    if usuario == computadora:                             #si el usuario es igual a computadora 
       return "empate"                                      #colocar empate
    if(usuario == "2" and computadora == "1") or \
        (usuario == "3" and computadora == "2") or \
        (usuario == "4" and computadora == "3") or \
        (usuario == "5" and computadora == "4") or \
        (usuario == "6" and computadora == "5"):
        return "ganaste"               #si usuario pone 2 y computadora 1 colocar gana de lo contraria(else) perdiste
    else:
        return "perdiste"

print("elige un numero")
usuario = input(opciones)
print("si tu numero fue mayor del que el oponenete ganas")
# Elección de la computadora
computadora = random.choice(opciones)
print(f"La computadora eligió: {computadora}")
resultado = determinar_ganador(usuario, computadora)
print(resultado)



#juego de piedra papel o tijera



# Opciones disponibles
opciones = ["piedra", "papel", "tijera"]

# Función para determinar el ganador
def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        return "Ganaste"
    else:
        return "Perdiste"

# Bucle principal del juego
while True:
    # Elección del usuario
    usuario = input("Elige piedra, papel o tijera (o 'salir' para terminar): ").lower()
    
    if usuario == "salir":
        break
    if usuario not in opciones:
        print("Opción no válida. Intenta de nuevo.")
        continue
    
    # Elección de la computadora
    computadora = random.choice(opciones)
    print(f"La computadora eligió: {computadora}")
    
    # Determinar el ganador
    resultado = determinar_ganador(usuario, computadora)
    print(resultado)

    import random
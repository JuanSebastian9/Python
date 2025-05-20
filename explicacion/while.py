
x = 0
while x < 5:            #mientras que x sea menor que 5 
    print(x)            #que imprima x
    x += 1             #x cuando imprima se va a sumar 1

#cuando llegue a 3 parar (break)
    x = 0
while x < 5:
    if x ==3:         #cuando llegue a 3 parar (break)
       break   
    print(x)
    x += 1

#para saltar un numero

numbers = [1,2,3,4,5,6]
for i in numbers:
        if i == 3:       
           continue
        print(i)    # Omite el 3
        
def mostrar_menu():
    print("\nMenú:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")

while True:
    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        print("Has elegido la Opción 1")
    elif opcion == "2":
        print("Has elegido la Opción 2")
    elif opcion == "3":
        print("Has elegido la Opción 3")
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")
      
# Inicializamos la variable para controlar el bucle
marca_seleccionada = ""

# El bucle se repite hasta que el usuario elija "LG"
while marca_seleccionada.lower() != "lg":
    # Pedir al usuario que elija una marca
    marca_seleccionada = input("Elige una marca de celular: ")

    # Comprobamos la selección del usuario
    if marca_seleccionada.lower() == "lg":
        print("Celular disponible. ¡Excelente elección!")
    else:
        print(f"Lo siento, la marca {marca_seleccionada} no está disponible. Intenta de nuevo.")
        
print("Gracias por utilizar nuestra tienda en línea.")


# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.
 
odd_numbers = 0
even_numbers = 0
 
# Lee el primer número.
number = int(input("Introduce un número o escribe 0 para detener: "))
 
# 0 termina la ejecución.
while number != 0:
    # Verificar si el número es impar.
    if number % 2 == 1:
        # Incrementar el contador de números impares odd_numbers.
        odd_numbers += 1
    else:
        # Incrementar el contador de números pares even_numbers.
        even_numbers += 1
    # Leer el siguiente número.
    number = int(input("Introduce un número o escribe 0 para detener: "))
 
# Imprimir resultados.
print("Conteo de números impares:", odd_numbers)
print("Conteo de números pares:", even_numbers)

#crea un bucle donde si no pone el numero secreto se quede atrapado en un bucle

secret_number = 777


nombre = (input("como te llamas: "))
numero = int(input("introduce numero: "))
while numero != 777:
       print("¡Ja, ja! ¡Estás atrapado en mi bucle!",nombre)
       numero = int(input("Introduce un número nuevamente: "))
print ("¡Bien hecho, muggle! Eres libre ahora.",nombre)

#while ejemplo con if 

largest_number = -99999999
counter = 0

while True:
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")
 
#Diseña un programa que use un bucle while y le pida continuamente al usuario que ingrese una palabra a menos que ingrese "chupacabra" como la palabra de output secreta, en cuyo 
#caso el mensaje "Has dejado el bucle con éxito." debe imprimirse en la pantalla y el bucle debe terminar.

while True:
    palabra = input("ingrese nueva palabra: ")
    if palabra == "chupacabra":
        print("Has dejado el bucle con éxito.")
        break

#28 ordenar lista 

my_list = [8, 10, 6, 2, 4]  # lista a ordenar
swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.

while swapped:
    swapped = False  # no hay intercambios hasta ahora
    for i in range(len(my_list) - 1):  # Recorremos la lista hasta el penúltimo elemento
        if my_list[i] > my_list[i + 1]:  # Si el elemento actual es mayor que el siguiente...
            swapped = True  # Entonces hay que intercambiar.
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # Intercambiamos los elementos para ordenarlos en orden ascendente
#consola 
# Comparar 2 y 4 → No se intercambian.
#Comparar 4 y 6 → No se intercambian.
#Comparar 6 y 8 → No se intercambian.
#Comparar 8 y 10 → No se intercambian. resultado [2, 4, 6, 8, 10]


#ejemplo de calificacion de estudiantes

clase_escolar = {}  # Diccionario para almacenar estudiantes y sus calificaciones DIC(llave de acceso y informacion)

while True:
    nombre = input("Ingresa el nombre del estudiante: ")  # Pedimos el nombre del estudiante
    if nombre == '':  # Si el nombre está vacío, terminamos el bucle
        break
    
    calificacion = int(input("Ingresa la calificación del estudiante (0-10): "))  # Pedimos la calificación
    if calificacion not in range(0, 11):  # Si la calificación no está entre 0 y 10, terminamos el bucle
        break
    
    if nombre in clase_escolar:
        clase_escolar[nombre] += (calificacion,)  # Agregamos la calificación a la tupla existente
    else:
        clase_escolar[nombre] = (calificacion,)  # Creamos una nueva tupla con la calificación inicial
        
# Recorremos los nombres de los estudiantes en orden alfabético
for nombre in sorted(clase_escolar.keys()):
    suma = 0  # Variable para la suma de calificaciones
    contador = 0  # Contador de calificaciones
    for calificacion in clase_escolar[nombre]:  # Recorremos las calificaciones del estudiante
        suma += calificacion  # Sumamos las calificaciones
        contador += 1  # Contamos cuántas calificaciones tiene el estudiante
    print(nombre, ":", suma / contador)  # Calculamos e imprimimos el promedio
    
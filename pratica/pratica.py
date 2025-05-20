
#codewars categorias = listas o problemas
# -------------------------------
#1 escribe si el petalo de flor 2,4,6(par) esta enamdorado de lo contrario no esta enamorado(impar) tiene que ser par y impar para que esten enamorado problema
# -------------------------------

def lovefunc(a, b):
#Esta línea define una función llamada lovefunc que toma dos argumentos: a y b.


    if a % 2 == 0 and b % 2 == 0:
        return False
#a % 2 == 0 verifica si a es par (un número es par si al dividirlo entre 2 el residuo es 0).
#b % 2 == 0 verifica si b es par.
#Si ambos a y b son pares, la función retorna False, es decir, no están enamorados.


    elif a % 2 != 0 and b % 2 == 0:
        return True
#a % 2 != 0 verifica si a es impar (un número es impar si al dividirlo entre 2 el residuo no es 0).
#b % 2 == 0 verifica si b es par.
#Si a es impar y b es par, la función retorna True, es decir, están enamorados.

    elif a % 2 == 0 and b % 2 != 0:
        return True

# -------------------------------
#2 reloj (algoritmo)
# -------------------------------

#paso de crear las variables, a lo cual empezando de cero creo debería quedar así;
h=00
m=00
s=00

#después debería de crear el array con esas variables agrupadas y sus limites en el mismo orden.

tipos=[h,m,s];
limite=[24,60,60]; 

#hora se crea la función

class inicializarContador(type, limite):
	if (type == limite):
		type = 0 
          
# -------------------------------
#3 En esta sencilla tarea se te da un número y tienes que convertirlo en negativo. Pero, ¿quizás el número ya sea negativo?
# -------------------------------

def make_negative(number):
    return -abs(number)

#otra solucion

def make_negative(number):
    if number < 0:
        return number
    else:
        return number * -1

# Ejemplo de uso
print(make_negative(5))  # Output: -5
print(make_negative(-3)) # Output: -3

# -------------------------------
#4 Crea una función que tome un número entero como argumento y regrese "Even"para números pares o "Odd"para números impares.
# -------------------------------

def even_or_odd(number):  #primero crear la funcion
  if number % 2 == 0:     # si el numero es par colocar evene 
    return "Even"          # y retomar even 
  else:                   # de lo contrario 
    return "Odd"          # Odd

# -------------------------------    
# 6 Este código no se ejecuta correctamente. Intenta averiguar por qué.
# -------------------------------

def multiply(a, b):
  return a * b

# -------------------------------
# 7 Obtienes una matriz de números y devuelves la suma de todos los positivos.
# -------------------------------

def positive_sum(arr):       # esto se utiliza cuando no se que ay adentro 
    sum = 0                  #variable para sumar
    for number in arr:       #para numero en arr 
        if number > 0:        # si numero es mayor que 0 
            sum = sum + number    #sumar numero y creo otra variable para que lo guarde en suma
    return sum                # retomamos lo guardado en suma 

# -------------------------------
#8 Completa la solución para que invierta la cadena que se le pasa.
# -------------------------------

def solution(string):
    invertir = ""
    for letra in string:                  #juan
        invertir = letra + invertir       #lo que hace es 1 letra j guarda
    return invertir                       #2 letra u + j
                                          #3 letra a + guardado uj
 
#la otra solucion puede ser 

def invertir_cadena(cadena):
    return cadena[::-1]

# -------------------------------
#9 Necesitamos una función que pueda transformar un número (entero) en una cadena.
# -------------------------------

def number_to_string(num):
    return str(num)   #str string


# -------------------------------
#10 Complete el método que toma un valor booleano y devuelve una "Yes"cadena para true, o una "No"cadena para false.
# -------------------------------

def bool_to_word(bool):      ##1 crear una funcion que reciva una variable bolean
#2 saber si adentro del boolean trae un true
    if bool == True:
        return 'Yes'  #3 retomar un yes cuando traiga un true adentro
    else:              #4 sino trae un true retornar no
        return 'No'
    
#Muy simple, dado un número (entero / decimal / ambos dependiendo del idioma), encuentra su opuesto (inverso aditivo).
def opposite(number):          
        return number * -1

#Es bastante sencillo. Tu objetivo es crear una función que elimine el primer y el último carácter de una cadena. Se te proporciona un parámetro, la cadena original. No tienes que preocuparte por cadenas con menos de dos caracteres.
def remove_char(s):
    return s[1:-1]

# -------------------------------
#11 Complete la función suma al cuadrado para que eleve al cuadrado cada número que se le pase y luego sume los resultados.
# -------------------------------

def elevar_numero(numeros):
    return sum(x * 2 for x in numeros) # suma y para elevar x utilisa 2 **   y for(para) x in (en) numeros

# -------------------------------
# 12 Escriba un programa que encuentre la suma de todos los números del 1 al num. El número siempre será un entero positivo mayor que 0. Su función solo necesita devolver el resultado. Lo que se muestra entre paréntesis en el ejemplo a continuación es cómo se llega a ese resultado y no es parte de él. Vea las pruebas de muestra.
#Por ejemplo (Entrada -> Salida) :
#8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)  #lista
# -------------------------------


def summation(num):
    return num*(num+1)//2  

#metodo dos 
def summation(num):
    resultado = 0
    for s in range(1, num + 1):  #Si s = 5, los números que generará el rango serán 1, 2, 3, 4 y 5.
          resultado += s   #suma todo esos numero y += lo guarda de una vez en la variable 
    return resultado  

# -------------------------------
#15 multiplicar los numeros pero solo los pares no los impares en un rango de 10
# -------------------------------

numeros = []
for i in range(1,11): #rango de 1 hasta 10 si es par
    if i % 2 == 0:  #PAR
        numeros.append(i*2) #agrega el numero (i) y lo multiplica x2

# -------------------------------
#13 eliminar los espacios de la cadena 
# -------------------------------

def no_espacios(x):
    espacio= x.replace(" ","")
    return espacio

# -------------------------------
#14 Considere una matriz/lista de ovejas en la que puede faltar alguna oveja en su lugar. Necesitamos una función que cuente la cantidad de ovejas presentes en la matriz (verdadero significa presente).
# -------------------------------

def count_sheeps(sheep):
    contador = 0  # Inicializa el contador en 0
    for s in sheep:  # Recorre cada elemento de la lista
        if s == True:  # Verifica si el elemento es True
            contador += 1  # Incrementa el contador si la condición es verdadera
    return contador  # Devuelve el total de elementos True

# -------------------------------
#15 Necesitamos una función que pueda transformar una cadena en un número. ¿Qué formas de lograrlo conoces?
#Nota: No te preocupes, todas las entradas serán cadenas y cada cadena es una representación perfectamente válida de un número integral.  #lista
# -------------------------------


def string_to_number(s):
    return int(s)
# -------------------------------
#16 Escriba una función para convertir un nombre en iniciales. Esta función acepta estrictamente dos palabras con un espacio entre ellas. #lista
#El resultado debe ser dos letras mayúsculas con un punto que las separa.
#Debería verse así:
#Sam Harris=>S.H
# -------------------------------

def convertir_a_iniciales(nombre):
    # Dividir el nombre en dos palabras
    palabras = nombre.split()
    # Obtener la primera letra de cada palabra y convertirla en mayúscula
    iniciales = palabras[0][0].upper() + '.' + palabras[1][0].upper() 
                                       #se une
    return iniciales

# Ejemplos de uso
palabras = ["Sam", "Harris"]
#palabras[0][0].upper() = "S"
#palabras[1][0].upper() = "H"}

# -------------------------------
#16 Tarea Dado un año, devuelve el siglo en el que se encuentra.
# -------------------------------

1705 = 18 #siglo 18

def century(year):
    siglo = year // 100 #para ayar el siglo lo divido por 100 
    if year % 100 != 0: #si da diferente a 0 es porque pertenece al otro siglo
        siglo += 1  #se le suma +1 que es el siguente siglo  
    return siglo

# -------------------------------
#17 Como Nathan sabe que es importante mantenerse hidratado, bebe 0,5 litros de agua por cada hora de ciclismo.
#Te dan el tiempo en horas y debes devolver la cantidad de litros que beberá Nathan,
#redondeado al valor más pequeño.
# -------------------------------

def litres(time):
    return int(time * 0.5)
#analisis para resolverlo 
#1 hora = 0.5 litros
#tiempo 1 =  horas 1 = 0.5 tomo agua en litros 
#redondear valor mas pequeño = int

#18 Dado un número aleatorio no negativo, debes devolver los dígitos de este número dentro de un str en orden inverso y volverlo entero

def digitize(numero):
    return [int(x) for x in str(numero)[::-1]] 
#lo convierte en entero pasa numero por numero en (str)Numero y lo invierte con [::-1]
#int(digito) convierte cada carácter (como '3', '5') de nuevo a un número entero.

# -------------------------------
#19 Cree una función que devuelva una declaración de saludo que utilice una entrada; su programa debería devolver, 
# "Hello, <name> how are you doing today?".
# -------------------------------

def greet(name):
    return f'Hello, {name} how are you doing today?'

# -------------------------------
#20 ¿Puedes encontrar la aguja en el pajar?
# Escribe una función findNeedle()que tome un arrayconjunto de basura pero que contenga uno"needle"
# Después de que su función encuentre la aguja, debería devolver un mensaje (como una cadena) que diga:
# "found the needle at position "Además indexencontró la aguja, así que:
# -------------------------------

def find_needle(haystack):  
    posicion = haystack.index("needle")  #index y la palabra que quiero buscar que es needle
    return f"found the needle at position {posicion}" #retorna la posicion -

# -------------------------------
#21  tarea es preparar un código simple para evaluar o encontrar el tiempo final de un periodo de tiempo dado, 
# expresándolo en horas y minutos. La hora de inicio se da como un par de horas (0..23) y minutos (0..59). 
# El resultado debe ser mostrado en la consola.
# -------------------------------

horas = int(input("Hora de inicio (horas): "))
minutos = int(input("Minuto de inicio (minutos): "))
duracion = int(input("Duración del evento (minutos): "))
minutos = minutos + duracion # encuentra el número total de minutos
horas = horas + minutos // 60 # encuentra el número de horas ocultas en los minutos y actualiza las horas
minutos = minutos % 60 # corrige los minutos para que estén en un rango de (0..59)
horas = horas % 24 # corrige las horas para que estén en un rango de (0..23) 
print(horas, ":", minutos, sep='')

# -------------------------------
#22 si el ingreso del ciudadano no era superior a 85,528 pesos, el impuesto era igual al 18% del ingreso menos 556 pesos y 2 centavos (esta fue la llamada exención fiscal).
#si el ingreso era superior a esta cantidad, el impuesto era igual a 14,839 pesos y 2 centavos, más el 32% del excedente sobre 85,528 pesos.
#Tu tarea es escribir una calculadora de impuestos.
# -------------------------------

ingresos = float(input("Introduce el ingreso anual: "))

if ingresos < 85528:
	inpuestos = ingresos * 0.18 - 556.02 #que se paga el 18% del ingreso, pero con una resta defija de 556.02 pesos.
else:
	inpuestos = (ingresos - 85528) * 0.32 + 14839.02 #se paga un monto fijo de 14,839.02 pesos, más el 32% y ongreso le resta  sobre 85,528.

if inpuestos < 0.0:
	inpuestos = 0.0

inpuestos = round(inpuestos, 0)
print("El impuesto es:", inpuestos, "pesos")

 # -------------------------------
#23 si el número del año no es divisible entre cuatro, es un año común.
#de lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
#de lo contrario, si el número del año no es divisible entre 400, es un año común.
#de lo contrario, es un año bisiesto.
# -------------------------------

year = int(input("Introduce un año: "))  # Pide al usuario que introduzca un año y lo convierte a entero.

if year < 1582:  # Comprueba si el año es menor a 1582.
    print("No está dentro del período del calendario Gregoriano")  
    # Imprime un mensaje indicando que el año no pertenece al calendario gregoriano.
else:  # Si el año es 1582 o mayor, verifica si es bisiesto o común.
    if year % 4 != 0:  # Comprueba si el año no es divisible entre 4.
        print("Año Común")  # Si no es divisible entre 4, es un año común.
    elif year % 100 != 0:  # Comprueba si el año no es divisible entre 100.
        print("Año Bisiesto")  # Si no es divisible entre 100, es un año bisiesto.
    elif year % 400 != 0:  # Comprueba si el año no es divisible entre 400.
        print("Año Común")  # Si no es divisible entre 400, es un año común.
    else:  # Si ninguna de las condiciones anteriores se cumple, el año es bisiesto.
        print("Año Bisiesto")

# -------------------------------
#24Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores,  
#y generar la altura de la pirámide que se puede construir utilizando estos bloques.
#Nota: La altura se mide por el número de capas completas - si los constructores no tienen la 
#cantidad suficiente de bloques y no pueden completar la siguiente capa, terminan su trabajo inmediatamente.
#Prueba tu código con los datos que hemos proporcionado.
# -------------------------------

bloques = int(input("Ingresa la cantidad de bloques: "))

# Inicializamos la altura de la pirámide y los bloques necesarios para la siguiente capa
altura = 0
bloques_necesarios = 1

# Mientras haya bloques suficientes para construir la siguiente capa
while bloques >= bloques_necesarios:
    bloques -= bloques_necesarios  # Resta los bloques usados
    altura += 1  # Incrementa la altura de la pirámide (una capa más)
    bloques_necesarios += 1  # La siguiente capa requiere más bloques 

# Imprime la altura máxima alcanzada
print("La altura de la pirámide es:", altura) #ejemplo si ingresa 20 bloques la altura es 5


# -------------------------------
#25 En 1937, un matemático alemán llamado Lothar Collatz formuló una hipótesis intrigante (aún no se ha comprobado) que se puede describir de la siguiente manera #lista
#toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0;
#si es par, evalúa un nuevo c0 como c0 ÷ 2;
#de lo contrario, si es impar, evalúe un nuevo  c0  como 3 × c0 + 1;
#si c0 ≠ 1, salta al punto 2.
# -------------------------------

c0 = int(input("Ingresa un número entero: "))

# Asegúrate de que el número sea positivo y no cero
if c0 <= 0:
    print("Por favor ingresa un número entero positivo que no sea cero.")
else:
    while c0 != 1:  # El bucle continuará hasta que c0 sea igual a 1
        if c0 % 2 == 0:  # Si c0 es par
            c0 //= 2  # Divide c0 entre 2
            print("Nuevo valor de c0 (par):", c0)
        else:  # Si c0 es impar
            c0 = 3 * c0 + 1  # Aplica 3 * c0 + 1
            print("Nuevo valor de c0 (impar):", c0)
    
    print("El proceso ha terminado, c0 es igual a 1.")


hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

# -------------------------------
#26 listas
# -------------------------------

# Paso 1: escribe una línea de código que solicite al usuario
hant_list = input("ingrese 5 numeros").split()
hant_list = [int(num) for num in hant_list]
# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
hant_list.pop
# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print(len(hant_list))
#imprime todo
print(hat_list)

# -------------------------------
#27 listas
# -------------------------------

# Paso 1: Crear lista vacía
beatles = [] 
print("Paso 1:", beatles)

# Paso 2: Agregar a los primeros miembros
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)

# Paso 3: Pedir al usuario que agregue los siguientes miembros
for _ in range(2):
    member = input("Agrega un miembro de la banda (Stu Sutcliffe o Pete Best): ")
    beatles.append(member)
print("Paso 3:", beatles)

# Paso 4: Eliminar a Stu Sutcliffe y Pete Best
beatles.remove("Stu Sutcliffe")
beatles.remove("Pete Best")
print("Paso 4:", beatles)

# Paso 5: Agregar a Ringo Starr al principio de la lista
beatles.insert(0, "Ringo Starr")
print("Paso 5:", beatles)

# Longitud de la lista
print("La longitud de la lista es:", len(beatles))

# -------------------------------
#28 ordenar lista en forma interactivo  #lista
# -------------------------------

#facil utilizando sort
my_lista = []  
numero = int(input("¿Cuántos elementos deseas ordenar?: "))

for i in range(numero):  # Rango limitado al número de elementos ingresados
    value = float(input("Ingresa un elemento de la lista: "))  # Leer un número
    my_lista.append(value)  # Agregar el número a la lista

my_lista.sort() # Ordenar la lista de forma ascendente

#dificil sin utilizar sort

my_lista = [8, 10, 6, 2, 4]  # lista a ordenar
swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.
numero = int(input("¿Cuántos elementos deseas ordenar?: "))

for i in range(numero): #rango que no se pase del numero
    value = float(input("Ingresa un elemento de la lista: "))
    my_lista.append(value) #agrega numero

while swapped:
    swapped = False  # no hay intercambios hasta ahora
    for i in range(len(my_lista) - 1):  # Recorremos la lista hasta el penúltimo elemento
        if my_lista[i] > my_lista[i + 1]:  # Si el elemento actual es mayor que el siguiente...
            swapped = True  # Entonces hay que intercambiar.
            my_lista[i], my_lista[i + 1] = my_lista[i + 1], my_lista[i]  # Intercambiamos los elementos para ordenarlos en orden ascendente
print("\nOrdenada:")
print(my_lista)

#consola si fuera 10,8,2,4,6
# Comparar 2 y 4 → No se intercambian.
#Comparar 4 y 6 → No se intercambian.
#Comparar 6 y 8 → No se intercambian.
#Comparar 8 y 10 → No se intercambian. resultado [2, 4, 6, 8, 10]

# -------------------------------
#29 encontrar un numero dentro de una lista 
# -------------------------------

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False #comienza con false cuando lo encuentre se cambia a true 
 
for i in range(len(my_list)):  # Recorre cada índice de la lista
    found = my_list[i] == to_find  # Compara el elemento actual con el valor a encontrar
    if found:  # Si lo encuentra
        break  # Sale del bucle de inmediato

if found:  # Si se encontró el elemento
    print("Elemento encontrado en el índice", i)
else:  # Si no se encontró
    print("ausente")

# -------------------------------
#30 TIENES QUE ELIMINAR LOS DUPLICADOS Y GUARDARLOS EN UNA LISTA  #lista
# -------------------------------

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
guardado = []

for i in my_list:
    if i not in guardado:  # Comprobamos si el elemento no ha sido agregado ya a 'guardado'
        guardado.append(i)

print("La lista con elementos únicos:")
print(guardado)

# -------------------------------
#31 Ahora encuentra la temperatura más alta durante todo el mes - analiza el código:
# -------------------------------


#Se crea una matriz (lista de listas) de 31 días, cada uno con 24 horas.
temperatura = [[0.0 for h in range(24)] for d in range(31)] # Aquí se supone que la matriz se actualiza con temperaturas reales.
# (Ejemplo: temps[0][12] = 30.5 asignaría 30.5°C al día 1 a las 12 PM)

# para asegurarnos de que cualquier temperatura real lo supere.
valor_temperatura = -100.0 # Inicializamos la variable temperatura con un valor muy bajo (-100.0)
#
for day in temperatura:  #Recorremos cada día en la matriz 'temperatura'
    for day in temperatura: #    # Recorremos cada temperatura en el día actual

        # actualizamos la variable 'highest'
        if temperatura > valor_temperatura: # Si encontramos una temperatura más alta que la registrada hasta ahora,
            valor_temperatura = temperatura     # actualizamos la variable 

# Finalmente, imprimimos la temperatura más alta encontrada en la matriz.
print("La temperatura más alta fue:", valor_temperatura)

# -------------------------------
#32 habitacion ocupado o desocupado sistema
# -------------------------------

#False equivale a 0 → Habitación desocupada. True equivale a 1 → Habitación ocupada (reservada).
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
#rooms     [edificios]                  [pisos]             [habitacion] 

rooms[1][9][13] = True  # Reservar habitación 14 en el piso 10 del edificio 2
rooms[0][4][1] = False  # Liberar habitación 2 en el piso 5 del edificio 1

disponible = 0
 
for room_number in range(20):  #verifica si esta ocupado o no
    if not rooms[2][14][room_number]: # Si la habitación está desocupada
#2 = Edificio 3 (porque los índices empiezan en 0).
#14 = Piso 15.
        disponible += 1 # Aumentar el contador

# -------------------------------
#33 Cubo - un arreglo tridimensional (3x3x3)
# -------------------------------

cube = [
    [  # z Cubo 0 (primer nivel)
        [':(', 'x', 'x'],  # y Fila 0
        [':)', 'x', 'x'],  # y Fila 1
        [':(', 'x', 'x']   # y Fila 2
    ],
    [  # z Cubo 1 (segundo nivel)
        [':)', 'x', 'x'],  #y  Fila 0
        [':(', 'x', 'x'],  #y  Fila 1
        [':)', 'x', 'x']   #y  Fila 2
    ],
    [  # z Cubo 2 (tercer nivel)
        [':(', 'x', 'x'],  #y  Fila 0
        [':)', 'x', 'x'],  #y Fila 1
        [':)', 'x', 'x']   #y  Fila 2
    ]
]
cube[z][y][x]
#z → Cubo (nivel/altura)
#y → Fila (posición en la matriz)
#x → Columna (elemento en la fila)

print(cube)
print(cube[0][0][0])  # output: ':('
print(cube[2][2][0])  # output: ':)'

# -------------------------------
#34 Números primos - cómo encontrarlos
# -------------------------------

def is_prime(num):
    for i in range(2, int(1 + num ** 0.5)):   # Iteramos desde 2 y numero lo multiplica por 0.5 para  verificar si un número es primo.
        if num % i == 0: # Si num es divisible por i, no es primo
            return False #retorna falso
    return True  #true Si no encontró divisores, (es primo)

# Recorremos números del 1 al 19
for i in range(1, 20):
    # Verificamos si (i + 1) es un número primo reccoriendo los valores de 1 al 19
    if is_prime(i + 1):
        print(i + 1, end=" ")  # Imprimimos en la misma línea
print()  # Nueva línea al final

# -------------------------------
#35 calcular el promedio de los estudiantes utilizando dic
# -------------------------------

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
    

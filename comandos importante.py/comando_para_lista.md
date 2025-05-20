`Listas (list)`	Mutable `[1, 2, 3]`  **mutable se puede modificar**
`Tuplas (tuple)`	Inmutable  `(1, 2.0, "cadena", [3, 4], (5, ), True)` **inmutable no se puede modificar**
`Diccionarios (dict)`	Mutable `({clave}, Valor: {valor}")`
`Conjuntos (set)`	Mutable    `{1, 2, 3}`
`Cadenas (str)`	Inmutable   `("Hola" "1" "2")`
`Enteros (int)`	Inmutable    `(1,2,3,4)`
`Flotantes (float)`	Inmutable  `(1,5 1,6 2,5)`
`Booleanos (bool)`	Inmutable   `(True - False)`

del vals[1]
**lista[comienzo:final]**  #para recorrer desde 1 y reccorer -1 hasta el ultimo sin incluir el ultimo si no el penultimo #ejemplo [2,3,4,5,6] 
**lista[1:-1]**   = 3,4,5 ** no incluyeel 6 si no el penultimo **lista[:3]** = 2,3,4 **list[3:]** = 5,6 **my_list[-2: ]** = 5,6
**for i in range(2, int(1 +`num ** 0.5`)):**  Iteramos desde 2 y numero lo multiplica por 0.5 para verificar si es numero primo con num ** 0.5
return **`number * -1`**   # encuentra el opuesto del numero si es positivo lo convierte en negativo
return **`min (lista)`**      #min es una función  que se utiliza para encontrar el valor más pequeño 
return **`cadena[::-1]`**   #invierte una cadena y si es numero seria con return for digito in str(n)[::-1]
espacio = **`variable.replace(" ","")`**   #para quitar los espacios de una cadena de principio a final

variable`in`list **verifica si un elemento dado (el argumento izquierdo) está actualmente almacenado en algún lugar dentro de la lista ej: print(5 in my_list)= false o true**
variable`not in`list  **comprueba si un elemento dado (el argumento izquierdo) está ausente en una lista** 

numeros = list(map(`int`, lista))   **int Convierte cada elemento de la lista a entero**
`str`(variable)        **str para pasar cualquier valor en un string (cadena)**
print (`zip`(nombre1,nombre2))  **zip une las dos listas**
variable.`add`(palabra)   **add agrega elemento con add**
`len`(variable)         **len sabe la longitud con len**
name`.split`()   **split separar la cadena de texto en una lista de palabras usando el espacio Por ejemplo"Sam Harris" se convierte en ["Sam","Harris"]**
variable`.upper`()      **upper es usado para convertir todos los caracteres de una cadena de texto (string) a mayusculas**
variable`.remove`(palabra)  **remove quita/eliminar la palabra con remove** 
del nums[1:3]   **Elimina los elementos en posiciones 1 y 2 ejemplo nums=[1, 2, 3, 4, 5] elimina el 2 y 3**
variable`.index`("nombre")  **index busca e la variable el nombre**
variable`.clear` ()     **clear elimina todo** 
variable`.append()`:    **Agrega un elemento a una lista.**
variable`.extend()`:    **Agrega varios elementos a una lista.**
variable`.insert(A, B):  **Inserta un elemento en una posición específica.** A = posicion(ULTIMA SI NO COLOCA A) B= numero o letra`
variable`.pop()`:     **Eliminar el último elemento de la lista.**
variable`.sort()`:    **Ordena los elementos de una lista ya sea palabra o letra.**
variable`.reverse()`: **Invierte el orden de los elementos de una lista.**
`join(variable)`:    **Une los elementos de una lista en una cadena de texto.**
variable`.strip()`: **Elimina los espacios al principio y al final de una cadena.**
variable`find()`:    **Busca una subcadena y devuelve su índice.**
variable`replace()`:   **Reemplaza una subcadena con otra en una cadena de texto.**
`sorted`(numeros) **se utiliza para ordenar de forma menor a mayor (1,2,3)(a,b,c)**
cadena.`lowerd()`   **para convertirlo en minusculas todas**
`time.sleep(1)`  **tiempo de espera ejemplo 1 segundo ejemplo en rangos**
`input`("ingrese 5 numeros") **ingresar solicitud del usuario**

# ejempl o de unir todos los conjuntos para eliminar duplicados
new_set = countries.`union`(northAm,centralAm,southAm)
# Mostrar el resultado
print(new_set)

 **map aplica la función int a cada elemento de la secuencia (en este caso, cada carácter de la cadena invertida) para convertir**
`map(int, ...)`       #cada carácter a un número entero. Por ejemplo, '3' se convierte en 3.

` dic.item  #items()`   **.items() devuelve una lista de tuplas (clave, valor) del diccionario. ejemplo** 
`for clave, valor in mi_dict.items():`  **// print(f"Clave: {clave}, Valor: {valor}")**
`dic.update(item)`  ** un diccionario agrega sus claves y valores al diccionario que lo llama, sobrescribiendo los valores de las claves que ya existen
```python
#ejercicio 1

# Paso 1: escribe una línea de código que solicite al usuario
hant_list = input("ingrese 5 numeros").split()
hant_list = [int(num) for num in hant_list]

# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
hant_list.pop

# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print(len(hant_list))

#ejercicio 2 agregar numeros o cosas 
my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.append(i + 1)

print(my_list)

#ejercicio 3 ordenamiento

my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)

#ejercicio 4 de

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




# ejemplos 
# Creación de listas
lista_vacia = []
lista_numeros = [1, 2, 3, 4, 5]
lista_mixta = [1, "dos", 3.0, True]

print("Lista vacía:", lista_vacia)
print("Lista de números:", lista_numeros)
print("Lista mixta:", lista_mixta)

# Acceder a elementos

print("Primer elemento:", lista_numeros[0])
print("Último elemento:", lista_numeros[-1])

# Modificar elementos

print("\nModificar elementos")

lista_numeros[0] = 10

#Agregar y eliminar elementos"

lista_numeros.append(6)  #append agregar lista 


#Lista después de append:", lista_numeros

lista_numeros.insert(2, 99)

#remover numero

lista_numeros.remove(99)

"elemento eliminado con pop()"

ultimo = lista_numeros.pop()  

#eliminado con pop 1

elemento = lista_numeros.pop(1)



# Operaciones básicas

print("\nOperaciones básicas")
lista_concatenada = lista_numeros + lista_mixta
print("Lista concatenada:", lista_concatenada)
lista_repetida = lista_numeros * 2
print("Lista repetida:", lista_repetida)
print("¿Está 3 en la lista?", 3 in lista_numeros)
print("Longitud de la lista:", len(lista_numeros))

# Iteración sobre los elementos de una lista


print("\nIteración sobre elementos de la lista")
for elemento in lista_numeros:
    print(elemento)

# Salida final

print("\nGracias por utilizar el programa de listas. ¡Hasta la próxima!")

#ejemplo

lista_mixta = [1, "dos", 3.0, True]
print(lista_mixta)
# Acceder a elementos
print("\nAcceso a elementos")
print("Primer elemento:", lista_mixta[0])
print("Segundo elemento:", lista_mixta[1])
print("tercer elemento:", lista_mixta[2])
print("cuarto elemento:", lista_mixta[3])

# Lista de dos dimensiones

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz:")
for bloque in matriz:
    for elemento in bloque:
        print(elemento, end=' ')
    print()

print(type(matriz))                   #para saver si es lista o tupla


# Lista de tres dimensiones

tensor = [
    [   
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
]

print("Tensor")
for bloque in tensor:           #para bloque en tensor 
    for fila in bloque:              #para fila en bloque 
        for elemento in fila:          #para elemento en fila 
            print(elemento, end=' ')       #imprimir elemento hasta el final
        print()
    print()

print(type(tensor))             #para saver si es lista o tupla


# Tuplas


tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

print("¿Está 3 en la tupla1?", 3 in tupla1)
print("Longitud de tupla1:", len(tupla1))

tupla_repetida = tupla1 * 2
print("Tupla repetida:", tupla_repetida)

print("Elementos de tupla1:")
for elemento in tupla1:
    print(elemento)

print(type(tupla1))   #para saver si es lista o tupla
mod
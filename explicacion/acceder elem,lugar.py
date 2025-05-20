my_list = [1, 2, 3, 4]
print(my_list[-3:-2]) #el outp es 2

#ejemplo 
tup = (1, 2, 4, 8)
tup = tup[1:-1] # 2,4
tup = tup[0]  #2
print(tup) #outp 2

#ejemplo del cubo 
#z → Cubo (nivel/altura)
#y → Fila (posición en la matriz)
#x → Columna (elemento en la fila)


cube = [
    [  # Cubo 0 (primer nivel)
        [':(', 'x', 'x'],  # Fila 0
        [':)', 'x', 'x'],  # Fila 1
        [':(', 'x', 'x']   # Fila 2
    ],
    [  # Cubo 1 (segundo nivel)
        [':)', 'x', 'x'],  # Fila 0
        [':(', 'x', 'x'],  # Fila 1
        [':)', 'x', 'x']   # Fila 2
    ],
    [  # Cubo 2 (tercer nivel)
        [':(', 'x', 'x'],  # Fila 0
        [':)', 'x', 'x'],  # Fila 1
        [':)', 'x', 'x']   # Fila 2
    ]
]

cube[z][y][x]
print(cube[0][0][0])  # output: ':('
print(cube[2][2][0])  # output: ':)'

#2 ejercicio

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


#**lista[comienzo:final]**  #para recorrer desde 1 y reccorer -1 hasta el ultimo sin incluir el ultimo si no el penultimo #ejemplo [2,3,4,5,6] 
#**lista[1:-1]**   = 3,4,5 ** no incluyeel 6 si no el penultimo **lista[:3]** = 2,3,4 **list[3:]** = 5,6 **my_list[-2: ]** = 5,6


# 3. Asignación de lista y eliminación de elementos
vehicles_one = ['coche', 'bicicleta', 'motor']
print(vehicles_one)  # output: ['coche', 'bicicleta', 'motor']

vehicles_two = vehicles_one
del vehicles_one[0]  # Elimina 'coche'
print(vehicles_two)  # output: ['bicicleta', 'motor']  
# **Nota:** Al usar `vehicles_two = vehicles_one`, ambos apuntan a la misma lista.

# 4. Copiar toda o parte de una lista utilizando rebanadas (slicing)
colors = ['rojo', 'verde', 'naranja']

copy_whole_colors = colors[:]  # Copia la lista entera
copy_part_colors = colors[0:2]  # Copia parte de la lista
print(copy_whole_colors)  # output: ['rojo', 'verde', 'naranja']
print(copy_part_colors)  # output: ['rojo', 'verde']

# 5. Usar índices negativos para hacer rebanadas

sample_list = ["A", "B", "C", "D", "E"]
new_list = sample_list[2:-1]
print(new_list)  # output: ['C', 'D']

# 6. Rebanadas con parámetros start y end opcionales
my_list = [1, 2, 3, 4, 5]
slice_one = my_list[2:]  # Desde el índice 2 hasta el final
slice_two = my_list[:2]  # Desde el principio hasta el índice 1 (sin incluirlo)
slice_three = my_list[-2:]  # Los dos últimos elementos

print(slice_one)  # output: [3, 4, 5]
print(slice_two)  # output: [1, 2]
print(slice_three)  # output: [4, 5]

# 7. Eliminar rebanadas utilizando del

# Eliminar elementos específicos utilizando remove
my_list = [1, 2, 3, 4, 5]

# Eliminar los dos primeros elementos (1 y 2) utilizando remove
my_list.remove(1)  # Elimina el primer '1'
my_list.remove(2)  # Elimina el primer '2'
print(my_list)  # output: [3, 4, 5]

# 8. Verificar si un elemento está en la lista utilizando 'in' y 'not in'
my_list = ["A", "B", 1, 2]

print("A" in my_list)  # output: True
print("C" not in my_list)  # output: True
print(2 not in my_list)  # output: False


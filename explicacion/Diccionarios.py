my_dictionary = {
    key1: value1,
    key2: value2,
    key3: value3,
}

#ejemplo
pol_esp_dictionary = {
    "kwiat": "flor",
    "woda": "agua",
    "gleba": "tierra"
    }
 
item_1 = pol_esp_dictionary["gleba"] # Ejemplo 1
print(item_1) # salida: tierra
 
item_2 = pol_esp_dictionary.get("woda") # Ejemplo 2
print(item_2) # salida: agua

#ejemplo
pol_esp_dictionary = {
    "zamek": "castillo",
    "woda": "agua",
    "gleba": "tierra"
    }
 
pol_esp_dictionary["zamek"] = "cerradura"
item = pol_esp_dictionary["zamek"]
print(item) # salida: cerradura

#ejemplo
pol_esp_dictionary = {"kwiat": "flor"}
 
pol_esp_dictionary.update({"gleba": "tierra"})
print(pol_esp_dictionary) # salida: {'kwiat': 'flor', 'gleba': 'tierra'}
 
pol_esp_dictionary.popitem()
print(pol_esp_dictionary) # salida: {'kwiat': 'flor'}

#Si deseas examinar los elementos (claves y valores) del diccionario, puedes emplear el método items(), por ejemplo:
pol_esp_dictionary = {
    "zamek": "castillo",
    "woda": "agua",
    "gleba": "tierra"
}

# Recorremos el diccionario e imprimimos cada palabra en polaco y su traducción al español
for clave, valor in pol_esp_dictionary.items(): ## .items() devuelve una lista de tuplas (clave, valor) del diccionario
    print("Pol/Esp ->", clave, ":", valor)

#ejemplo

pol_esp_dictionary = {
    "zamek": "castillo",
    "woda": "agua",
    "gleba": "tierra"
    }
 
print(len(pol_esp_dictionary)) # salida: 3
del pol_esp_dictionary["zamek"] # eliminar un elemento
print(len(pol_esp_dictionary)) # salida: 2
 
pol_esp_dictionary.clear() # eliminar todos los elementos
print(len(pol_esp_dictionary)) # salida: 0
 
del pol_esp_dictionary # elimina el diccionario

#ejemplo 

dictionary = {}
my_list = ['a', 'b', 'c', 'd']
 
for i in range(len(my_list) - 1):
    dictionary[my_list[i]] = (my_list[i], )
 
for i in sorted(dictionary.keys()):
    k = dictionary[i]
    print(k[0]) #imprime a,b,c

#ejemplo

dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}

# Inicializar la variable 'v' con el valor correspondiente a la clave 'one'
v = dictionary['one']  # Esto asigna 'two' a v

# Bucle que itera sobre las claves del diccionario
for k in range(len(dictionary)):  # La longitud del diccionario es 3, por lo que se ejecuta 3 veces
    v = dictionary[v]  # En cada iteración, 'v' se actualiza con el valor de la clave 'v' en el diccionario


print(v) #oupt Two porque Empieza con 'two' (porque v = dictionary['one']).
#Luego va a 'three' (porque v = dictionary['two']).
#Luego va a 'one' (porque v = dictionary['three']).
# Configuración de una aplicación
config = {
    "host": "localhost",
    "port": 8080,
    "debug": True
}
print("Configuración:", config)

# Contador de palabras
palabras = ["manzana", "banana", "naranja", "manzana", "banana"]
contador = {}
for palabra in palabras:             #para la plabara en palabras 
    if palabra in contador:              #si palabra en contador 
        contador[palabra] += 1            #contar palabra y colocarle +1
    else:                           #de lo contrario dejarlo en 1
        contador[palabra] = 1 
print("Contador de palabras:", contador)

# Mapeo de usuarios a datos
usuarios = {
    "user123": {"nombre": "Juan", "edad": 30},
    "user456": {"nombre": "Ana", "edad": 25}
}
print("Datos de usuario user123:", usuarios["user123"])

# Almacenamiento de datos estructurados
libro = {
    "título": "Cien años de soledad",
    "autor": "Gabriel García Márquez",
    "año": 1967
}
print("Datos del libro:", libro)

# Datos en formato JSON
import json
json_data = json.dumps(libro)
print("Datos en JSON:", json_data)

#contactos ejemplo

contactos = {
    "Carla": {"apellido": "Florida", "altura": 1.7, "edad": 30},
    "Diego": {"apellido": "Antesana", "altura": 1.75, "edad": 32}
}
print(contactos["Diego"])



#ver como se costruye una clase con sus caracteristicas y funcionalidades para simular un objeto de la vida real 

class Lavadora:
    def __init__(self,altura,modelo,pais,marca):
        self.altura = altura
        self.modelo = modelo
        self.precio = 0
        self.pais = pais
        self.marca = marca
        self.disponible = True
    def lavar(self):
        print("estoy lavando")
    def secar(self):
        print("estoy secando")
    def elegir_opciones(self):
        print("estas eligiendo una opcion")
    def mostrar_precio(self):
        self.precio = self.altura * 5
        print(self.precio)

lavadora = Lavadora (1.43,"praint","colombia","lg")
print(lavadora.altura)
print(lavadora.precio)
lavadora.mostrar_precio()

#objetos caracteristicas y funcionalidades

class Avion:
    def __init__ (self,altura,modelo,pais,marca,precio):
        self.altura = altura
        self.modelo = modelo
        self.pais = pais
        self.marca = marca
        self.precio = precio
    def ensender_motor(self):
        print("el motor esta prendido")
    def apagar_motor(self):
        print("el motor esta apagado")
    def abrir_puerta(self):
        print("la puerta esta abierta")
    def cerrar_Puerta(self):
        print("la puerta esta cerrada")
    def mostrar_precio(self):
        print("1.35")
    
avion = Avion (1.35,"avianca","colombia","avia","500")
avion.mostrar_precio()
print(avion.altura)
print(avion.precio)


class Celular:
    def __init__(self,modelo,precio,marca,altura):
        self.modelo = modelo
        self.precio = precio
        self.marca = marca
        self.altura = altura
    def celular_prendido(self):
        print("el celular esta prendido")
    def celular_apagado(self):
        print("el celular esta apagado")
    def reiniciar_celular(self):
        print("el celular se esta reiniciando")
    def mostrar_precio(self):
        print("600")

celular = Celular ("lg",600,"lg","40")
celular.mostrar_precio()

marca = input("Elige una marca de celular: ")

if marca.lower() == "lg":
    print("Celular disponible")
else:
    print("Celular no disponible")


print(celular.precio)
print(celular.marca)


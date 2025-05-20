class Vehiculo:
    def __init__(self, modelo, precio):
        self.modelo = modelo
        self.precio = precio
        self.disponible = True

    def vender(self):
        if self.disponible:
            self.disponible = False
            print(f"El vehículo {self.modelo} ha sido vendido.")
        else:
            print(f"El vehículo {self.modelo} no está disponible.")

    def hacer_disponible(self):
        self.disponible = True
        print(f"El vehículo {self.modelo} está disponible para la venta nuevamente.")

class Cliente:
    def __init__(self, nombre, id_cliente):
        self.nombre = nombre
        self.id_cliente = id_cliente
        self.vehiculos_comprados = []

    def comprar_vehiculo(self, vehiculo):
        if vehiculo.disponible:
            vehiculo.vender()
            self.vehiculos_comprados.append(vehiculo)
        else:
            print(f"El vehículo {vehiculo.modelo} no está disponible.")

    def devolver_vehiculo(self, vehiculo, concesionario):
        if vehiculo in self.vehiculos_comprados:
            vehiculo.hacer_disponible()
            self.vehiculos_comprados.remove(vehiculo)
            concesionario.agregar_vehiculo(vehiculo)
        else:
            print(f"El vehículo {vehiculo.modelo} no está en la lista de comprados.")

class Concesionario:
    def __init__(self):
        self.vehiculos = []
        self.clientes = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        print(f"El vehículo {vehiculo.modelo} ha sido agregado al inventario.")

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"El cliente {cliente.nombre} ha sido registrado.")

    def mostrar_vehiculos_disponibles(self):
        print("Vehículos disponibles:")
        for vehiculo in self.vehiculos:
            if vehiculo.disponible:
                print(f"{vehiculo.modelo} por ${vehiculo.precio}")


#crear lista de carrros

concesionario = Concesionario()
concesionario.agregar_vehiculo(Vehiculo("gru","200"))
concesionario.registrar_cliente(Cliente("Pedro","2"))



# Crear concesionario
concesionario = Concesionario()
concesionario.agregar_vehiculo(vehiculo1)
concesionario.agregar_vehiculo(vehiculo2)
concesionario.registrar_cliente(cliente1)
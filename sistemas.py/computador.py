class Computadora:
     def __init__(self,modelo,precio):                     
           self.modelo = modelo
           self.precio = precio
           self.disponible = True

     def vender(self):
           if self.disponible:                        #si esta disponible
                 self.disponible = False                                #y es falso (no esta disponible)
                 print(f"la computadora{self.modelo} esta vendido")          #colocar que esta vendida
           else:
                 print(f"la computadora {self.modelo} no esta disponible")         #y no esta disponible
 
     def hacer_disponible(self):                          
           self.disponible = True                                    #si la opcion es verdadera
           print(f"la computadora {self.modelo} esta disponible")         #decir que esta disponible

class Cliente:                                       
      def __init__ (self, name, user_id):
            self.nombre = name
            self.usuario = user_id
            self.almacenados =[]

      def prestar_computadora(self,computadora):
          if computadora.disponible:         #si esta disponible
             computadora.borroow()        #cambiar al estado de prestado (borroow)
             self.almacenados.append(computadora)     #el la lista de almacenados agregar el computador prestado
          else:                              #de lo contrario
             print(f"el libro {self.modelo} no esta disponible")

      def delvolver_computadora(self,computadora): #para devolver computadora
            if computadora in self.prestar_computadora:    #si el computador esta en prestar computadora
               computadora.devolver_computadora()         #delvolver a computadora
               self.prestar_computadora.remove(computadora)      #eliminar en prestar computadora
            else:
                 print(f"no esta en la lista de los prestados  {self.modelo} ")   
class Almacenamiento:
     def __init__(self):
          self.computadora = []
          self.user= []

     def agregar_computadora(self,computadora):
         self.computadora.append(computadora)
         print(f"la computadora{computadora.title} ha sido agregada")

     def registrar_usuario(self, users):
          self.users.append(users)
          print(f"el usuario {users.name} ha sido registrado ")

     def computadores_disponibles(self):
          print("computadores disponibles:")
          for computadora in self.computadora:
               if computadora.available:
                    print(f"{computadora}")

#crear lista de computadores

almacenamiento = Almacenamiento()
almacenamiento.agregar_computadora(Computadora("Dragon","200"))
almacenamiento.registrar_usuario(Cliente("juan","5"))
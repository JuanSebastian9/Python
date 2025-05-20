#ejemplo de iterador que es

# permite al programador recorrer un contenedor, particularmente listas

#crear una lista

mi_lista = [1,2,3,4]

#obtener el iterador

mi_iter = iter(mi_lista)

#usar el iterador

print(next(mi_iter))   #cuales son los valores que se guardan en memoria con next
print(next(mi_iter))

#crear un iterador para un numero impar
#limite
limit = 10

odd_itter = iter(range(1,limit+1,2))  #literar cada dos numero

#usar el literador

for num in odd_itter:
    print(num)

#un generador es separar partes o cosas en paquetes 

#crear la funcion para definir mi generador
def mi_generador ():
    yield 1
    yield 2
    yield 3

for value in mi_generador():  #por cada valor que esta en mi generador
    print(value)               #imprimier los valores que va generando 

#ejemplo de generador

def fionacci (limit):
    a, b = 0, 1           #a y b es 0 y 1 
    while a< limit:       #si a es menor que el limite crear un generador
          yield a         #crear generado 
          a,b=b, a+b      #el nuevo valor de a es b y el nuevo valor de b es a+b

for num in fionacci(10):  #por cada numero que esta en fionacci queremos como limite a menor de 10
    print(num)            #imprimir el numero 

 #crear generado para ver los pares y impares

#impar 

limit = 30
dd_itter = iter(range(1,limit+1,2))  #literar cada dos numero
for lis in dd_itter:
    print(lis)


#pares

    limit = 30
dd_itter = iter(range(2,limit+1,2))  #literar cada dos numero
for lis in dd_itter:
    print(lis)
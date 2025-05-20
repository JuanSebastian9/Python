#ENTEROS FLOTANTES Y BOOLEANOS

float(num 1) + (num 2) #numero con decimales
int(num 1) + (num 2)  #numero entero 

x = 10                #(entero con el comando type para saber)
y = 5.678             #(punto flotante con el comando type para saber)
z = 1.2E6 
a = 1.2E-6            #(E es elevado)
print( type (x))
print( type (y))
print( z)             #(para que de el resultado se le quita type)
print( a)       
print( y + a )        #(sumas)
print( x + y )    

#falso o verdadero y el tipo con type

is_true = True
is_fase = False
print(is_true)
print( type(is_true))   

#Operaciones Matemáticas en Python

a = 10
b = 3
print("suma:", a + b)
print("resta:", a - b)
print("multiplicacion:", a * b)
print("division:", a / b)
print("modulo:", a % b)
print("parte entera de la division :", a // b)  
print("potenciacion:", a ** b)
a += + 2
print(a)
operation1 = 2 + 3 * 4         #este esta mal    
operation2 = 2 + (3 * 4)       #primero la multiplicacion y despues la suma
print(operation1)
print(operation2) 
operation3 = (2+3) * (4**2) / 8 - 1    #primero resuelve los () 
print( operation3)

#operaciones booleanos donde el resultado es true o  false 

a = 10
b = 3
print( a > b )      #mayor que b             true
print(a < b)        # a menor que b
print( a >= b )     #mayor o igual que b     true
print(a <= b )      #menor o igual que b     false
print( a == b )     #a igual que b           false
print(a != b )      #a diferente o no igual que b       true

#metodo slice

a = [1,2,3,4,5]
b = a
print(a)
print(b)
del a [0]
print(a)         
print(b)
print(id(a))    #para saber donde se esta almacenando esta informacion
print(id(b))
c = a [:]       #desde el pincipio hasta el final para quitar el problema de que no se vea en otra
print(id(a))    
print(id(b))   
print(id(c))
a.append (6)      #añadir 6 en el a
print(a )
print(b)  
print(c)          #solucionado no se repite 4 si no 3

#para volver negativo una operacion

def make_negative(number):
    return -abs(number)

# Ejemplo de uso

print(make_negative(5))  # imprime: -5
print(make_negative(-3)) # imprime: -3


#El rango (range) es un tipo especial de iterable que genera una secuencia de números. Puedes usarlo para 
# crear secuencias de números de manera rápida, sin tener que crear una lista manualmente. Por ejemplo, 
# si quieres sumar los números del 1 al 5:
for s in range(1, 6):  # Esto genera los números 1, 2, 3, 4, 5 
    print(i)
#en caso de que sea una lista seria 
 for s in range(1, numero + 1):  #pasa numero por numero con un rango de 1 y el +1 es para que incluya el ultimo numero

#poner numero negativo 

def make_negative( number ):
    if number < 0:      # menor que 0 
        return number
    else:                   #todo numero multiplicado x -1 da menos
        return number * -1
    
#poner numero positivo

def make_postivo( number ):
    if number > 0:      # mayor que 0 
        return number
    else:                   #todo numero multiplicado x -1 da mas
        return number * -1
    
    
# 7 Obtienes una matriz de números y devuelves la suma de todos los positivos.
# Obtienes una matriz de números y devuelves la suma de todos los positivos.

def positive_sum(arr):       # esto se utiliza cuando no se que ay adentro 
    sum = 0                  #variable para sumar
    for number in arr:       #para numero en arr 
        if number > 0:        # si numero es mayor que 0 
            sum = sum + number    #sumar numero y creo otra variable para que lo guarde en suma
    return sum                # retomamos lo guardado en suma 

#esta funcion recorre desde el numero 1 (osea el 2 porque el primero es 0)(para no contar el ultimo se pone -1 )

def remove_char(s):  #la s es un string (lista de letra)
    return s[#numero : #numero] 

#ejemplo
# Tu objetivo es crear una función que elimine el primer y el último carácter de una cadena. Se te proporciona un parámetro, la cadena original. No tienes que preocuparte por cadenas con menos de dos caracteres.

def remove_char(s):
    return s[1:-1] 

# funcion para suma
def suma(numero1, numero2):
  return numero1 + numero2
#para especificarle los numeros

#suma 
def suma(numero1, numero2):
  return numero1 + numero2

assert suma(5, 7) == 12

#multiplicacion 

def multiplicacion(numero1,numero2):
  return numero1 * numero2

assert multiplicacion(5, 2) == 10
assert multiplicacion(5, 5) == 25
assert multiplicacion(5, 8) == 40

#ejemplo para sumas solo numeros positivos 

def positive_sum(arr):       # esto se utiliza cuando no se que ay adentro 
    sum = 0                  #variable para sumar
    for number in arr:       #para numero en arr 
        if number > 0:        # si numero es mayor que 0 
            sum = sum + number    #sumar numero y creo otra variable para que lo guarde en suma
    return sum                # retomamos lo guardado en suma 
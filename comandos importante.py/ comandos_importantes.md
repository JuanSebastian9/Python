**`def(parametro)`**     #definir una funcion y dentro un parametro
**`while True`**    # ejecutará un bloque de código mientras la condición es verdadero
**`while`**           #estructura de control de flujo, concretamente lo que hace es repetir un código mientras dure una determinada condición. 
**`if`**            #estructura condicional
**`elif`**           #para escribir mas condiciones despues de if
**`else`**           #de lo contrario
**`for`**          #para
**`in`**            #en
**`else`**         #de lo contrario
**`return`**        #se utiliza dentro de una función para devolver un valor al lugar desde donde la función fue llamada 
**`input`**         #es usada para obtener datos de entrada del usuario, como texto o números  ejemplo valor = int(input("Ingresa un número: "))
**`f`**            #La f sirve para que dentro del string(almacenar secuencias) puedas poner variables. print(f"El resultado es {resultado}")
**`try`**           #para capturar posible error
**`ValueError`**   #lo utilizamos cuando queremos avisarle al usuario del programa que un dato o argumento que ingresó en la consola ha sido - incorrecto. 
**`except Exception as e:`** #se utiliza para captar otro error áparte de valueError
**`except ZeroDivisionError:`**        #se utiliza para capturar excepciones que ocurren cuando se intenta dividir un valor entre cero
**`append`**         #agregar lista o nombres
**`class`**          #proveen una forma de empaquetar datos y funcionalidad juntos
**`self`**          #el mismo se utiliza para dentro del def__init__(self) cualquier
**`__init__`**        #es un método especial que se usa para inicializar un nuevo objeto de una clase.
**`variable`**      #una variable es ejemplo nombre = "Juan" o es_estudiante = True o de una clase Class = clase
**`palabra = ""`**    #el caracter base es el vasio donde no ay nada  ejemplo  palabra = ""
**`assert`**          #verificar si lo que esta ejecutando que sea verdadero siempre si no es verdadero sale erro assert suma(5, 7) == 12 bien assert **`suma(6, 7) == 12 mal 13
**variable`in`list** verifica si un elemento dado (el argumento izquierdo) está actualmente almacenado en algún lugar dentro de la lista ej: print(5 in my_list) = false o true
**variable`not in`list** comprueba si un elemento dado (el argumento izquierdo) está ausente en una lista 


**`sum (x ** 2 for x in numeros)`**   #suma (esto sirve  para elevarlo  a la 2 pasando numero por numero)
**`return num*(num+1)//2`**  #suma de todos los números del 1 al num ejemplo 8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)
**`for s in range(1, numero + 1):`**   #Si numero  es 5, range(1, 5 + 1) generará la secuencia: `1, 2, 3, 4, 5`. 2. **`para s en

## en que ocasiones se utiliza los modulos % 
**1 par o impar usando modulo (lo que sobra)** 
`number % 2 == 0 o number % 2 == 1`**  # si el numero da 0 es par si da 1 es impar 
**2 Comprobar si es divisible (si se puede dividir o no)**
`if numero % divisor == 0:` #si da 0 es porque es divisible si da != 0 es porque no es divisible
**3 generar patrones o condiciones especificas**
for i in range(1, 11):
    if i % 3 == 0:
        print(f"{i} es múltiplo de 3")
**4 redondeo o agrupamientos**

```python
# un string es una union de caracteres como la a,e,f acambio un numero es un solo datos como un 1 o 2 o 3
# print("suma:", a + b)
# print("resta:", a - b)
# print("multiplicacion:", a * b)
# print("division:", a / b)
# print("modulo:", a % b)
# print("parte entera de la division :", a // b)  
# print("potenciacion:", a ** b)

# != en programación significa "distinto de" o "no igual a
# == : Igual a
# != : Diferente de
# < : Menor que
# > : Mayor que
# <= : Menor o igual que
# >= : Mayor o igual que
# = : Asignación simple

# += : Suma y asigna
# -= : Resta y asigna
# *= : Multiplica y asigna
# /= : Divide y asigna
# %= : Módulo y asigna
# **= : Exponente y asigna
# //= : División entera y asigna

#binarios

#&: Devuelve 1 solo cuando ambos bits son 1.
#|: Devuelve 1 si al menos uno de los bits es 1.
#~: Invierte todos los bits (es la negación a nivel de bits).
#^: Devuelve 1 solo cuando los bits en la misma posición son diferentes.
#>>: Desplaza los bits a la derecha (equivalente a dividir por 2).
#<<: Desplaza los bits a la izquierda (equivalente a multiplicar por 2).

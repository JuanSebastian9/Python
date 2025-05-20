def add(a,b):                   
    return a + b

def substract(a,b):
    return a - b

def multiply(a,b):                            #funcion con def
    return a * b

def divide(a,b):
    return a / b


def calculator():
    while True:                                       #repetir codigo mientras dure un determinado condicion
        print("Seleccione una operación")
        print("1. Suma")                                 #funcion con def de elegir 
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        option = input("Ingresa su opción (1,2,3,4,5):")              

        if option == "5":                                   #si oprime la funcion 5 le coloca salir calculadora
            print("Saliendo de la calculadora")
            break
        
        if option in ["1","2","3","4"]:                                     #si elije 1,2,3,4,5  poner un numero (float) (mensaje que es input)
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))

            if option == "1":                                            #si coloca 1 sumas num1,nume2
                print("La suma es:", add(num1,num2))                      
            elif option == "2":                                            #si coloca option 2 restar num1,num2
                print("La resta es:", substract(num1,num2))
            elif option == "3":
                print("La multiplicación es:", multiply(num1,num2))
            elif option == "4":
                print("La división es:", divide(num1,num2))   
        else:
            print("Opción no válida, por favor intenta de nuevo.")                       #de lo contrario poner no valido
calculator()

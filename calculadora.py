# Online Python - IDE, Editor, Compiler, Interpreter

def suma(total):
    if total== "NaN":
        num1 = int(input("Dime el primer numero a sumar: "))
        num2 = int(input("Dime el segundo numero a sumar: "))
        return num1+num2
    else :
        num2 = int(input("Dime el numero a sumar al total: "))
        print("El total ahora es: "+ str(total+num2))
        return total+num2

def resta(total):
    if total== "NaN":
        num1 = int(input("Dime el primer numero a restar: "))
        num2 = int(input("Dime el segundo numero a restar: "))
        return num1-num2
    else :
        num2 = int(input("Dime el numero a restar al total: "))
        print("El total ahora es: "+ str(total-num2))
        return total-num2
    
def multiplicar(total):
    if total== "NaN":
        num1 = int(input("Dime el primer numero a multiplicar: "))
        num2 = int(input("Dime el segundo numero a multiplicar: "))
        return num1*num2
    else :
        num2 = int(input("Dime el numero a multiplicar al total: "))
        print("El total ahora es: "+ str(total*num2))
        return total*num2
    
def dividir(total):
    if total== "NaN":
        num1 = int(input("Dime el primer numero a dividir: "))
        num2 = int(input("Dime el segundo numero a dividir: "))
        return num1/num2
    else :
        num2 = int(input("Dime el numero a dividir al total: "))
        print("El total ahora es: "+ str(total/num2))
        return total/num2
    
def operar(eleccion, total):
    if eleccion==1:
        return suma(total)
    elif eleccion==2:
        return resta(total)
    elif eleccion==3:
        return multiplicar(total)
    elif eleccion==4:
        return dividir(total)
    elif eleccion>=5:
        print("Opcion no valida, elige una opcion del 1 al 5")
        return total

#MAIN

total = "NaN"
eleccion = int(input("Bienvenido a la calculadora,elija una opcion (del 1 al 5):\n Opcion 1: Suma \n Opcion 2: Resta \n Opcion 3: Multiplicar \n Opcion 4: Division \n Opcion 5: Salir \n Elige que operacion realizar:"))
if(eleccion!=5):
    total=operar(eleccion, total)

while(eleccion<5 and total!="NaN"):
    eleccion = int(input("Opcion 1: Suma \n Opcion 2: Resta \n Opcion 3: Multiplicar \n Opcion 4: Division \n Opcion 5: Salir \n Elige que operacion realizar:"))
    total=operar(eleccion, total)

print("Gracias por usar la calculadora!")


"""
Def: En programación, una sentencia condicional es una instrucción o grupo de instrucciones 
que se pueden ejecutar o no en función del valor de una condición.
En python el orden de las condiciones son:

1. if
2. elif
    .
    .
    .
3. else
"""

#1. Si tenemos dos variables A = 200 y B = 100 podemos pedir a nuestro programa que si un numero es mayor imprima un mensaje en pantalla.
a = 200
b = 100
if a > b: #Pon atencion como usamos la condicional if y el operador >
    print("A es mayor que B")

#2. Si tenemos dos variables A y B podemos pedir a nuestro programa que si un numero es mayor imprima un mensaje en pantalla. Pero, si ese numero no cumple con la condicion, imprimir otro mensaje por pantalla.
a = int(input("Ingresa un numero: "))
b = int(input("Ingresa otro numero: "))
if a > b: #Podemos leer esta linea como: 'si A es mayor que B entonces...'
    print("A es mayor que B")
elif a < b: #Podemos leer esta linea como: 'si A es menor que B entonces...'
    print("A es menor que B")

#Si tenemos dos variables A  y B podemos pedir a nuestro programa que si un numero es mayor imprima un mensaje en pantalla. Pero, si ese numero no cumple con la condicion, imprimir otro mensaje por pantalla.
a = int(input("Ingresa un numero: "))
b = int(input("Ingresa otro numero: "))
if a > b: #Podemos leer esta linea como: 'si A es mayor que B entonces...'
    print("A es mayor que B")
elif a < b: #Podemos leer esta linea como: 'si A es menor que B entonces...'
    print("A es menor que B")
else:
    print("Ningun numero es mayor que el otro")
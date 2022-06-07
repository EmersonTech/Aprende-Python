"""
Def: En python, existen las operaciones matematicas que cumplen con las leyes de la aritmetica.
1.Partentesis ()
2.Potencias ** 
3.Multiplicacion * 
4.Division / ; // ; %
5.Adicion + 
6.Sustraccion - 
"""

#1. Sumar 2 variables. Una variable entera y otra decimal. Ambas deben ser > 0.
x = int(input("Ingresa un entero: "))
y = float(input("Ingresa un decimal: "))
suma = (x + y)
print(f"El resultado de la operacion es {suma}")

#2. Restar 3 variables. Ambas deben ser < 0 y pueden ser enteras o decimales.
a = eval(input("Ingresa un numero: "))
b = eval(input("Ingresa un numero: "))
c = eval(input("Ingresa un numero: "))
resta = (a - b - c)
print(resta)

#3. Multiplica 2 variables. Elige el tipo de dato que prefieras (int, float) y opera una multiplicacion.
# imprime su resultado por pantalla.
a = eval(input("Ingresa un numero: "))
b = eval(input("Ingresa un numero: "))
multiplicacion = (a * b)
print(multiplicacion)

#4. Crea una variable que almacene el valor de 2 y crea otra variable donde el usuario ingrese
# la potencia (el exponente) para que sea operado con el numero 2.
a = 2
b = int(input("Ingresa una potencia: "))
potencia = (a ** b)
print(f"El resultado de la potencia es {potencia}")

#4. Crea un programa que divida dos numeros ingresados por el usuario.
a = int(input("Ingresa un numero: "))
b = int(input("Ingresa un numero: "))
division = (a / b) # / Usado para dividir un numero
modulo = (a % b) # % Usado para obtener el residuo de una division
division_entera = (a // b) # Usado para obtener un resultado de tipo entero (int)

print(f"El resultado al dividir ambos numeros es {division}")
print(f"El residuo al dividir los numeros es {modulo}")
print(f"El resultado al dividir ambos numeros de forma entera es {division_entera}")

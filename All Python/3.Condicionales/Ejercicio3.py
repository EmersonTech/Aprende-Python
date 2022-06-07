"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
Pista: Para determinar si es par o no, se necesita una formula matematica en donde al realizar una division, el residuo debe ser = 0.
"""
# Pedir datos
num = eval(input("Ingresa un numero: "))

# Calcular los numeros
if num % 2 == 0:
    print("Es par")
else:
    print("No es par")  
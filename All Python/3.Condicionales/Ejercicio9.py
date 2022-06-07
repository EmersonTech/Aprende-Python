"""
Escribe un programa en donde el usuario ingrese 3 numeros enteros y determine
cual de ellos es mayor, mediano y menor respectivamente. Si el usuario ingresa
una secuencia erronea, ejemplo: 3, 3, 3. El programa debe mostrar un error

Solucion:
Recuerda que la formula matematica para determinar cuantas posibilidades
puedes combinar con 3 variables usamos la combiacion basica de factorial
Factorial -> 3x2x1 = 6 combinaciones posibles.

Combinaciones:
#1. 123
#2. 132
#.3 312
#.4 321
#.5 231
#.6 213

Al probar todas las combinaciones anteriores, tu programa debe ordenarlos
e imprimirlos por pantalla
"""
num1 = int(input("Ingresa el primer digito: "))
num2 = int(input("Ingresa el segundo digito: "))
num3 = int(input("Ingresa el tercer digito: "))

# Aqui usamos todas las combinaciones, dejando la variable num1 como la mayor
if num1 > num2 > num3:
    print(f"{num1} Es mayor, {num2} es mediano, {num3} es menor")
elif num1 > num3 > num2:
    print(f"{num1} Es mayor, {num3} es mediano, {num2} es menor")

# Aqui usamos todas las combinaciones, dejando la variable num2 como la mayor
elif num2 > num1 > num3:
    print(f"{num2} Es mayor, {num1} es mediano, {num3} es menor")
elif num2 > num3 > num1:
    print(f"{num2} Es mayor, {num3} es mediano, {num1} es menor")

# Aqui usamos todas las combinaciones, dejando la variable num3 como el mayor
elif num3 > num1 > num2:
    print(f"{num3} Es mayor, {num1} es mediano, {num2} es menor")
elif num3 > num2 > num1:
    print(f"{num3} Es mayor, {num2} es mediano, {num1} es menor")

# Si se ejecuta una secuencia erronea como: 3,3,3 nos
else:
    print("Error de digitos")
"""
Crea dos variables en donde el usuario ingrese numeros, luego imprime por pantalla
todas las operaciones aritmeticas que hemos visto: suma, resta, multiplicacion,
division, potencia, division entera. Ambos numeros deben ser >= 5. 
"""
# Ingreso de valores
num1 = eval(input("Ingresa un numero: "))
num2 = eval(input("Ingresa otro numero: "))

# Operaciones aritmeticas
suma = (num1 + num2)
resta = (num1 - num2)
multiplicacion = (num1 * num2)
potencia = (num1 ** num2)
division = (num1 / num2)
modulo = (num1 % num2)
division_entera = (num1 // num2)

# Salida de valores
print(f"Resultado: Suma {suma}, resta {resta}, multiplicacion {multiplicacion}, division {division}, potencia {potencia}, modulo {modulo}, division entera {division_entera}")
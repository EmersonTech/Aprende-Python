"""
Def: Un imput es la entrada de un valor, ya sea numerico (int), decimal (float), buleano (bool) o incluso cadena de texto (string).
Cada entrada sera almacenada dentro de una variable.
"""
#1. Crea una variable llamada 'entero' que a traves de un imput, almacene un numero entero, mayor que cero (>0). Debes incluir el mensaje
# 'Introduce un entero, mayor que cero: '. Luego imprime el resultado en pantalla, mostrando el tipo de dato.
entero = int(input("Introduce un entero, mayor que cero: "))
print(entero,type(entero))

#2. Crea una variable llamada 'decimal' que a traves de un imput almacene un decimal cualquiera, mayor que cero (>0). Debes incluir el
# mensaje 'Introduce un decimal, mayor que cero: '
decimal = float(input("Introduce un decimal, mayor que cero: "))
print(decimal,type(decimal))

#3. Crea una variable llamada 'cadena' que a traves de un imput almacene una cadena de texto cualquiera. Debes incluir el
# mensaje 'Introduce una cadena de texto: '
cadena = str(input("Introduce una cadena de texto: "))
print(cadena,type(cadena))

#4. Crea una variable llamada num1 que pueda recibir valores enteros o decimales. Luego crea otra variable llamada num2
# que tambien reciba valores enteros o decimales. Luego imprime ambos valores por pantalla indicando el tipo de valor.
# ambos numeros deben ser menores o iguales que cero (<=0).
num1 = eval(input("Ingresa un numero: "))
num2 = eval(input("Ingresa otro numero: "))
print(f"Tus numeros son: El num1 {num1}. Y el num2 {num2}")

#5. Escribe un programa que solicite al usuario que ingrese su nombre. El nombre se debe almacenar en una 
# variable llamada nombre. A continuación se debe mostrar en pantalla el texto "Bienvenido a la matrix, 
# [usuario]”, donde “[usuario]” se reemplazará por el nombre que el usuario haya ingresado.
nombre = str(input("Ingresa tu nombre: "))
print("Bienvenido a la Matrix",nombre)

#6. Crea una variable llamada 'nombre' y otra 'apellido' que a traves de un imput almacene una cadena de texto. Luego imprime por
#pantalla el resultado, en una sola linea de codigo. junto con el mensaje: Mi nombre es [nombre] y mi apellido es [apellido]
nombre = str(input("Introduce tu nombre: "))
apellido = str(input("Introeduce tu apellido: "))
print(f"Mi nombre es {nombre} y mi apellido es {apellido}")

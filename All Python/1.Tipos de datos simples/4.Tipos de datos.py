"""
Def: En python tendremos distintos tipos de datos y podemos averiguar con que tipos de 
datos estamos operando a traves de una instruccion type(). Los tipos de datos pueden ser:

int = Enteros.
float = Decimales.
str = Cadenas de texto.
bool = Buleanos.

Los buleanos seran vistos mas adelante.
"""

#1. Muestra por pantalla un numero entero e indica que tipo de dato pertenece.
entero = 5
print(entero,type(entero))
print()

#2. Muestra por pantalla un numero entero que sea de tipo string (cadena de texto)
# imprime su valor y el tipo de dato que pertenece
cadena = "5" #El numero 5, ya no es un numero, pues ahora pertenece a una cadena de texto.
print(cadena,type(cadena))
print()

#3. Muestra por pantalla una cadena de texto e indica que tipo de dato pertenece.
cadena = "El numero pi esta compuesto por el 3.14"
print(cadena,type(cadena))
print()

#4. Muestra por pantalla un numero decimal e indica que tipo de dato pertenece.
decimal = 3.14
print(decimal,type(decimal))
print()


"""
Def: Las funciones incorporadas son parecidas a los metodos string.
La diferencia es que aca podemos usar mas datos, incluyendo numeros.
A lo largo del curso iremos viendo como usarlos de mejor manera,
sin embargo, iremos viendo unos ejemplos para familiarizarnos mejor con ellos.

Ten en cuenta que hasta el momento hemos visto varias funciones incorporadas: input(), eval(), type(), print(), etc...
"""
#1. Dado un numero entero cualquiera, conviertelo en decimal.
entero = int(input("Ingresa un numero entero: "))
decimal = float(entero)
print(decimal)

#2. Dado un numero decimal cualquiera, conviertelo a entero.
decimal = float(input("Ingresa un numero decimal: "))
entero = int(decimal)
print(entero)

#3. Dado un numero cualquiera > 0, devolver su inverso.
x = eval(input("Ingresa cualquier numero > 0: "))
x_abs = abs(x)#La palabra abs proviene de valor absoluto.
print(x_abs)

#4. Dado un numero cualquiera, imprime un mensaje por pantalla mostrando dicho numero pero en lenguaje binario.
x = int(input("Ingresa un numero cualquiera: "))
x_bin = bin(x)#La palabra bin proviene de binario.
#Ten en cuenta que el resultado siempre tendra el prefijo 0b al inicio.
print(x_bin)

#5. Dado una cadena, imprime por pantalla su longitud de la palabra insertada por el usuario.
palabra = str(input("Inserta una palabra cualquiera: "))
palabra_longitud = len(palabra)
print(palabra_longitud)

#6. Dado un numero ingresado por el usuario imprime su rango, es decir desde donde comienza hasta donde termina (su inicio y su fin)
x = int(input("Ingresa un numero: "))
x_rango = range(x)
print(x_rango)

#7. Dado una cadena de numeros enteros, imprime por pantalla el valor minimo.
numeros = (0,1,2,3,4,5)
numero_minimo= min(numeros)
print(numero_minimo)

#8. Dado una cadena de numeros enteros, imprime por pantalla el valor minimo.
numeros = (0,1,2,3,4,5)
numero_maximo= max(numeros)
print(numero_maximo)

#9. Ejecuta el comando de ayuda junto con un parametro cualquiera.
help(int)#El parametro, es lo que va dentro del parentesis().


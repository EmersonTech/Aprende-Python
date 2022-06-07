
"""
Dada las siguentes 5 ecuaciones (mostrar ecuaciones) resuelve el problema y encuentra el resutlado
para cada problema planteado
"""
#1. Problema. El resultado debe ser igual a -72.5333
problema1 = 4**3 * (13/15 - (2*1)) 
print(f"El resultado a nuestro problema es {problema1}")

#2. Problema. Resuelve y transforma el valor a numero entero.
# Si al ingresar A = 3.8 ; B = 20 ; C = 3.1 El resultado sera de 516
a = eval(input("Ingresa un valor a A:"))
b = eval(input("Ingresa un valor a B:"))
c = eval(input("Ingresa un valor a C:"))
problema2 = (a**3 * (b**2 - 2*a*c)) / (2*b)
problema2 = int(problema2)
print(f"El resultado a nuestro problema es {problema2}")

#3. Problema. Resuelve y tansforma el valor a numero entero. El resultado es 1.
problema3 = (((4/15) + (3/10)) / ((12/25) * (20/21)))
problema3 = int(problema3)
print(f"El resultado al problema es {problema3}")

#4. Problema. Resuelve y transforma el valor a entero. El resultado sera -35
problema4 = ((28/4) - (45/9) - 13+8 - (7*3) + (50/10) - 16)
problema4 = int(problema4)
print(f"El resultado al problema es {problema4}")

#5. Problema. Resuelve y transforma el valor a entero. El resultado sera 0
problema5 = (((2/3)**5)**4 * ((2/3)**7)**3 / (((2/3)**6)**2 * ((2/3)**3)**9))
problema5 = int(problema5)
print(f"El resultado al problema es {problema5}")
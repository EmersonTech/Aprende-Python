"""
Variable Auxiliar: Intercambia el valor de 2 variables introducidas
por el usuario.
"""
a = int(input(("a -> ")))
b = int(input(("b -> ")))
print(f"El valor de a es {a} y el valor de b es {b}")
#Variable auxiliar C:
c = a
a = b
b = c
print(f"El nuevo valor de a es {a} y el nuevo valor de b es {b}")
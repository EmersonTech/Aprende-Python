"""
Un programa en donde un usuario ingrese un numero < 0 cualquiera y este devuelva
el mismo numero pero positivo
"""
numero = eval(input("Ingresa cualquier numero > 0: "))
numero = abs(numero)
print(numero)
# Alternativamente, puedo jugar con operaciones matematicas para transformar el digito multiplicando (negativo * negativo = positivo)
# numero = (-1 * numero)
# print(numero) 
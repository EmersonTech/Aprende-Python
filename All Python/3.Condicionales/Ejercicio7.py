"""
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada.

TARIFAS:
Hasta 4 años -> Gratis
Niños entre 5 y 10 años -> 2.000
Niños y adolecentes entre 11 y 16 años -> 4.000
Adolecentes a partir de los 17 años -> 6.000
"""
edad = int(input("Ingresa tu edad: "))
if edad <= 4:
    print("Puedes entrar gratis")
elif edad > 4 and edad <= 10:
    print("El precio por la entrada es de $2.000")
elif edad > 10 and edad <= 16:
    print("El precio por la entrada es de $4.000")
else:
    print("El precio por la entrada es de $6.000")
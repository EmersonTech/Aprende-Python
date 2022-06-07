"""
Una discoteca quiere un programa en donde el usuario ingrese su edad. 
Si es >= 18 puede pasar. De lo contrario, no puede ingresar.
"""
# Menu
print("Bienvenido estimado cliente")

# Pedir valores
edad = int(input("Ingresa tu edad, por favor: "))

# Condicionales
if edad >= 18:
    print("Eres mayor, puedes pasar.")
else:
    print("Lo sentimos, eres menor, no puedes pasar")
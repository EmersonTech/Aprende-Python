"""
Escribe un programa en donde la computadora le pida al usuario crear una contraseña.
Luego el programa pregunte al usuario por esa contraseña ingresada anteriormente.
Si la contraseña coinide entones imprime un mensaje <La contraseña es correcta, puedes ingresar>. De lo contrario, imprime otro mensaje <Error, la contraseña es incorrecta>
El programa no toma en cuenta las mayusculas.
"""
password = input("Bienvenido usario. Cree una contraseña: ")
key = input("Ingresa la contraseña para acceder la computadora: ")
password_lower = password.lower()# Aqui decimos al programa que los caracteres introducidos los convierta en minusculas.
if key == password_lower:
    print("La contraseña es correcta, puedes ingresar")
else:
    print("Error, la contraseña es incorrecta.")
 
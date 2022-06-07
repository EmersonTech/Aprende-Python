"""
Escribe un programa en donde el usuario ingrese su edad. Si es < 0 imprime un mensaje
de error. Si la edad >= 100, imprime un mensaje de error.
"""
edad = int(input("Ingresa tu edad: "))
# Para entender la logica del problema tenemos que recordar que si al ingresar el numero 1 nuestra primer condicion LOGICA se vuelve verdadera, pero la segunda condicion se vuelve falsa. Por lo tanto (verdadero & falso = verdadero) al usar el OR. 
if edad <= 0 or edad >= 100:
    print("Error, edad incorrecta")
else:
    print("Edad aceptada")
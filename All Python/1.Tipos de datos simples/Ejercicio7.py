"""
Crea una variable llamada 'nombre' y otra 'apellido' que a traves de un imput almacene una cadena de texto. Luego imprime por
pantalla el resultado, en una sola linea de codigo. junto con el mensaje: Mi nombre es [nombre] y mi apellido es [apellido]
Ambas palabras deben ser introducidas en minusculas.
"""
nombre = str(input("Introduce tu nombre: "))
apellido = str(input("Introeduce tu apellido: "))
nombre_mayus = nombre.capitalize()
apellido_mayus = apellido.capitalize()
print(f"Mi nombre es {nombre_mayus} y mi apellido es {apellido_mayus}")
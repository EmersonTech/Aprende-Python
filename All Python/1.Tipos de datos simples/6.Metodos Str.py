"""
Def: En python existen los metodos, y son herramientas que nos ayudaran a modificar el comportamiento de
nuestros programas. A continuacion podras ver algunos ejemplos.
"""
#1. capitalize() Sirve para convertir la primer letra de un string en mayusculas.
palabra = input("Ingresa un string: ")
palabra_mayuscula = palabra.capitalize()
print(palabra_mayuscula)

#2. casefold() Convierte las mayusculas iniciales en minusculas. 
palabra = input("Ingresa un string: ")
palabra_minuscula = palabra.casefold()
print(palabra_minuscula)

#3. count() Nos muestra el numero de veces que se repite una palabra.
palabra = ("hola platano platano adios pi 4")
palabra_contar = palabra.count("platano")
print(palabra_contar)

#4. upper() Sirve para transformar un texto completo a mayusculas.
metodo = input("Ingresa un texto en minusculas: ")
metodo_mayusculas = metodo.upper()
print(metodo_mayusculas)

#5. lower() Sirve para transformar un texto completo a minusculas.
metodo = input("Ingresa un texto en mayusculas: ")
metodo = metodo.lower() #Fijate como esta vez no creamos una nueva variable, sino que esta vez a la variable 'metodo' le incorporamos la funcion directamente.
print(metodo)

#6. title() Sirve para que cada palabra ingresada se vuelva mayuscula.
palabra = input("Ingresa una oracion: ")
palabra = palabra.title() #Nuevamente no creamos una nueva variable, sino que esta vez a la variable 'palabra' le incorporamos la funcion directamente.
print(palabra)

#7. replace () Sirve para reemplazar un valor por otro.
oracion = "Pase todo el dia programando codigo en python"
oracion_reemplazada = oracion.replace("python","C++")
# Nota la comparacion entre ambos prints, uno imprime el contendio de la variable oracion, y el otro de la variable oracion_reemplazada.
print(oracion)
print(oracion_reemplazada)

#8. find() Sirve para comprobar si los valores ingresados son mayusculas. Puede devolver dos valores: True, False
palabra = "Tres tristes tigres, tres tristes tigres"
palabra = palabra.islower()
print(palabra)
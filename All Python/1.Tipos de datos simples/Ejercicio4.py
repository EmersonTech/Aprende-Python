"""
Crea un programa de computadora que pida el nombre y el apellido a un usuario para
el inicio de sesion. El programa pedira su nombre y apellido,y  debe
devolver sus iniciales en mayusculas de manera automatica. Recuerda usar los
metodos que hemos visto anteriormente.

Ejemplo: al ingresar
"""
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
nom_mayus = nombre.capitalize()
ape_mauys = apellido.capitalize()
print(f"Bienvenido, usuario {nom_mayus,ape_mauys}")
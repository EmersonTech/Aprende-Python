"""
Un cine promociona su nueva pelicula de miedo y solo podran entrar personas mayores de 18 años. Si el usuario es mayor de 15 años puede entrar si tiene autorizacion de sus padres.
Crea un programa en donde el usuario ingrese su edad y señale si tiene o no autorizacion de sus padres. 
"""
# Menu
print("Bienvenido estimado cliente")

# Pedir valores
edad = int(input("Ingresa tu edad, por favor: "))

# Condicionales
if edad >= 18:
    print("Eres mayor, puedes pasar.")
elif edad >= 15:
    autorizacion = input(("Tienes autorizacion de tus padres?: "))
    if autorizacion == "si": #Pon atencion como creamos una condicion dentro de otra conidcion
        print("Puedes entrar")
    else:
        print("No puedes pasar")
else:
    print("No puedes pasar")
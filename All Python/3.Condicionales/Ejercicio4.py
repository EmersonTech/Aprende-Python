"""
Para pedir un credito en determinado banco se debe ser mayor de 18 años y tener unos ingresos iguales o superiores a 300.000 clp mensuales. Escribir un programa que pregunte al usuario su nombre, edad e ingreso mensual. Y muestre por pantalla su nombre con la inicial en mayuscula y si el usuario puede pedir el credito o no.
"""
# Pedir datos
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
ingresos = eval(input("Ingresa tu sueldo mensual: "))

# Zona de calculos y logica
nombre = nombre.capitalize() #Con esta funcion, nuestra inicial se vuelve mayuscula
if edad >= 18 and ingresos >= 300000: #Nota como estamos usando el operador and y >=
    print(f"Estimado {nombre}. Puede solicitar el credito")
else:
    print(f"Lo sentimos señor {nombre}, no cumple con los requisitos")
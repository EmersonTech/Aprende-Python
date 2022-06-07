"""
Un programa que pida al usuario la base y la altura en cm de un rectangulo
para poder calcular su area y perimetro.
"""
# Zona de imputs
base = eval(input("Ingresa la longitud de la base en cm: "))
altura = eval(input("Ingresa la longitud de la altura en cm: "))

# Zona de calculos
area = (base * altura)
perimetro = (2*(base+altura))

# Zona de outputs
print(f"El area es de {area}cm y su perimetro es de {perimetro}cm")
"""
Un programa que calcule el area y permietro de una circunferencia.
"""
# Zona de imputs
diametro = eval(input("Ingresa el radio de la circunferencia: "))
PI = 3.14

# Zona de calculos
radio = (diametro / 2)
area = (PI * radio**2)
permietro = (2*PI*radio)

# Zona de outputs
print(f"El area es de {area}cm. El perimetro es de {permietro}cm y su radio es {radio}")
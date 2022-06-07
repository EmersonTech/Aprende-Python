"""
organizacion = "FreeCodeCamp"

print("Aprende a programar con " + organizacion)
print("Aprende a programar con {}".format(organizacion))
print(f"Aprende a programar con {organizacion}") #F-string
"""

adj = input("Ingresa adjetivo: ")
verb1 = input("Ingresa adjetivo: ")
verb2 = input("Ingresa adjetivo: ")
verb3 = input("Ingresa adjetivo: ")

madlib = f"Programar es tan {adj}. Siempre me emociona porque me encanta {verb1} problemas. Aprende a {verb2} con python y logra tus {verb3}"

print(madlib)
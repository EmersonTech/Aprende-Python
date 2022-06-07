"""
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:

Renta	                 Tipo impositivo
Menos de 10000€	                5%
Entre 10000€ y 20000€	        15%
Entre 20000€ y 35000€	        20%
Entre 35000€ y 60000€	        30%
Más de 60000€	                45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo 
impositivo que le corresponde.
"""
renta = eval(input("Escribe tu ingreso: "))
if renta < 10000:
    print("Te corresponde un impositivo del 5%")
elif renta < 20000:
    print("Te corresponde un impositivo del 15%")
elif renta < 35000:
    print("Te corresponde un impositivo del 20%")
elif renta < 60000:
    print("Te corresponde un impositivo del 30%")
else:
    print("Te corresponde un impositivo del 45%")
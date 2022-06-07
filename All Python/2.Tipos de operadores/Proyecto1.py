"""
TIENDA DE ROPA.

Una tienda de ropa vende diferentes productos: Polerones, Zapatillas, Gorro y pantalones.
El precio unitario de cada producto esta compuesto por determinados precios en pesos chilenos clp:

Gorro: $15.000 c/u
Pantalon: $20.000 c/u
Poleron: $25.000 c/u
Zapatillas: $30.000 c/u


1. Crea un menu que se imprima por pantalla, mostrando los productos y sus precios unitarios.
2. Crea variables que almacenen la cantidad de gorros, zapatillas, etc... que el cliente desee llevar
3. Añade la tarifa del iva teniendo en cuenta que este es del 19%
4. Suma todas las compras del cliente en una variable.
5. Muestra un mensaje por pantalla la cantidad de cada producto que el cliente quiera llevar. Adicional
a eso, que se muestre el precio total de la compra, el precio del iva y el precio de la compra añadiendo el iva.

Ejemplo:
Si el cliente lleva: 1 gorro, 1 pantalon, 1 poleron y 1 par de zapatillas. El programa debe imprimir:
El cliente desea llevar: 1 gorros, 1, polerones, 1 pantalones, 1 par de zapatillas. El total de la compra es de $90000, el valor del iva por la compra es $17100 y el precio total incluyendo el iva es de $107100 pesos.
"""

# Menu
print("*Bienvenido a nuestra tienda virtual*")
print("=========================")
print("Nuestros productos son: ")
print()
print("Gorro: $15.000 c/u")
print("Pantalon: $20.000 c/u")
print("Poleron: $25.000 c/u")
print("Zapatillas: $30.000 c/u")
print("=========================")

# Zona de peticion de valores de entrada
gorro = int(input("Cuantos gorros quiere llevar?: "))
polerones = int(input("Cuantos polerones quiere llevar?: "))
pantalones = int(input("Cuantos pantalones quiere llevar?: "))
zapatillas = int(input("Cuantos pares de zapatillas quiere llevar?: "))
tarifa_iva = 0.19 #Recuerda que decir 0.19 es igual que 19%

# Zona de calculos
precio_gorro = (gorro * 15000)
precio_poleron = (polerones * 25000)
precio_pantalon = (pantalones * 20000)
precio_zapatillas = (zapatillas * 30000)
precio_total_compra = (precio_pantalon + precio_gorro + precio_poleron + precio_zapatillas)

# Aqui calculamos el iva con su formula: iva = (valor producto * tarifa iva)
precio_iva = int((tarifa_iva * precio_total_compra))
precio_total = int((precio_iva + precio_total_compra))
#Usamos la funcion int() para que el resultado sea entero

# Aqui imprimimos el resultado del problema
print(f"El cliente desea llevar: {gorro} gorros, {polerones}, polerones, {pantalones} pantalones, {zapatillas} par de zapatillas. El total de la compra es de ${precio_total_compra}, el valor del iva por la compra es ${precio_iva} y el precio total incluyendo el iva es de ${precio_total} pesos")
 


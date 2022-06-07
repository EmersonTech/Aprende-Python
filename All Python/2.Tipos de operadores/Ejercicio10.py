"""
Un producto cuesta $70.000 clp sin iva, crea un programa que calcule
cuanto se debe pagar en total incluyendo el iva con un mensaje tipo:
El precio de la compra es de $<precio compra> y el precio total de la
compra incluyendo el iva es de $<precio compra + iva>. 
Toma en cuenta que el iva es del 19%
"""
valor_producto = 70000
tarifa_iva = 0.19
valor_total = (valor_producto * (1+tarifa_iva))
print(f"El precio de la compra es de {valor_producto} y el precio total de la compra incluyendo el iva es de {valor_total}")
"""
Un producto cuesta $40.000 clp sin IVA. Crea un programa que calcule
cual es la cantidad que debe pagar por el concepto de IVA, 
tomando en cuenta que es del 19%, junto con un mensaje que diga:
El valor solamente del iva es de $<iva> pesos

Formula para calcular el iva:
iva = (valor producto * tarifa iva) 
"""
valor_producto = 40
#El 19% es lo mismo que 0.19
tarifa_iva = 0.19
iva = int(valor_producto * tarifa_iva)
print(f"El valor solamente del iva es de ${iva} pesos")
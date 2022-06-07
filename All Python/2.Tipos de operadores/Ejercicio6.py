"""
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
calcule el índice de masa corporal y lo almacene en una variable, y muestre por 
pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice 
de masa corporal calculado redondeado con dos decimales.
"""
peso = eval(input("Ingrese su peso en kg: "))
estatura = eval(input("Ingrese su estatura en cm: "))
imc = (peso / (estatura)**2)
imc_redondeado = round(imc) #Con esta instruccion redondeamos el numero.
print(f"Tu índice de masa corporal es {imc}") #Este es el resultado sin redondeo.
print(f"Tu índice de masa corporal es {imc_redondeado}")#Este es el resultado redondeado.
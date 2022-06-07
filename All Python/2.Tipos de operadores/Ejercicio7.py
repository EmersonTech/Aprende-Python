"""
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> 
da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, 
y <c> y <r> son el cociente y el resto de la división entera respectivamente.
"""
n = eval(input("Ingresa un numero: "))
m = eval(input("Ingresa un numero: "))
c = (n // m)
r = (n % m)
print(f"Al dividir los numeros {n} y {m}, da un cociente {c} y un resto {r}")
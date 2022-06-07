"""
Crea un programa en donde el usuario ingrese un numero entero,
luego otro numero decimal. Convierte el decimal a entero y el 
entero a decimal. Luego imprime un mensaje por pantalla Recuerda usar las funciones 
incorporadas.
"""
# Aqui hacemos la entrada de valores.
entero = int(input("Ingresa un entero: "))
decimal = float(input("Ingresa un decimal: "))

# Aqui hacemos la conversion de valores, de decimal a entero y viceversa.
entero_a_decimal = float(entero)
decimal_a_entero = int(decimal)

# Aqui ejecutamos el print()
print(f"El numero entero ingresado es {entero} y su conversion es {entero_a_decimal}. El numero decimal ingresado es {decimal} y su entero es {decimal_a_entero}")
"""
En estado de pandemia, una tienda de accesorios de telefonia te contrata como programador para crear un programa
que automatice sus procesos de logisticas.
La tienda se destaca vendiendo: Carcasas de telefono y cargadores. El precio unitario de cada carcasa es de
$15 USD y los cargadores son de $10 USD.
Crea un programa que pregunte cuantas carcasas y cargadores desea el cliente. Luego mostrar por pantalla un mensaje
tipo: El cliente quiere <cantidad> carcasas y <cantidad> cargadores. El valor total de las carcasas es de $<valor total>
y el valor total de los cargadores es de $<valor total>. Sumando ambas compras nos da un total de $<total carcasas y cargadores>
"""
# Aqui hacemos la entrada de datos.
carcasas = int(input("Cuantas carcasas quiere el cliente?: "))
cargadores = int(input("Cuantos cargadores quiere el cliente?: "))

# Aqui hacemos las operaciones aritmeticas.
valor_carcasas = (carcasas * 15)
valor_cargadores = (cargadores * 10)
valor_total_compras = (valor_cargadores + valor_carcasas)

# Aqui hacemos la salida de datos.
print(f"El cliente quiere {carcasas} carcasas y {cargadores} cargadores. El valor total de las carcasas es de ${valor_carcasas} y el de los cargadores es de ${valor_cargadores}. El precio total de las compras es de ${valor_total_compras}")
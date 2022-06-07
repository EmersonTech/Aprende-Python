print()
import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print(f"El nombre de tu computadora es: {hostname}") #F-sting
print("Tu ip es: " + ip)
print("Apreta la telca ENTER para salir")
#Para que el programa no se cierre
input()
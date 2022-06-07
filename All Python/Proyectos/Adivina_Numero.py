import random


def adivina_numero(x):
    print("===================")
    print("BIENVENIDO AL JUEGO")
    print("===================")
    print()
    print("Tu objetivo es adivinar el numero generado por la computadora")

    numero_aleatorio = random.randint(1, x) #Numero aleatorio entre 1 y x

    prediccion = 0

    while prediccion != numero_aleatorio:
        #El usuario ingresa un numero
        prediccion = int(input(f"Adivina un numero entre 1 y {x}: "))#F-string

        if prediccion < numero_aleatorio:
            print("Game over")
        elif prediccion > numero_aleatorio:
            print("Game over")

    print(f"Felicitaciones, adivinaste el numero {numero_aleatorio} correctamente")


adivina_numero(10)
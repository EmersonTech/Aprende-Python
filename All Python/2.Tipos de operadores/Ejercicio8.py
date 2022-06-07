"""
Dado los siguentes problemas, comprueba su veracidad y responde en el comentario
Una vez respondido cada ejercicio ejecuta el codigo.
"""
#1. Comparar si se cumplen las condiciones, si son verdaderas o falsas.
x = 2
print("Problema 1",1 > x > 3)
#La respuesta es: False

#2. Comparar si se cumplen las condiciones, si son verdaderas o falsas.
num1 = 2
num2 = 2
print("Problema 2",num1 != num2)
#La respuesta es: False

#3. Comparar si se cumplen las condiciones, si son verdaderas o falsas.
num1 = 4
num2 = 3
print("Problema 3",num1 == num2)
#La respuesta es: False

#4. Comparar si se cumplen las condiciones, si son verdaderas o falsas.
a = 20
b = 25
c = 22
resultado1 = (a+b) >= (c+a)
print("Problema 4",resultado1)
#La respuesta es: True

#5. Comparar si se cumplen las condiciones, si son verdaderas o falsas.
a = 2
b = 2
c = 3
d = 3
resultado2 = (a >= b and c <= d)
print("Problema 5",resultado2)
#La respuesta es: True

#6. Comparar si se cumplen las condiciones, si son verdaderas o falsas.
a = 1
b = 2
c = 3
resultado3 = ((a != b) or (c != c))
print("Problema 6",resultado3)
#La respuesta es: True

#7. Comparar si se cumplen las condiciones, si son verdaderas o falsas.
a = 22
b = 23
c = 22
resultado4 = (not(c >= a) and (b > c))
print("Problema 7",resultado4)
#La respuesta es: False

#8. Comparar si se cumplen las condiciones, si son verdaderas o falsas.
a = 22
b = 23
c = 22
resultado5 = (not(c >= a) or (b > c))
print("Problema 8",resultado5)
#La respuesta es: True

#9. Comparar si se cumplen las condiciones, si son verdaderas o falsas.
a = 22
b = 23
c = 22
resultado6 = (not(c >= a) or not(b > c))
print("Problema 9",resultado6)
#La respuesta es: False

#10. Comparar si se cumplen las condiciones, si son verdaderas o falsas.
a = 22
a *= 2
b = 33
b //= 2
resultado7 = (not(a > b)) and (b != a) and not(b < a)
print("Problema 10",resultado7)
#La respuesta es: False

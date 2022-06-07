"""
Def: Los operadores de asignasion son usadas para asignar valores, tal como hemos visto
a lo largo del curso. Sin embargo, podemos combinarlos con los operadores aritmeticos.
Por ejemplo:

=
+=
-=
*=
/=
//=
%=
"""

#1. Realizar una asignacion a un numero.
x = 5
print(x)

#2. Realizar una suma entre la variable X y el numero 3 (+=).
x = 5
x += 3 #El numero 3 se estara sumando al contenido de la variable x, osea el 5
print(x)

#3. Realizar una resta entre la variable X y el numero 7.
x -= 7
print(x)#Como vimos anteriormente el valor X va operando con las demas variables. Y ahora lo restamos con el 7, quedando resultado 1.

#4. Agregar la variable Y = 2. Luego realiza una operacion aritmetica para que Y ahora valga 10
y = 5
y *= 2
print(y)

#5. La variable Y tiene que ser potenciada por el contenido de la variable X
y **= x
# El resultado va a ser 10 ya que estamos escribiendo 10 en potencia de 1
print(y)

#6. 

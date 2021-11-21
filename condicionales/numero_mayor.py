# Se cargan por teclado tres números distintos.
# Mostrar por pantalla el mayor de ellos.

number_one = int(input('Ingresa el primer numero: '))
number_two = int(input('Ingresa el segundo numero: '))
number_three = int(input('Ingresa el primer numero: '))

if number_one > number_two:
    if number_one > number_three:
        print(f' El {number_one} es mayor')
    else:
        print(f' El {number_three} es mayor')
else:
    if number_two > number_one:
        print(f' El {number_two} es mayor')
    else:
        print(f' El {number_three} es mayor')

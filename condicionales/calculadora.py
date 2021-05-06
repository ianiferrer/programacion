'''
Script en python que simule una calculadora con las 
operaciones artméticas básicas. El Menú mostrado será
el siguiente:

Suma
Resta
Multiplicación
División
División Entera
Módulo
Potencia
''' 


ADDING = 1
SUBTRACT = 2
MULTIPLY = 3
DIVISION = 4
INTEGER_DIVISION = 5
MODULE = 6
POWER= 7

print(f'''               CALCULADORA BASICA V1
{ADDING}) Suma
{SUBTRACT}) Resta
{MULTIPLY}) Multiplicación
{DIVISION}) División 
{INTEGER_DIVISION}) División Entera
{MODULE}) Módulo
{POWER}) Potencia
''')

choose_number = int(input('Elige un número '))

if ADDING <= choose_number <= POWER:
        first_number = int(input('Primer valor '))
        second_number = int(input('Segundo Valor '))
        if choose_number == ADDING:
               print(f'{first_number} + {second_number} = {first_number + second_number}') 
        elif choose_number == SUBTRACT:
                print(f'{first_number} - {second_number} = { first_number - second_number}')
        elif choose_number == MULTIPLY:
                print(f'{first_number} * {second_number} = { first_number * second_number}')
        elif choose_number == DIVISION:
                if second_number != 0:
                        print(f'{first_number} / {second_number} = { first_number / second_number}')
                else:
                        print('Opción no definida')
        elif choose_number == INTEGER_DIVISION:
                if second_number != 0:
                        print(f'{first_number} // {second_number} = { first_number // second_number}')
                else:
                        print('Opción no definida')
        elif choose_number == MODULE:
                if second_number != 0:
                        print(f'{first_number} % {second_number} = { first_number % second_number}')
                else:
                        print('Opción no definida')
        else:
                print(f'{first_number} ** {second_number} = { first_number ** second_number}')

else:   
        print('Opcion no valida')

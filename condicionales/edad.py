'''
Algoritmo-2
Script en python que solicite la edad del usuario y si esa edad es mayor o igual que 18 indicarle que es mayor de edad.

'''

# Datos de entrada -> Edad del usuario
# Dato de salida -> Mostrar por pantalla al usuario que es mayor de edad
# Proceso -> si edad > = 18:
                # print('Es mayor de edad)

print('Peograma para detectar si tu edad es mayor o igual a 18')
number = int(input('Edad: '))

if number >= 18:
    print(f'Tu edad es{number}, eres mayor de edad.')

print('Adios...')
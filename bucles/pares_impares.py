'''
Algoritmo 1: Contar pares e impares
Se desea hallar la suma de los números pares e impares comprendidos entre 1 y 100.
'''
# Datos de Entrada  -> Números del 1 al 100
# Datos de Salida  -> Suma de números pares e impares del 1 al 100
# Procesos -> Usar el modulo (%) para saber saber si es par o impar

aadd_pairs = 0
odd_numbers = 0

for numbers in range(1,101):
    if numbers % 2 == 0:
       aadd_pairs += numbers
    else:
        odd_numbers += numbers

print(f'La suma de los numeros pares es : {aadd_pairs}')
print(f'La suma de los numeros impares es : {odd_numbers}')

 
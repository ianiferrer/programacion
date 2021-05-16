'''
Conversor de grados célsius a grados fahrenheit.

'''

# Pedir al usuario el grado por teclado.
# formula f = (9/5 * celsius) + 32 
# Resultado en fahrenheit
print('''      CONVERSOR DE GRADOS CELSIUS A FAHRENHEIT.''')
Celsius_degrees = int(input('Grados Célsius'))
fahrenheit_degrees = float((9/5 * Celsius_degrees) + 32)
print(f'Convirtiendo a grados fahrentheit:... {fahrenheit_degrees} ')
# Calcular el máximo de números positivos introducidos por
# teclado, sabiendo que metemos números hasta que
# introduzcamos uno negativo

numero = 1
suma = 0
while numero > 0:
    numero = int(input('digite un número '))
    if numero > 0:
        suma = suma + numero
print(f'La suma de los numeros es: {suma} ')
    
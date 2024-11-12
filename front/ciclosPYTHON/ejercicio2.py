# Determinar si un numero es o no es primo

num = int(input('por favor ingrese un número: '))

a = 1
y = 0

while a <= num:
    if num % a == 0:
        y += 1
    a += 1
    
if y == 2:
    print(f'El número {num} es primo')
    
else:
    print(f'El núemero {num} no es primo')

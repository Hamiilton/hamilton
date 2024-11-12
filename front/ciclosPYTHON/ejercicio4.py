# Determinar cuales y cuantos números perfectos hay entre 1 y
# 1000?
for y in range(1, 1001):

    z = 2
    suma = 0
    while z <= y:
        if y % z == 0:
            suma += y // z
        z += 1
        
    if suma == y:
        print(y)
        
        
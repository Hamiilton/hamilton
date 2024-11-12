# Algoritmo para hallar el m.c.d de dos números m y n por
# el algoritmo de Euclides.



# def mcd_euclides(n1, n2):
  
       
#     while n1 % n2 != 0:
        
#         resto = n1 % n2
#         n1 = n2
#         n2 = resto
#     return n2
# print(mcd_euclides(60, 48))

n1 = int(input('ingrese un número '))
n2 = int(input('ingrese otro número '))

while n1 % n2 != 0:
        
        resto = n1 % n2
        n1 = n2
        n2 = resto
        
print (f'El mcd de los numeros ingresado  es {n2}')
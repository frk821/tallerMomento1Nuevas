'''
    1.Construir un programa que permita ingresar N (cantidad digitada por
    el usuario) números enteros y cuente cuantos múltiplos de 2 y de 3
    fueron ingresados
'''

cantidad = int(input("Cuantos números quiere ingresar en la lista?: "))

numeros = []

contador = 1
while(contador<=cantidad):
    numero = int(input("Digita un número: "))
    numeros.append(numero)
    contador +=1

multiplos2 = 0
multiplos3 = 0

for auxiliar in numeros:
    if(auxiliar%2==0):
        multiplos2 += 1            
    if(auxiliar%3==0):
        multiplos3 += 1

print(f'En la lista de números {numeros}')
print(f'Hay {multiplos2} multiplos de 2')
print(f'Hay {multiplos3} multiplos de 3')

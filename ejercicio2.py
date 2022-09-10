'''
    2.Leer el nombre de 10 frutas {nombre, color, precio} para preparar un
    salpicón; el programa debe permitir mostrar las 10 frutas ingresadas al
    mismo tiempo en sentido inverso al ingresado
'''


print("**************** FRUTAS *******************")
print("*** Ingresa las frutas para el salpicón ***")

#Lista Productos
frutas = []
frutasInvertidas = []
contador = 0

while(contador<4):
    fruta = {}
    fruta['nombre']=input("Digita el nombre de la Fruta: ")
    fruta['color']=input("Digita el color de la Fruta: ")
    fruta['precio']=input("Digita el precio de la Fruta: ")
    print("***Fruta añadida***")
    frutas.append(fruta)
    contador +=1
    frutasInvertidas.insert((len(frutas)-contador),fruta)



print('Las Frutas registradas son:')
print(frutas)
print("********************************************************************")
print('Las Frutas invertidas')
print(frutasInvertidas)

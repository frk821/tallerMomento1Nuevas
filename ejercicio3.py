'''
    3.Construir un programa para ir de compras en un supermercado
    que permita la construcción del siguiente MENU:
    1. Digitar 1 para recibir {código, nombre, precio} de un producto (+0.4)
    2. Digitar 2 para mostrar todos los productos registrados (+0.4)
    3. Digitar 3 para permitir buscar por código un producto y editar el precio
    de este (+0.4)
    4. Digitar 4 para permitir buscar por código un producto y eliminar el
    producto (+0.4)
    5. Digitar 0 para SALIR
'''

print("*** Tienda Frank ***")
print("*** Elige una opción ***")
print("1. Ingresar productos al inventario")
print("2. Para ver todos los productos registrados")
print("3. Busca un producto por su código y Edita su precio")
print("4. Busca un producto por su código y Eliminarlo")
print("5. Digita 0 (cero) para salir")


#Lista Productos
productos = []

#opcion
opcion = 50

while(opcion != 0):
    #Diccionario Producto
    producto = {}
    opcion=int(input("Digita una opción: "))
    if(opcion==1):
        producto['codigo']=input("Digita el codigo del Producto: ")
        producto['nombre']=input("Digita el nombre del Producto: ")
        producto['precio']=input("Digita el precio del Producto: ")
        print("***Producto agregado***")
        productos.append(producto)

    elif(opcion==2):
        print("*** Productos Registrados ***")
        print(productos)
    elif(opcion==3):
        busqueda = input("Ingrese el codigo del producto que desea cambiar su precio: ")
        for auxiliar in productos:
            if(auxiliar['codigo']==busqueda):
                auxiliar['precio']=input("Ingresa el precio que deseas actualizar: ")            
        print(productos)   
    elif(opcion==4):
        busqueda = input("Digita el código del producto que deseas eliminar: ")
        for auxiliar in productos:
            if(auxiliar['codigo']==busqueda):
                productos.remove(auxiliar)            
        print(productos)
    elif(opcion==0):
        break
    else:
        print("Pilas!!! *Digite una opción válida")

else:
    print("Salió del Programa")


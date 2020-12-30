# -*- coding: utf-8 -*-
"""
@author: JC
"""
# Valores iniciales (de prueba) para los productos
productos = {"p01": ["Producto 1", 10.5], "p02": ["Producto 2", 20.3]}


def registrar_producto():
    cod_prod = input("Ingrese codigo de producto: ")
    desc = input("Ingrese descripcion: ")
    precio = float(input("Ingrese precio unitario: "))
    productos[cod_prod] = [desc, precio]
    print("Pedido registrado correctamente")


def mostrar_producto(codigo, nombre, precio):
    print("Producto encontrado ... ")
    print("****************************")
    print("Codigo:", codigo)
    print("Descripcion:", nombre)
    print("Precio:", precio)
    print("****************************")


def buscar_producto():
    print("Ingrese opcion de busqueda: ")
    print("1) Por codigo")
    print("2) Por nombre")
    opcion = int(input(">> "))
    cod_prod = None
    if (opcion == 1):
        cod_buscar = input("Ingrese codigo producto: ")
        if (productos.get(cod_buscar) != None):
            datos = productos[cod_buscar]#obtengo los datos, en este caso es una lista(nom prod,cant)
            mostrar_producto(cod_buscar, datos[0], datos[1])
            cod_prod = cod_buscar #cod prod 1!=none
        else:
            print("Producto no encontrado")
    elif (opcion == 2):
        nombre_buscar = input("Ingrese nombre producto: ")
        claves = list(productos.keys())#obtengo una lista de claves codigo de vendedor
        valores = list(productos.values())# obtengo una lista de listas valores (nomProd, cant)
        encontrado = False
        for i in range(len(valores)):
            producto = valores[i]# solo obtengo la primer lista del i=0
            nombre = producto[0] # esta lista es [nombre,cant]
            if (nombre == nombre_buscar):
                mostrar_producto(claves[i], nombre, producto[1])
                cod_prod = claves[i]
                encontrado = True
        if (encontrado == False):
            print("Producto no encontrado")
    else:
        print("Opcion incorrecta")
    return cod_prod
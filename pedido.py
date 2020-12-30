# -*- coding: utf-8 -*-
"""
@author: JC
"""
import producto as prd

'''
Los productos se almacenan en un diccionario
Estructura:
    - Clave:    Tupla formada por: Codigo de pedido y codigo de usuario.
                El caso no menciona informacion de usuario asi que se
                asumira un codigo (se utilizara una variable)
    - Valor:    Lista de tuplas, cada una de ellas contiene el codigo de 
                producto y la cantidad de unidades.
    Ejemplo:
        {(100, 1234): [("P01", 3), ("P02", 4)]}
        Se interpreta de la siguiente forma:
            - El codigo de pedido es 100
            - El codigo de usuario es 1234
            - La composicion del pedido es la siguiente:
                - 3 unidades del producto "P01"
                - 4 unidades del producto "P02"
'''

# Pedidos de ejemplo
pedidos = {(1, 1234): [("p01", 4), ("p02", 3)], (2, 1234): [("p02", 3)]}
# Se asume que siempre trabajaremos con el mismo usuario
cod_usuario = 1234
# Porcentaje de IGV
RATIO_IGV = 0.18


def registrar_pedido():
    # Asignamos el codigo de pedido (se incrementara de 1 en 1)
    cod_pedido = len(pedidos) + 1
    lista_prod = []# se crea una lista de productos del pedido
    continuar = True
    while (continuar == True):
        cod_prod = prd.buscar_producto()
        if (cod_prod != None):
            unidades = int(input("Ingrese cantidad de unidades: "))
            lista_prod.append((cod_prod, unidades))
        opcion = input("Ingrese 'S' para agregar otro producto: ")
        if (opcion != "S"):
            continuar = False
    pedidos[(cod_pedido, cod_usuario)] = lista_prod # diccionario clave es una tupla y valor es una lista q contiene una tupla
    print("Se ha generado el pedido: ", cod_pedido)


def buscar_pedido():
    cod_ped = int(input("Ingrese codigo del pedido: "))
    lista_prod = pedidos.get((cod_ped, cod_usuario))# usa get para obtener la lista [cod_prod,unid) mediante las clave ( cod_pe,cod_usuari)
    subtotal = 0
    if (lista_prod != None):
        print("Informacion del pedido", cod_ped)
        for item in lista_prod:
            cod_prod = item[0]
            cantidad = item[1]
            producto = prd.productos[cod_prod]# aqui obtengo los valores tipo lista [ nomb, precio] mediante la clave
            nombre = producto[0]
            precio = producto[1]
            print("****************************")
            print("Producto:", nombre)
            print("Unidades:", cantidad)
            print("****************************")
            subtotal = subtotal + cantidad * precio
        print("Subtotal:", subtotal)
        print("Impuesto:", subtotal * RATIO_IGV)
        print("Total:", subtotal * (1 + RATIO_IGV))
    else:
        print("Pedido no encontrado")



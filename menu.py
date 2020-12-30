
# -*- coding: utf-8 -*-
"""
@author: JC
"""
import pedido
import producto

tupla_opciones = ("Registrar producto",
                  "Buscar producto",
                  "Registrar pedido",
                  "Consultar pedido",
                  "Salir"
                  )


def main():
    opcion = -1
    opcion_salir = len(tupla_opciones)
    while (opcion != opcion_salir):
        print("****************************")
        print("Seleccione una opcion: ")
        for i in range(1, len(tupla_opciones) + 1):
            print(str(i) + ")", tupla_opciones[i - 1])
        print("****************************")
        opcion = int(input(">> "))
        if (opcion == 1):
            producto.registrar_producto()
        elif (opcion == 2):
            producto.buscar_producto()
        elif (opcion == 3):
            pedido.registrar_pedido()
        elif (opcion == 4):
            pedido.buscar_pedido()
        elif (opcion == 5):
            print("Gracias por utilizar la aplicacion")
        else:
            print("Opcion incorrecta")


# Pruebas
main()
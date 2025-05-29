
from  paquete.funciones import *
from  paquete.validate import *


def iniciar():
    depositos = ["CABA", "Z SUR", "Z OESTE", "Z NORTE"]
    vendedores = [0,1,2,3,4]
    matriz_vacia = crear_matriz(len(vendedores), len(depositos))
    matriz_vacia_vendedores = crear_matriz(len(vendedores), len(depositos))
    
    print("Bienvenido al programa")
    resultado1 = None
    resultado2 = None
    inicio = True

    while inicio == True:
        print("1)Obtener ventas\n2)Obtener vendedores\n3)Vendedor que superen 500.000\n4)Mostrar zonas en que se vendieron más de $2.000.000.\n5)Obtener el mejor vendedor de cada zona.\n6)Cambiar vendedores\n7)Informe de ingresos de la empresa:\n8)Mostrar ventas en otras monedas\n9)Porcentaje de ventas de cada vendedor sobre el total de ventas de cada zona.\n10)Salir")

        opcion = int(input("Elija una opcion: "))
        opcion = validar_rango(opcion,10,1)
        if opcion == 1:
            if resultado1 == None:
                resultado1 = cargar_secuencialmente(matriz_vacia, vendedores, depositos, "ventas", "Ingrese un valor para la venta")
                print("\nVentas cargadas exitosamente!\n")
                
            else:
                print("\tMatriz Ventas\n")
                agregar_indice(resultado1,depositos,vendedores)
                
        elif opcion == 2:
            if resultado2 == None:
                resultado2 = cargar_secuencialmente(matriz_vacia_vendedores, vendedores, depositos, "vendedores", "Ingrese el vendedor de la venta")
                print("\nVendedores cargados exitosamente!\n")
            else:
                print("\tMatriz Vendedores\n")
                agregar_indice(resultado2,depositos,vendedores)
                
        elif opcion == 3:
            if resultado1 != None:
                print("")
                buscar_vendedor_maximo(resultado2, resultado1)
                print("")
            else:
                print("\nPrimero debe cargar las ventas (opcion 1)\n")
                
        elif opcion == 4:
            if resultado1 != None:
                print("")
                buscar_zona_maximo(resultado1, depositos)
                print("")
            else:
                print("\nPrimero debe cargar las ventas (opcion 1)\n")
                
        elif opcion == 5:
            if resultado1 != None:
                print("")
                mostrar_mejores_vendedores(resultado1, resultado2, vendedores,depositos)
                print("")
            else:
                print("Primero debe cargar las ventas (opcion 1)")

        if opcion == 7:
            print()
        if opcion == 8:
            print()
        if opcion == 9:
            print()
        if opcion == 10:
            print("Saliendo...\n")
            inicio = False
            break

inicio = iniciar()
if inicio == None:
    print("Programa finalizado.")

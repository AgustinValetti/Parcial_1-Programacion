
from  paquete.funciones import *
def iniciar():
    depositos = ["CABA ", "Z SUR ", "Z OESTE","Z NORTE"]
    vendedor = ["Daniel", "Matias", "Damian","Marcos","Janina"]
    matriz_vacia = crear_matriz(len(vendedor), len(depositos))
    print("Bienvenido al programa")

    inicio = True

    while inicio == True:
        print("1)Obtener ventas\n2)Obtener vendedores\n3)Vendedor que superen 500.000\n4)Mostrar zonas en que se vendieron más de $2.000.000.\n5)Obtener el mejor vendedor de cada zona.\n6)Cambiar vendedores\n7)Informe de ingresos de la empresa:\n8)Mostrar ventas en otras monedas\n9)Porcentaje de ventas de cada vendedor sobre el total de ventas de cada zona.\n10)Salir")

        opcion = int(input("Elija una opcion: "))

        if opcion == 1:
            matriz_ventas = cargar_secuencialmente(matriz_vacia, vendedor,depositos, "Ingrese un valor de la venta de")
            print()
        if opcion == 2:
            resultado2 = cargar_secuencialmente(matriz_vacia, depositos,vendedor, "Ingrese un valor de la venta en")
            print()

        if opcion == 3:
            resultado3 = buscar_vendedor_maximo(vendedor, matriz_ventas)
            print()
        if opcion == 4:
            print("4. Mostrar zonas en que se vendieron más de $2.000.000.\n")
            resultado4 = buscar_zona_maximo(matriz_ventas,depositos)

        if opcion == 5:
            probar = mostrar_mejores_vendedores(matriz_ventas, depositos,vendedor)
            print()
        if opcion == 6:
            print()

        if opcion == 7:
            print()
        if opcion == 8:
            print()
        if opcion == 9:
            inicio = False
        if opcion == 10:
            print("Saliendo...\n")
            inicio = False
            break

inicio = iniciar()
if inicio == None:
    print("Programa finalizado.")

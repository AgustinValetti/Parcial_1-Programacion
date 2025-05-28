
depositos = ["CABA ", "Z SUR ", "Z OESTE","Z NORTE"]
vendedor = ["Daniel", "Matias", "Damian","Marcos","Janina"]


def crear_matriz(filas:int,
                 columnas:int)-> list:
    
    """
    Esta funcion recibe dos eneteros
    el primero en forma de filas y el segundo en columnas
    devuelve una matriz
    """
    if type(filas) == int and type(columnas) == int:
        matriz = []
        

        for i in range(filas):
            fila = [0] * columnas
            matriz += [fila]

    
    else:
        return "Los datos ingresados deben ser enteros"
    
    return matriz


def cargar_secuencialmente(matriz:list,
                            vendedor:list,
                            deposito:list,
                            mensaje:str="")-> list:
    """
    Esta funcion recibe una matriz y la carga secuencialmente
    retorna la matriz cargada
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            cargar = int(input(f"{mensaje} {vendedor[j]} en {deposito[j]}:  "))

            matriz[i][j] = cargar

    
    return matriz

def mostrar_matriz(matriz:list)->list:
    """
    Esta funcion recibe una matriz y
    la retorna ordenada para una mejor
    visualizacion
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], "\t", end="")
        print("")
    return
# matriz_vacia = crear_matriz(len(vendedor), len(depositos))

# resultado = cargar_secuencialmente(matriz_vacia, vendedor,depositos, "Ingrese un valor de la venta de")
# mostrar_matriz(resultado)


def buscar_vendedor_maximo(matriz_vendedores:list, matriz_ventas:list)-> str:
    """
    Esta funcion recibe una matriz de ventas, una lista
    y retonra los vendedores con mayores ventas
    """

    print("Vendedores superiroes a 500.000:")
    for i in range(len(matriz_ventas)):
        
        for j in range(len(matriz_ventas[i])):
            if matriz_ventas[i][j] > 500000:

                print("\t",matriz_vendedores[i][j])



# resultado = buscar_vendedor_maximo(matriz_vendedores, matriz_ventas)

def buscar_zona_maximo(matriz_ventas:list, depositos:list)-> str:

    """
    Esta funcion recibe por parametro una matriz de ventas
    y retorna las zonas con ventas mayores a 2.000.000
    """

    cantidad_zonas = len(matriz_ventas[0])
    print("Zonas superiroes a 2.000.000:")
    for j in range((cantidad_zonas)):
        total_de_la_zona = 0
        for i in range(len(matriz_ventas)):
            total_de_la_zona += matriz_ventas[i][j]

        if total_de_la_zona > 2000000:
            print(f"Zona {depositos[j]} (Total recaudacion vendida: ${total_de_la_zona})")


# resultado2 = buscar_zona_maximo(matriz_ventas,depositos)

def mostrar_mejores_vendedores(matriz_ventas:list
                               ,depositos:list
                               ,vendores:list)-> str:

    """
    Esta funcion recibe por parametro una matriz de ventas
    y retorna los mejores vendedores
    """

    cantidad_de_zonas = len(matriz_ventas[0])

    for j in range(cantidad_de_zonas):
        venta_maxima = 0
        mejor_vendedor = ""

        for i in range(len(matriz_ventas)):
            if matriz_ventas[i][j] > venta_maxima:
                venta_maxima = matriz_ventas[i][j]
                mejor_vendedor = vendores[j]
        
        print(f"En {depositos[j]}: el mejor vendedor fue {mejor_vendedor}, Venta total: { venta_maxima}")

    return
# probar = mostrar_mejores_vendedores(matriz_ventas, depositos,vendedor)

# print(probar)



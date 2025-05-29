


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


def cargar_secuencialmente(matriz: list,
                          lista_filas: list,
                          lista_columnas: list,
                          tipo_de_dato: str,
                          mensaje: str = "") -> list:
    """
    Esta función recibe una matriz y la carga secuencialmente
    retorna la matriz cargada
    """
    if tipo_de_dato == "ventas":
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                cargar = int(input(f"{mensaje} {lista_filas[i]} en {lista_columnas[j]}: "))
                matriz[i][j] = cargar
        return matriz

    elif tipo_de_dato == "vendedores":
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                while True:
                    cargar = input(f"{mensaje} fila {i} columna {j} {lista_columnas[j]}: ")
                    matriz[i][j] = cargar
                    break

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

                print(f"\t {matriz_vendedores[i][j]}:   ${matriz_ventas[i][j]} ")



# resultado = buscar_vendedor_maximo(matriz_vendedores, matriz_ventas)

def buscar_zona_maximo(matriz_ventas: list, depositos: list) -> None:
    """
    Esta funcion recibe por parámetro una matriz de ventas [vendedores],zonas]
    y muestra las zonas donde la recaudacion total supera los 2.000.000.
    """

    cantidad_depositos = len(matriz_ventas[0])
    cantidad_vendedores = len(matriz_ventas)

    print("Zonas con ventas superiores a $2.000.000:")

    for j in range(cantidad_depositos):
        total_de_la_zona = 0
        for i in range(cantidad_vendedores): 
            total_de_la_zona += matriz_ventas[i][j]

        if total_de_la_zona > 2_000_000:
            print(f"- {depositos[j]} (Total recaudado: ${total_de_la_zona})")


# resultado2 = buscar_zona_maximo(matriz_ventas,depositos)

def mostrar_mejores_vendedores(matriz_ventas: list,
                              matriz_vendedores:list,
                              vendedor:list,
                              depositos:list) -> None:
    """
    Esta funcion recibe por parámetro una matriz de ventas
    y muestra los mejores vendedores por zona
    """
    cantidad_vendedores = len(matriz_ventas)
    cantidad_de_zonas = len(matriz_ventas[0])
    
    if cantidad_vendedores != len(vendedor):
        print("Error: la cantidad de filas en la matriz de ventas no coincide con la cantidad de vendedores.")
        return
    
    mejor_vendedor = ["0"] * len(vendedor)

    print("Mejores vendedores por zona:")
    for j in range(cantidad_de_zonas):
        venta_maxima = -1
        

        for i in range(cantidad_vendedores):
            if matriz_ventas[i][j] > venta_maxima:
                venta_maxima = matriz_ventas[i][j]
                mejor_vendedor[j] = matriz_vendedores[i][j]
        
        print(f"En {depositos[j]}: {mejor_vendedor[j]} (${venta_maxima})")

    return 
# probar = mostrar_mejores_vendedores(matriz_ventas, depositos,vendedor)

# print(probar)

def agregar_indice(matriz_cargada:list,
                   depositos:list,
                   vendedores:list)-> list:
    """
    Esta funcion recibe una matriz por parametro, los depositos y los vendedores
    devuelve una matriz con la primer fila mostrando los depositos y la primer columna 
    mostrando los vendedores
    """

    for i in range(len(matriz_cargada)+1):
        for j in range(len(matriz_cargada[0])+1):
            if i == 0 and j == 0:
                print(end="  ")
            elif i == 0 and j > 0:
                print(f"{depositos[j - 1]}", end="  ")
            elif i > 0:
                if j == 0:
                    print(f"{vendedores[i - 1]}", end="  ")
                else:
                    print("", matriz_cargada[i-1][j-1], end="\t")
        
        print("  ")
    
    return matriz_cargada

def calcular_largo(matriz)->list: 
    maximo = 0 
    for i in range(len(matriz)):#ejemplo 10
        for j in range(len(matriz[0])):#

                if len(matriz[i][j])>maximo:
                    maximo = len(matriz[i][j])

    for i in range(len(matriz)):#ejemplo 10
        for j in range(len(matriz[0])):#ejemplo 10

            while len(matriz[i][j]) < maximo:

                matriz[i][j] += " "
    return matriz
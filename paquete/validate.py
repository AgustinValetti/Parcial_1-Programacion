def validar_rango(dato:int, max:int, min:int)->int:

    '''
    Valida un entero para el menu de opciones
    '''

    while dato > max or dato < min:
        dato = int(input(f"Porfavor ingrese un numero valio entre {min} y {max}:"))
    return dato
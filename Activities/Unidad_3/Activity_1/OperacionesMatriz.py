# LECTURA DE X MATRICEZ
def crearMatriz(filas: int, columnas: int):
    matriz = []
    for i in range(int(filas)):
        matriz.append([i]*int(columnas))
    return matriz

# PROCESOS


def pedirDatosMatriz(direccion: str, item: int, error: str):
    mensajeNumero = f"Digite la cantidad total de {direccion} que desea ingresar en la matriz #{item + 1}: "
    return catarNumeroEntero(mensajeNumero, error)

# ENTRADAS


def catarNumeroEntero(message: str, error: str):
    whilevalidation = False
    while not whilevalidation:
        number = input(f"{message}")
        whilevalidation = number.isdigit()
        if not whilevalidation:
            print(f"{error}")
        else:
            return int(number)


def llenarMatriz(matriz: list, error: str, numeroDeMatriz: int):
    for item in range(len(matriz)):
        for element in range(len(matriz[item])):
            mensajePosicionesMatriz = f"Digite el dato de la posicion {item} {element} en la matriz #{numeroDeMatriz + 1}:"
            matriz[item][element] = catarNumeroEntero(
                mensajePosicionesMatriz, error)
    return matriz


def inicioPrograma(mensajeNumeroMatricez: str, error: str, filas: str, columnas: str):
    listaDeMatricez = []
    for item in range(catarNumeroEntero(mensajeNumeroMatricez, error)):
        listaDeMatricez.append(llenarMatriz(crearMatriz(pedirDatosMatriz(
            filas, item, error), pedirDatosMatriz(columnas, item, error)), error, item))
    return listaDeMatricez


mensajeFilas = "Filas"
mensajeColumnas = "Columnas"
mensajeError = "Por favor digite un número entero"
mensajeNumeroMatricez = "Digite la cantidad de matricez que desea crear: "
print("===============================================")
listaMatricesz = inicioPrograma(mensajeNumeroMatricez, mensajeError,
                                mensajeFilas, mensajeColumnas)

# SALIDAS
print("Las matricez quedaron de las siguiente forma: ")
for item in range(len(listaMatricesz)):
    print("Matriz #", item + 1)
    for i in listaMatricesz[item]:
        print('  '.join(map(str, i)))
print("===============================================")

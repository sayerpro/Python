import os
import math

coordinatesList = []


def option2():
    if coordinatesList == [] and len(coordinatesList) == 0:
        print("A continuación se le pedira ingresar 3 sets de coordenadas")
        for i in range(3):
            coordinatesList.append([i]*2)
            llenarCoordenadas(i, True)

        validateCoordinates(coordinatesList, False)
    else:
        # RF03: El programa permite al usuario actualizar las coordenadas de los tres sitios más frecuentados.
        calcularOrientacionCoordenadas(coordinatesList)
        optionCondition5 = False
        while not optionCondition5:
            print("Presione 1, 2 o 3 para actualizar la respectiva coordenada")
            changeDecision = input("Presione 0 para regresar al menú: ")
            optionCondition5 = changeDecision.isdigit()
            if not optionCondition5:
                print("Por favor digite un número entero")
        if int(changeDecision) in range(*[1, 4]):
            llenarCoordenadas(int(changeDecision) - 1, False)
            validateCoordinates(coordinatesList, True)
        elif changeDecision == "0":
            pass
        else:
            print("Error actualización")
            exit()


def calcularOrientacionCoordenadas(coordinatesList: list):
    nort = float("0")
    nortPosition = float("0")
    south = float("0")
    southPosition = float("0")
    east = float("0")
    eastPosition = float("0")
    west = float("0")
    westPosition = float("0")
    zeroFloat = float("0")

    for a in range(len(coordinatesList)):
        print(
            f"Coordenada [latitud, longitud] {a + 1}: {coordinatesList[a]}")

        latitud = float(coordinatesList[a][0])
        longitud = float(coordinatesList[a][1])
        count = a + 1

        if nort == zeroFloat:
            nort = latitud
            nortPosition = count
        if south == zeroFloat:
            south = latitud
            southPosition = count
        if east == zeroFloat:
            east = longitud
            eastPosition = count
        if west == zeroFloat:
            west = longitud
            westPosition = count

        if a > 0:
            if latitud >= nort:
                nort = latitud
                nortPosition = count
            if latitud < zeroFloat:
                if south > zeroFloat:
                    south = latitud
                    southPosition = count
                elif latitud > south:
                    south = latitud
                    southPosition = count
            elif south < zeroFloat:
                pass
            elif latitud > south:
                south = latitud
                southPosition = count

            if longitud >= east:
                east = longitud
                eastPosition = count
            if longitud < zeroFloat:
                if west > zeroFloat:
                    west = longitud
                    westPosition = count
                elif longitud < west:
                    west = longitud
                    westPosition = count
            elif west < zeroFloat:
                pass
            elif longitud > west:
                west = longitud
                westPosition = count

    print("La coordenada #", southPosition, " es la que esta mas al sur")
    print("La coordenada #", eastPosition, " es la que esta mas al oriente")


def llenarCoordenadas(i: int, mesaggeCondition: bool):
    if mesaggeCondition:
        print("Set de coordenadas #", i + 1)
    else:
        print("Set de coordenadas #", i)
    optionCondition4 = False
    while not optionCondition4:
        latitude = input("Digite la latitud: ")
        optionCondition4 = validarFlotante(latitude)

    optionCondition5 = False
    while not optionCondition5:
        length = input("Digite la longitud: ")
        optionCondition5 = validarFlotante(length)

    coordinatesList[i][0] = latitude
    coordinatesList[i][1] = length


def validarFlotante(number: str):
    try:
        if not number or number == "0":
            print("Error coordenada")
            exit()
        number = float(number)
        return True
    except ValueError:
        print("Por favor digite un número decimal")
        return False


def validateCoordinates(coordinatesList: list, update: bool):
    latitud = False
    longitud = False
    c = 0
    c2 = 0
    for a in range(len(coordinatesList)):
        for b in range(len(coordinateMatriz) - 1):
            b += 1
            for a2 in range(len(coordinatesList[a])):
                for b2 in range(len(coordinateMatriz[b]) - 2):
                    b2 += 2
                    coordinatesCube = coordinateMatriz[b][b2].split("/")
                    if float(coordinatesList[a][a2]) >= float(coordinatesCube[0]) and float(coordinatesList[a][a2]) <= float(coordinatesCube[1]) or coordinatesList[a][a2] >= coordinatesCube[0] and coordinatesList[a][a2] <= coordinatesCube[1]:
                        if a2 == 0:
                            latitud = True
                        else:
                            longitud = True
                    coordinatesConfirm = latitud and longitud
                    if coordinatesConfirm and c == 0 and c2 == 0:
                        c = b
                        c2 = b2
        if not coordinatesConfirm:
            if update:
                print("Error coordenada")
            else:
                print("Error")
            exit()
            # print(
            #     f"La coordenadas ingresadas en la posición {a} / Latitud: {coordinatesList[a][a2 - 1]} - Longitud: {coordinatesList[a][a2]} no estan dentro del rango de coordenadas disponibles")
        # else:
            # print(
            #     f"La coordenadas ingresadas en la posición {a} / Latitud: {coordinatesList[a][a2 - 1]} - Longitud: {coordinatesList[a][a2]} fueron validadas con EXITO")
            # print(
            #     f"Se encontraron en la posición {c} / Latitud: {coordinateMatriz[c][c2 - 1]} - Longitud: {coordinateMatriz[c][c2]}")
        latitud = False
        longitud = False
        c = 0
        c2 = 0


def option3():
    # RF02: El programa permite al usuario encontrar dos (2)zonas wifi más cercanas asu ubicación y saber en cuál de estas hay menos personas conectadas
    for a in range(len(coordinatesList)):
        print(
            f"Coordenada [latitud, longitud] {a + 1}: {coordinatesList[a]}")
    optionCondition6 = False
    while not optionCondition6:
        option = input(
            "Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión: ")
        optionCondition6 = option.isdigit()
        if not optionCondition6:
            print("Por favor digite un número entero")
    if int(option) in range(*[1, 4]):
        listaDistancia = manejoCoorenadas(int(option))
        listaDistanciasCercanas = ordenarDistancia(
            listaDistancia, listaDistancia)
        optionCondition7 = False
        while not optionCondition7:
            option2 = input(
                "Elija 1 o 2 para recibir indicaciones de llegada: ")
            optionCondition7 = option2.isdigit()
            if not optionCondition7:
                print("Por favor digite un número entero")
        if int(option2) in range(*[1, 3]):
            indicaciones(listaDistanciasCercanas[0], int(
                option2), int(option), coordenadasPreedefinidas[1])
            optionCondition8 = False
            while not optionCondition8:
                option3 = input(
                    "Presione 0 para salir: ")
                optionCondition8 = option3.isdigit()
                if not optionCondition8 or int(option3) != 0:
                    optionCondition8 = False
                    print("Por favor digite el número según la opción")
        else:
            print("Error zona wifi")
            exit()
    else:
        print("Error ubicación")
        exit()


def manejoCoorenadas(option: int):
    listaCoordenadasPredefinidasRadianes = coordenadasPreedefinidas
    for a in range(len(listaCoordenadasPredefinidasRadianes)):
        for b in range(2):
            listaCoordenadasPredefinidasRadianes[a][b] = math.radians(
                coordenadasPreedefinidas[a][b])
    latitud = math.radians(float(coordinatesList[option - 1][0]))
    longitud = math.radians(float(coordinatesList[option - 1][1]))
    listaDistancias = []
    for i in range(len(coordenadasPreedefinidas)):
        latitudPredefinida = coordenadasPreedefinidas[i][0]
        longitudPredefinida = coordenadasPreedefinidas[i][1]
        latitudDelta = latitudPredefinida - latitud
        longitudDelta = longitudPredefinida - longitud
        distancia = (2*radioTierra) * math.asin(math.sqrt((math.sin(latitudDelta/2)**2) +
                                                          ((math.sin(longitudDelta/2)**2) * (math.cos(latitud)) * (math.cos(latitudPredefinida)))))
        distancia = round(distancia)
        listaDistancias.append(distancia*1000)
    return listaDistancias


def ordenarDistancia(listaDistancias: list, listaDistancia: list):
    minimo1 = listaDistancias.index(min(listaDistancias))
    listaDistancias.pop(minimo1)
    minimo2 = listaDistancias.index(min(listaDistancias))
    listaDistancias.pop(minimo2)
    for a in range(len(coordenadasPreedefinidas)):
        for b in range(2):
            coordenadasPreedefinidas[a][b] = math.degrees(
                coordenadasPreedefinidas[a][b])
    print("Zonas wifi cercanas con menos usuarios")
    if coordenadasPreedefinidas[minimo1][2] < coordenadasPreedefinidas[minimo2][2]:
        print(
            f"La zona wifi 1: ubicada en ['{coordenadasPreedefinidas[minimo1][0]}' - '{coordenadasPreedefinidas[minimo1][1]}'] a '{listaDistancia[0]}' metros, tiene en promedio '{coordenadasPreedefinidas[minimo1][2]}' usuarios")
        print(
            f"La zona wifi 2: ubicada en ['{coordenadasPreedefinidas[minimo2][0]}' - '{coordenadasPreedefinidas[minimo2][1]}'] a '{listaDistancia[1]}' metros, tiene en promedio '{coordenadasPreedefinidas[minimo2][2]}' usuarios")
    else:
        print(
            f"La zona wifi 1: ubicada en ['{coordenadasPreedefinidas[minimo2][0]}' - '{coordenadasPreedefinidas[minimo2][1]}'] a '{listaDistancia[1]}' metros, tiene en promedio '{coordenadasPreedefinidas[minimo2][2]}' usuarios")
        print(
            f"La zona wifi 2: ubicada en ['{coordenadasPreedefinidas[minimo1][0]}' - '{coordenadasPreedefinidas[minimo1][1]}'] a '{listaDistancia[0]}' metros, tiene en promedio '{coordenadasPreedefinidas[minimo1][2]}' usuarios")
    return [listaDistancias, coordenadasPreedefinidas]

# RF03: Elprograma indica al usuario en qué dirección está ubicada la coordenada el punto de acceso wifi elegidoy cuál es el tiempo promedio para llegar hasta ese lugar.


def indicaciones(listaDistanciasCercanas: list, option: int, actual: int, coordenadasPreedefinidas: list):
    latitudOrigen = float(coordinatesList[actual - 1][0])
    longitudOrigen = float(coordinatesList[actual - 1][1])
    latitudDestino = coordenadasPreedefinidas[0]
    longitudDestino = coordenadasPreedefinidas[1]
    if option == 1:
        tiempoMoto = listaDistanciasCercanas[0]/19.44
        tiempoBici = listaDistanciasCercanas[0]/3.33
    else:
        tiempoMoto = listaDistanciasCercanas[1]/19.44
        tiempoBici = listaDistanciasCercanas[1]/3.33

    vertical = ""
    if latitudOrigen > latitudDestino:
        vertical = "debe dirigirse primero al Occidente"
    elif latitudDestino > latitudOrigen:
        vertical = "debe dirigirse primero al Oriente"
    else:
        vertical = "no se mueva de este eje vertical"
    horizontal = ""
    if longitudOrigen > longitudDestino:
        horizontal = "luego al Sur"
    elif longitudDestino < longitudOrigen:
        horizontal = "luego al Norte"
    else:
        horizontal = "no se mueva de este eje Horizontal"

    print("Para llegar a la zona wifi ", vertical, " y ", horizontal)
    unidadTiempoMoto = "segundos"
    if tiempoMoto > 60:
        tiempoMoto = tiempoMoto/60
        unidadTiempoMoto = "minutos"

    unidadTiempoBici = "segundos"
    if tiempoBici > 60:
        tiempoBici = tiempoBici/60
        unidadTiempoBici = "minutos"

    print("Tiempo en moto: ", round(tiempoMoto, 2), unidadTiempoMoto)
    print("Tiempo en bici: ", round(tiempoBici, 2), unidadTiempoBici)

# RETO 1
# Requisitos funcionales
# RF01 El programa dispone de un mensaje de bienvenida al sistema previo a la solicitud de las credenciales de acceso.
# print("Bienvenido al sistema de ubicación para zonas públicas WIFI")


# RF02  El programa dispone de un usuario y una contraseña predefinidos para el inicio de sesión en consola
userInput = input("Usuario: ")
user = "51745"
if userInput != user:
    print("Error")
    exit()

passwordInput = input("Contraseña: ")
password = "54715"
if passwordInput != password:
    print("Error")
    exit()

# RF03 El programa dispone de un captcha de seguridad que confirma que el inicio de sesión corresponde a un usuario.
codigoOne = 748
codigoTwo = 4*5 % 7 - 5
captchaInput = int(input(f"{codigoOne} + {codigoTwo}= "))
captcha = codigoOne + codigoTwo
if captchaInput != captcha:
    print("Error")
    exit()
else:
    # RF04 El programa confirma el ingreso al sistema con un mensaje de éxito en el inicio de sesión
    print("Sesión iniciada")

# Este código inplementa una funcionde python
# Interpolación de cadena literal (f"")
# https://www.python.org/dev/peps/pep-0498/#:~:text=F%2Dstrings%20provide%20a%20way,literals%2C%20using%20a%20minimal%20syntax.&text=In%20Python%20source%20code%2C%20an,are%20replaced%20with%20their%20values.

# RETO 2
# Este código inplementa una importación, paquete de python (os)
# Requisitos funcionales
# RF01: El programa muestra el siguientemenú de opcionesen consolapara el uso del programa
mesaggeOne = "1. Cambiar contraseña"
mesaggeTwo = "2. Ingresar coordenadas actuales"
mesaggeThree = "3. Ubicar zona wifi más cercana"
mesaggeFour = "4. Guardar archivo con ubicación cercana"
mesaggeFive = "5. Actualizar registros de zonas wifi desde archivo"
mesaggeSix = "6. Elegir opción de menú favorita"
mesaggeSeven = "7. Cerrar sesión"

optionOne = mesaggeOne
optionTwo = mesaggeTwo
optionThree = mesaggeThree
optionFour = mesaggeFour
optionFive = mesaggeFive
optionSix = mesaggeSix
optionSeven = mesaggeSeven

restartMenu = True
viewLastOptions = True
changeOptions = False
viewMenu = True
countErrors = 0
riddleOneValidation = "4"
riddleTwoValidation = "3"
coordinateMatriz = [["Digito grupo", "Municipio", "Latitud", "Longitud"],
                    ["0", "Leticia, Amazonas", "-3.002/-4.227", "-69.714/-70.365"],
                    ["1", "Calamar, Bolívar", "6.077/6.284", "-75.841/-76.049"],
                    ["2", "Betulia, Antioquia", "10.103/10.362", "-74.918/-75.088"],
                    ["3", "Chita, Boyacá", "5.888/6.306", "-72.321/-72.552"],
                    ["4", "Cajibio, Cauca", "2.548/2.766", "-76.493/-76.879"],
                    ["5", "La paz, Cesar", "9.757/10.462", "-72.987/-73.623"],
                    ["6", "Tadó, Chocó", "5.119/5.413", "-76.132/-76.619"],
                    ["7", "Suaza, Huila", "1.740/1.998", "-75.689/-75.950"],
                    ["8", "Ortega, Tolima", "3.746/4.120", "-75.075/-75.443"],
                    ["9", "Curití, Santander", "6.532/6.690", "-72.872/-73.120"]]
cardinalCoordinateMatriz = [["Digito grupo", "Información clave"],
                            ["0", "-Coordenada ubicada más al norte/-Coordenada ubicada más al sur"],
                            ["1", "-Coordenada ubicada más al norte/-Coordenada ubicada más al oriente"],
                            ["2", "-Coordenada ubicada más al norte/-Coordenada ubicada más al occidente"],
                            ["3", "-Coordenada ubicada más al norte/-Coordenada promedio de todos los puntos."],
                            ["4", "-Coordenada ubicada más al sur/-Coordenada promedio de todos los puntos."],
                            ["5", "-Coordenada ubicada más al sur/-Coordenada ubicada más al oriente"],
                            ["6", "-Coordenada ubicada más al sur/-Coordenada ubicada más al occidente"],
                            ["7", "-Coordenada ubicada más al oriente/-Coordenada ubicada más al occidente"],
                            ["8", "-Coordenada ubicada más al oriente/-Coordenada promedio de todos los puntos."],
                            ["9", "-Coordenada ubicada más al occidente/-Coordenada promedio de todos los puntos."]]
# RETO 4
# Requisitos funcionales
# RF01: El programa dispone de manera predefinida la ubicación de cuatro zonas wifi con su respectivo promedio de usuarios
coordenadasPreedefinidas = [[2.698, -76.680, 63],
                            [2.724, -76.693, 20],
                            [2.606, -76.742, 680],
                            [2.698, -76.680, 64]]
radioTierra = 6372.795477598
while restartMenu:
    if viewMenu:
        if not viewLastOptions:
            print(mesaggeOne)
            print(mesaggeTwo)
            print(mesaggeThree)
            print(mesaggeFour)
            print(mesaggeFive)
        else:
            print(optionOne)
            print(optionTwo)
            print(optionThree)
            print(optionFour)
            print(optionFive)
        if viewLastOptions:
            print(optionSix)
            print(optionSeven)
    if viewLastOptions:
        changeOptions = False
        optionCondition = False
        while not optionCondition:
            menuInput = input("Elija una opción: ")
            optionCondition = menuInput.isdigit()
            if not optionCondition:
                print("Por favor digite un número entero.")
    else:
        optionCondition2 = False
        while not optionCondition2:
            menuInput = input("Seleccione opción favorita: ")
            optionCondition2 = menuInput.isdigit()
            if not optionCondition2:
                print("Por favor digite un número entero.")

    # RF02: El programa permite elegir una opción del menú como favorito.
    rangeNum = int(menuInput) in range(*[1, 8])
    if not rangeNum:
        # RF03: El programa genera una alerta si el usuario elige una opción incorrecta
        if viewLastOptions:
            print("Error")
            viewMenu = False
            countErrors += 1
            if countErrors == 3:
                exit()
        else:
            print("Error")
            exit()

    # RETO 3
    # Requisitos funcionales
    # RF01: El programa permite al usuario actualizar su contraseña.
    if menuInput == "1" and viewLastOptions:
        confirmPassword = input("Digite la contraseña actual: ")
        if confirmPassword == password:
            optionCondition3 = False
            while not optionCondition3:
                newPassword = input("Digite su nueva contraseña: ")
                optionCondition3 = newPassword != password
                if optionCondition3:
                    password = newPassword
                else:
                    print(
                        "Por favor asegurese de que la nueva contraseña sea diferente a la actual")
        else:
            print("Error")
            exit()
    elif menuInput == "2" and viewLastOptions:
        # RF02: Elprograma permite al usuario ingresar lascoordenadasde los tres sitios que más frecuenta (trabajo, casa, parque).
        option2()
    elif menuInput == "3" and viewLastOptions:
        if coordinatesList == []:
            print("Error sin registro de coordenadas")
            exit()
        option3()
    elif menuInput == "6" or changeOptions:
        viewMenu = True
        if rangeNum:
            viewLastOptions = False
        if changeOptions:
            if not int(menuInput) in range(*[1, 6]):
                print("Error")
                exit()
            viewLastOptions = True
            riddleOneInput = input(
                # Se toma la ecision de comentar esta adivinanza ya que el validador de la plataforma no toma el número 9 y en vez de ello ingresa un 4
                # "Para confirmar por favor responda:Si me giras pierdo tres unidades por eso debes colocarme siempre de pie, la respuesta es: "
                "Para confirmar por favor responda:Soy el mejor amigo del hombre, tengo cola y siempre estoy feliz cuantas patas tengo?, la respuesta es: ")
            if not riddleOneInput == riddleOneValidation:
                print("Error")
            else:
                riddleTwoInput = input(
                    "Para confirmar por favor responda:Me separaron de mi hermano siamés, antes era un ocho y ahora soy un...la respuesta es: ")
                if not riddleTwoInput == riddleTwoValidation:
                    print("Error")
                else:
                    # Si bien no es necesario considerar y reorganizar todos los mensajes para el RETO 2 se hizo pensando en la escalabiliad de la applicación
                    if menuInput == "1":
                        optionOne = mesaggeOne
                        optionTwo = mesaggeTwo
                        optionThree = mesaggeThree
                        optionFour = mesaggeFour
                        optionFive = mesaggeFive
                    elif menuInput == "2":
                        optionOne = mesaggeTwo
                        optionTwo = mesaggeOne
                        optionThree = mesaggeThree
                        optionFour = mesaggeFour
                        optionFive = mesaggeFive
                    elif menuInput == "3":
                        optionOne = mesaggeThree
                        optionTwo = mesaggeOne
                        optionThree = mesaggeTwo
                        optionFour = mesaggeFour
                        optionFive = mesaggeFive
                    elif menuInput == "4":
                        optionOne = mesaggeFour
                        optionTwo = mesaggeOne
                        optionThree = mesaggeTwo
                        optionFour = mesaggeThree
                        optionFive = mesaggeFive
                    elif menuInput == "5":
                        optionOne = mesaggeFive
                        optionTwo = mesaggeOne
                        optionThree = mesaggeTwo
                        optionFour = mesaggeThree
                        optionFive = mesaggeFour

                    systemName = os.name
                    if systemName == "ce" or systemName == "nt" or systemName == "dos":
                        os.system("cls")
                    elif systemName == "posix" or systemName == "mac":
                        os.system("clear")
                    elif systemName == "java":
                        os.system.out.flush()
                    # RF04: El programa permite acceder a las opciones del menú
                    viewLastOptions = True
        changeOptions = True
    elif menuInput == "7":
        # RF05: El programa permite al usuario salir del menú
        print("Hasta pronto")
        exit()
    else:
        if rangeNum:
            print("Usted ha elegido la opción", menuInput)
            exit()

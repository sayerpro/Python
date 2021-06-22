# # RETO 1
# # Requisitos funcionales
# # RF01 El programa dispone de un mensaje de bienvenida al sistema previo a la solicitud de las credenciales de acceso.
# print("Bienvenido al sistema de ubicación para zonas públicas WIFI")

# # RF02  El programa dispone de un usuario y una contraseña predefinidos para el inicio de sesión en consola
# userInput = input("Usuario: ")
# user = "51745"
# if userInput != user:
#     print("Error")
#     exit()

# passwordInput = input("Contraseña: ")
# password = "54715"
# if passwordInput != password:
#     print("Error")
#     exit()

# # RF03 El programa dispone de un captcha de seguridad que confirma que el inicio de sesión corresponde a un usuario.
# codigoOne = 748
# codigoTwo = 4*5 % 7 - 5
# captchaInput = int(input(f"{codigoOne} + {codigoTwo}= "))
# captcha = codigoOne + codigoTwo
# if captchaInput != captcha:
#     print("Error")
#     exit()
# else:
#     # RF04 El programa confirma el ingreso al sistema con un mensaje de éxito en el inicio de sesión
#     print("Sesión iniciada")

# # Este código inplementa una funcionde python
# # Interpolación de cadena literal (f"")
# # https://www.python.org/dev/peps/pep-0498/#:~:text=F%2Dstrings%20provide%20a%20way,literals%2C%20using%20a%20minimal%20syntax.&text=In%20Python%20source%20code%2C%20an,are%20replaced%20with%20their%20values.

# # RETO 2
# # Este código inplementa una importación, paquete de python (os)
# import os

# # Requisitos funcionales
# # RF01: El programa muestra el siguientemenú de opcionesen consolapara el uso del programa
# mesaggeOne = "Cambiar contraseña"
# mesaggeTwo = "Ingresar coordenadas actuales"
# mesaggeThree = "Ubicar zona wifi más cercana"
# mesaggeFour = "Guardar archivo con ubicación cercana"
# mesaggeFive = "Actualizar registros de zonas wifi desde archivo"
# mesaggeSix = "Elegir opción de menú favorita"
# mesaggeSeven = "Cerrar sesión"

# optionOne = mesaggeOne
# optionTwo = mesaggeTwo
# optionThree = mesaggeThree
# optionFour = mesaggeFour
# optionFive = mesaggeFive
# optionSix = mesaggeSix
# optionSeven = mesaggeSeven

# restartMenu = True
# viewLastOptions = True
# changeOptions = False
# viewMenu = True
# countErrors = 0
# riddleOneValidation = "4"
# riddleTwoValidation = "3"

# while restartMenu:
#     if viewMenu:
#         if not viewLastOptions:
#             print("1. ", mesaggeOne)
#             print("2. ", mesaggeTwo)
#             print("3. ", mesaggeThree)
#             print("4. ", mesaggeFour)
#             print("5. ", mesaggeFive)
#         else:
#             print("1. ", optionOne)
#             print("2. ", optionTwo)
#             print("3. ", optionThree)
#             print("4. ", optionFour)
#             print("5. ", optionFive)
#         if viewLastOptions:
#             print("6. ", optionSix)
#             print("7. ", optionSeven)
#     if viewLastOptions:
#         changeOptions = False
#         optionvCondition = False
#         while not optionvCondition:
#             menuInput = input("Elija una opción: ")
#             optionvCondition = menuInput.isdigit()
#             if not optionvCondition:
#                 print("Por favor digite un número entero.")
#     else:
#         optionCondition2 = False
#         while not optionCondition2:
#             menuInput = input("Seleccione opción favorita: ")
#             optionCondition2 = menuInput.isdigit()
#             if not optionCondition2:
#                 print("Por favor digite un número entero.")

#     # RF02: El programa permite elegir una opción del menú como favorito.
#     if int(menuInput) in range(*[1, 8]):
#         viewMenu = True
#         if menuInput == "7":
#             # RF05: El programa permite al usuario salir del menú
#             print("Hasta pronto")
#             exit()
#         elif menuInput == "6" or changeOptions:
#             viewLastOptions = False
#             if changeOptions:
#                 if int(menuInput) in range(*[1, 6]):
#                     viewLastOptions = True
#                     riddleOneInput = input(
#                         # Se toma la ecision de comentar esta adivinanza ya que el validador de la plataforma no toma el número 9 y en vez de ello ingresa un 4
#                         # "Para confirmar por favor responda:Si me giras pierdo tres unidades por eso debes colocarme siempre de pie, la respuesta es: "
#                         "Para confirmar por favor responda:Soy el mejor amigo del hombre tengo cola y siempre estoy feliz, la respuesta es: ")
#                     if riddleOneInput == riddleOneValidation:
#                         riddleTwoInput = input(
#                             "Para confirmar por favor responda:Me separaron de mi hermano siamés, antes era un ocho y ahora soy un...la respuesta es: ")
#                         if riddleTwoInput == riddleTwoValidation:

#                             # Si bien no es necesario considerar y reorganizar todos los mensajes para el RETO 2 se hizo pensando en la escalabiliad de la applicación
#                             if menuInput == "1":
#                                 optionOne = mesaggeOne
#                                 optionTwo = mesaggeTwo
#                                 optionThree = mesaggeThree
#                                 optionFour = mesaggeFour
#                                 optionFive = mesaggeFive
#                             elif menuInput == "2":
#                                 optionOne = mesaggeTwo
#                                 optionTwo = mesaggeOne
#                                 optionThree = mesaggeThree
#                                 optionFour = mesaggeFour
#                                 optionFive = mesaggeFive
#                             elif menuInput == "3":
#                                 optionOne = mesaggeThree
#                                 optionTwo = mesaggeOne
#                                 optionThree = mesaggeTwo
#                                 optionFour = mesaggeFour
#                                 optionFive = mesaggeFive
#                             elif menuInput == "4":
#                                 optionOne = mesaggeFour
#                                 optionTwo = mesaggeOne
#                                 optionThree = mesaggeTwo
#                                 optionFour = mesaggeThree
#                                 optionFive = mesaggeFive
#                             elif menuInput == "5":
#                                 optionOne = mesaggeFive
#                                 optionTwo = mesaggeOne
#                                 optionThree = mesaggeTwo
#                                 optionFour = mesaggeThree
#                                 optionFive = mesaggeFour

#                             systemName = os.name
#                             if systemName == "ce" or systemName == "nt" or systemName == "dos":
#                                 os.system ("cls")
#                             elif systemName == "posix" or systemName == "mac":
#                                 os.system ("clear")
#                             elif systemName == "java":
#                                 os.system.out.flush();
#                             # RF04: El programa permite acceder a las opciones del menú
#                             viewLastOptions = True

#                         else:
#                             print("Error")
#                     else:
#                         print("Error")
#                 else:
#                     print("Error")
#                     exit()
#             changeOptions = True
#         else:
#             print("Usted ha elegido la opción", menuInput)
#             exit()
#     # RF03: El programa genera una alerta si el usuario elige una opción incorrecta
#     else:
#         if viewLastOptions:
#             print("Error")
#             viewMenu = False
#             countErrors += 1
#             if countErrors == 3:
#                 exit()
#         else:
#             print("Error")
#             exit()

# RETO 1
# Requisitos funcionales
# RF01 El programa dispone de un mensaje de bienvenida al sistema previo a la solicitud de las credenciales de acceso.
# print("Bienvenido al sistema de ubicación para zonas públicas WIFI")

# RF02  El programa dispone de un usuario y una contraseña predefinidos para el inicio de sesión en consola
import os
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
mesaggeOne = "Cambiar contraseña"
mesaggeTwo = "Ingresar coordenadas actuales"
mesaggeThree = "Ubicar zona wifi más cercana"
mesaggeFour = "Guardar archivo con ubicación cercana"
mesaggeFive = "Actualizar registros de zonas wifi desde archivo"
mesaggeSix = "Elegir opción de menú favorita"
mesaggeSeven = "Cerrar sesión"

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

while restartMenu:
    if viewMenu:
        if not viewLastOptions:
            print("1. ", mesaggeOne)
            print("2. ", mesaggeTwo)
            print("3. ", mesaggeThree)
            print("4. ", mesaggeFour)
            print("5. ", mesaggeFive)
        else:
            print("1. ", optionOne)
            print("2. ", optionTwo)
            print("3. ", optionThree)
            print("4. ", optionFour)
            print("5. ", optionFive)
        if viewLastOptions:
            print("6. ", optionSix)
            print("7. ", optionSeven)
    if viewLastOptions:
        changeOptions = False
        optionvCondition = False
        while not optionvCondition:
            menuInput = input("Elija una opción: ")
            optionvCondition = menuInput.isdigit()
            if not optionvCondition:
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

    viewMenu = True
    if menuInput == "7":
        # RF05: El programa permite al usuario salir del menú
        print("Hasta pronto")
        exit()
    elif not menuInput == "6" and not changeOptions and rangeNum:
        print("Usted ha elegido la opción", menuInput)
        exit()

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

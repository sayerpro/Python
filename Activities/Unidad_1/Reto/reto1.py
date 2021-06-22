# RETO 1
# Requisitos funcionales
# RF01 El programa dispone de un mensaje de bienvenida al sistema previo a la solicitud de las credenciales de acceso.
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")

# RF02  El programa dispone de un usuario y una contraseña predefinidos para el inicio de sesión en consola
userInput = input("Usuario: ")
user = "51745"
if userInput != user:
    print("Error")
    exit()

passwordInput = input("Contraseña: ")
password = "45715"
if passwordInput != password:
    print("Error")
    exit()

# RF03 El programa dispone de un captcha de seguridad que confirma que el inicio de sesión corresponde a un usuario.
codigoOne = 749
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

# Este logica la desarrolle despues de ver mi código y ver si lo podría de hacer de otra forma
# Si bien considero que esta forma es mas eficiente ya que descarta todo el código en caso de no entrar a los condicionales if
# Me gusto experimentar con el exit() y funciona tal y como se especifica en el RETO 1

# userInput = input("Usuario: ")
# user =  "51593"
# if userInput == user:
#     passwordInput = input("Contraseña: ")
#     password = "39515"
#     if passwordInput == password:
#         codigoOne = 593
#         codigoTwo = (3%5)+5+1
#         captchaInput = int(input(f"{codigoOne} + {codigoTwo}= "))
#         captcha = codigoOne + codigoTwo
#         if captchaInput == captcha:
#             print("Sesión iniciada")
#         else:
#             print("Error")
#     else:
#         print("Error")
# else:
#     print("Error")

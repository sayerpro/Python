from io import open

archivo = open("archivo.txt", "w")
frase = "Escribiendo el python\n"
archivo.write(frase)
archivo.close
archivo = open("archivo.txt", "a")
frase = "Escribiendo el python 2\n"
archivo.write(frase)
archivo.close
archivo = open("archivo.txt", "r")
print(archivo.read())
archivo.close
archivo = open("archivo.txt", "r")
frase = "Escribiendo el python 2\n"
print(archivo.readlines())
archivo.close

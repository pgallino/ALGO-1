
"""Escribir una función, llamada rot13, que reciba un archivo de texto de origen
y uno de destino, de modo que para cada línea del archivo origen, se guarde una línea cifrada
en el archivo destino. El algoritmo de cifrado a utilizar será muy sencillo: a cada caracter com-
prendido entre la a y la z, se le suma 13 y luego se aplica el módulo 26, para obtener un nuevo
caracter.

Por ejemplo, el contenido del archivo origen es:

escribir una funcion, rot13
que reciba un archivo de texto

El archivo destino debe tener:

rfpevove han shapvba, ebg13
dhr erpvon ha nepuvib qr grkgb"""


def rot13(archivo_origen, archivo_destino):
    with open(archivo_origen) as origen, open(archivo_destino, "w") as destino:
            for linea in origen:
                linea.rstrip("\n")
                codificado = ""

                for caracter in linea:
                    if 96 < ord(caracter) < 110:
                        codificado += chr(ord(caracter)+13)
                    elif 109 < ord(caracter) < 123:
                        codificado += chr(97 + (13 - (123 - ord(caracter))))
                    else:
                        codificado += caracter

                destino.write(codificado)
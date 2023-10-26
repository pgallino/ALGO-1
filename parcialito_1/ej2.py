# 2. Un crucigrama es una matriz de nxm que contiene celdas.
# Las celdas son tuplas de dos elementos de la forma `(<color>, <contenido>)`.
# Cada celda puede ser `BLANCA` o `NEGRA`. El contenido es una cadena, si está
# vacía, la celda está vacía. Un crucigrama no está correctamente llenado si:
#   * Hay una celda `BLANCA` vacía
#   * Hay una celda `NEGRA` llena
# Escribir una función que dado un crucigrama, devuelva si está correctamente llenado.


# Completar la siguiente funcion
def correctamente_llenado(crucigrama):
    for i in range(len(crucigrama)):
        for j in range(len(crucigrama[i])):
            if crucigrama[i][j][0] == "NEGRA" and crucigrama[i][j][1] != "":
                return False
            elif crucigrama[i][j][0] == "BLANCA" and crucigrama[i][j][1] == "":
                return False
    
    return True


m1 = [
    [('BLANCA', 'H'), ('NEGRA', ''), ('BLANCA', 'B')],
    [('BLANCA', 'R'), ('NEGRA', ''), ('BLANCA', 'A')],
    [('BLANCA', 'M'), ('BLANCA', 'T'), ('BLANCA', 'G')],
]

m2 = [
    [('BLANCA', 'H'), ('NEGRA', '')],
    [('BLANCA', ''), ('NEGRA', '')]
]

m3 = [
    [('BLANCA', 'H'), ('NEGRA', 'M')],
    [('BLANCA', 'R'), ('NEGRA', '')]
]

assert correctamente_llenado(m1)
assert not correctamente_llenado(m2)
assert not correctamente_llenado(m3)

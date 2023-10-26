# Se cuenta con un sistema de versionado de software que identifica a cada versión 
# con tres números mayores o iguales a cero, (x, y, z) de la forma x.y.z.

# A mayor valor de x, más reciente es la versión. En caso de igualdad en x, 
# el mayor valor de y determina la más reciente y, si el valor de y también coincide,
# el valor a considerar es el z. 

# Se pide realizar una función que, dadas dos versiones representadas como 
# cadenas de caracteres, devuelva 1 si la primera versión recibida es mayor, 
# 0 si son iguales y -1 si la segunda es mayor.

# Escribir debajo de este comentario el código del ejercicio

def comparar_versiones(version1,version2):
    version1 = version1.split(".")
    version2 = version2.split(".")
    for i in range(3):
        version1[i]=int(version1[i])
        version2[i]=int(version2[i])
    if version1[0] > version2[0]:
        return 1
    elif version1[0] == version2[0] and version1[1] > version2[1]:
        return 1
    elif version1[0:2] == version2[0:2] and version1[2] > version2[2]:
        return 1
    elif version1[:] == version2[:]:
        return 0
    return -1

# Pruebas
assert comparar_versiones("0.1.1", "1.0.4") == -1
assert comparar_versiones("1.10.4", "1.2.4") == 1
assert comparar_versiones("1.1.4", "1.1.4") == 0

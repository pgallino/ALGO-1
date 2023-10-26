# Escribir una funcion que reciba dos secuencias A y B como parametro, 
# y devuelva un valor booleano indicando si todos los elementos de A estan en B

def esta_a_en_b(secuencia1, secuencia2):
    for elemento in secuencia1:
        if not elemento in secuencia2:      #toma cada elemento de la secuencia1 y se fija si esta en la secuencia2
            return False
        return True
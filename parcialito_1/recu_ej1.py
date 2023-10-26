# Escribir una función que dado un número entero positivo devuelva la mínima unidad del número, 
# que se calcula sumando los digitos del numero, y luego los digitos del resultado de esa suma,
# y asi sucesivamente hasta quedarse con un solo digito, que es la minima unidad. 
# Por ejemplo: `minima_unidad(546)` → `6` porque `5+4+6=15` y `1+5=6`.

# Escribir el codigo debajo de esta linea

def minima_unidad(n):

    cadena = str(n)

    if len(cadena) == 1:
        return int(cadena)

    while len(cadena) > 1:

        valor = 0

        for caracter in cadena:
            valor += int(caracter)
        
        cadena = str(valor)
    
    return valor

# Pruebas
assert minima_unidad(546) == 6
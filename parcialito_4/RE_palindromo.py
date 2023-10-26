"""Ejercicio 161 recursion
Escribir una función recursiva que reciba una cadena (sin espacios), y devuelva un booleano indicando si la cadena es o no un palíndromo."""


def _palindromo(palabra):
    if not palabra:
        return True

    if palabra[0] != palabra[-1]:
        return False

    return _palindromo(palabra[1:-1])

def palindromo(cadena):
    original = cadena
    copia = _palindromo(cadena)
    if copia:
        return True
    return False

print(palindromo("neuquen"))
print(palindromo("formosa"))

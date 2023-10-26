# 1. El estilo de nomenclatura `snake_case` permite representar un conjunto de
# palabras separándolas por un guión bajo, mientras que el estilo `CamelCase` las
# representa sin separadores, utilizando letras mayúsculas para la primera letra
# de cada palabra. Se pide realizar una función que reciba una cadena escrita en
# `snake_case` y devuelva su representación en `CamelCase`. Ejemplos:
# snake_a_camel("alan_turing") → "AlanTuring"
# snake_a_camel("hoy_es_el_parcial") → "HoyEsElParcial"


# Completar la siguiente funcion
def snake_a_camel(cadena):
    lista = cadena.split("_")
    for i in range(len(lista)):
        lista[i] = lista[i][0].upper() + lista[i][1:]
    
    return "".join(lista)


assert snake_a_camel("alan_turing") == "AlanTuring"
assert snake_a_camel("hoy_es_el_parcial") == "HoyEsElParcial"
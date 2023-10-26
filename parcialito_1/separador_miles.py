def agregar_separador_miles(numero):
    '''
    DOCU: eciba una cadena que contiene un largo número entero y devuelva una       cadena con el número y las separaciones de miles
    '''
    resultado = ""
    for i in range(len(numero)-1, -1, -1):
        resultado += numero[len(numero)-1-i]  #mete el numero[] equivalente a la pos i
        if i % 3 == 0 and i != 0:             #si i es divisible por 3 enteramente, agrega un puntito
            resultado += "."
    return resultado
def main():
    '''
    Pide al usuario que ingrese sucesion de numeros naturales uno tras otro hasta que el mismo ingrese `-1`. Al terminar, se debe imprimir cuantos numeros se ingresaron, la suma total de los valores y el promedio.
    '''
    contador = 0
    valor = 0
    print("Ingrese una sucesion de numeros naturales (o `-1` para terminar):")
    while True:
        numero = int(input())
        if numero == -1:
            break
        contador += 1
        valor += numero
    print("Cantidad de numeros ingresados:", contador)
    print("Suma de los valores:", valor)
    print("Promedio de los valores:", (valor)/(contador))


main()
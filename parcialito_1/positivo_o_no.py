def positivo_o_no():
    haymasdatos = "si"
    while haymasdatos == "si":
        x = int(input("Ingrese un número: "))
        if x > 0:
            print("Número positivo")
        elif x == 0:
            print("Ese número es 0")
        else:
            print("Número negativo")
        haymasdatos = input("¿Desea continuar? <si/no>: ")

positivo_o_no()
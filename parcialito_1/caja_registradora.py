def caja_registradora():
    total = 0
    
    while True:
        entrada = input("¿Cuánto vale? ")
        if entrada == "":
            break
        valor = float(entrada)
        if valor <= 0:
            print("Solo ingrese números positivos por favor.")
            continue
        total += valor

    print("El precio total es: ", total)

caja_registradora()    
def dia_semana():
    x = int(input("Ingrese el número del año: "))
    x = x % 7
    if x == 1:
        print("lunes")
    if x == 2:
        print("martes")
    if x == 3:
        print("miercoles")
    if x == 4:
        print("jueves")
    if x == 5:
        print("viernes")
    if x == 6:
        print("sabado")
    if x == 0:
        print("domingo")

dia_semana()
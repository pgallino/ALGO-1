def main():
    '''
    Lee notas (de a una) del usuario, preguntando en cada paso si se desea          continuar. Al finalizar, se imprime el promedio de las mismas.
    '''
    notas = []
    while True:
        nota=input("Ingrese una nota: ")
        if nota == "":
            break
        notas.append(int(nota))
    total = 0
    for i in range(len(notas)):
        total += notas[i]
    promedio = total/len(notas)
    print("El promedio es:", promedio)



main()

def main():
    '''
    Lee notas (de a una) del usuario, preguntando en cada paso si se desea continuar. Al finalizar, se imprime el promedio de las mismas.
    '''
    promedio = 0
    contador = 0
    suma_notas = 0
    while True:
        nota = int(input("Ingrese una nota: "))
        suma_notas += nota
        contador += 1
        continuar = input("Desea ingresar mas notas? (s/n): ")
        if continuar == "n":
          print("El promedio es:", suma_notas / contador)
          break
        else:
          continue
main()
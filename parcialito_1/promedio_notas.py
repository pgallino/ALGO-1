def main():
  suma = 0
  cantidad = 0
  seguir = ''
  while seguir != 'n':
     nota = int(input("Ingresar una nota: "))
     suma += nota
     cantidad += 1
     print(suma/cantidad)
     seguir = input("Quiere seguir agregando notas? [s/n]: ")
    #  if seguir == 'n':
    #    break

main()
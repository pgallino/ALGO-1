def imprimir_factores_primos():

  """Imprime la descomposición en factores primos
  del número entero k"""

  k=int(input("ingrese su numero: "))
  while k > 1:
    for i in range(2, k+1):
      if k%i == 0:
        print(i)
        k = k//i
        break

imprimir_factores_primos()
def imprimir_pares(inicio, fin):
    for i in range(inicio + inicio % 2, fin + 1, 2):
        print(i)

def main():

    print("Al ingresar dos números obtendrá todos los números pares entre ellos, ordenados crecientemente.")
    
    inicio = int(input("ingrese el primer número entero: "))
    fin = int(input("ingrese el segundo número entero: "))

    imprimir_pares(inicio, fin)

    print("estos son todos los números pares desde", inicio, "hasta", fin)

main()

    
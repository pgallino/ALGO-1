def imprimir_pares(inicio, fin):
    '''
    COMPLETAR DOCUMENTACION
    '''
    for i in range(inicio, fin+1):
        if(i % 2 == 0):
            print(i)

def main():
    '''
    El programa le pide dos numeros al usuario
    y luego imprime todos los pares entre ellos
    '''
    x = int(input("Ingrese el primer numero: "))
    y = int(input("Ingrese el segundo numero: "))
    imprimir_pares(x,y)

main()
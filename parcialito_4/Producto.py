def producto(num1, num2):
    '''
    COMPLETAR DOCUMENTACIÓN
    '''
    return num1*num2

def main():
    '''
    El programa le pide 2 números al usuario y luego imprime el producto.
    '''
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))

    print(producto(num1, num2))

main()
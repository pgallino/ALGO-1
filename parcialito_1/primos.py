def primos_h_natural(n):
    '''
    DOC: Completar
    '''
    for i in range(2,n+1):
        if esprimo(i):
            print(str(i), end=" ")

def esprimo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
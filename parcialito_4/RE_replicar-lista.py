"""funcion recursiva que replica n veces cada elemento de un arreglo"""

def _replicar(arr, n, lista):

    if arr == []:
        return lista
    
    valor = arr[0]
    
    lista += [valor] * n
    
    return _replicar(arr[1:], n, lista)

def replicar(arr, n):
    lista = []
    return _replicar(arr, n, lista)

arr = [1,2,3,4,5]

replicar(arr, 3)
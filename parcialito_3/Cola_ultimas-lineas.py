from Cola import Cola

def tail(nombre_archivo, N):

    cola = Cola()

    with open(nombre_archivo) as archivo:
        
        for i in range(N):
            linea = archivo.readline()
            linea = linea.rstrip("\n")
            cola.encolar(linea)
        
        for linea in archivo:
            linea = linea.rstrip("\n")
            cola.desencolar()
            cola.encolar(linea)

    for i in range(N):
        print(cola.desencolar())
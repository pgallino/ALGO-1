def empaquetar(lista):

    resultado = []
    subcontador = 1

    for i in range(0, len(lista)):
        
        if i == len(lista) - 1 or lista[i] != lista[i+1]:
            resultado.append((lista[i], subcontador))
            subcontador = 1
        
        elif lista[i] == lista[i+1]:
            subcontador += 1
    
    return resultado

print(empaquetar([1,2,1,1,1,6,3,3]))
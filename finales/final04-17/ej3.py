def interseccion(a, b):

    resultado = []
        
    for i in range(len(a)):
        if a[i] in b:
            indiceb = b.index(a[i])
            indicea = i
            break
        else:
            return resultado
    
    a = a[indicea:]
    b = b[indiceb:]
    
    if len(b) > len(a):
        for i in range(len(a)):
            if b[i] == a[i]:
                resultado += [b[i]]
        
        return resultado
    
    else:
        for i in range(len(b)):
            if b[i] == a[i]:
                resultado += [a[i]]
        
        return resultado

def interseccion2(a, b):
    # HACER: implementar la funcion
    i = 0
    j = 0
    l = []
    while i <= len(a)-1 and j <= len(b)-1:
    	if a[i] == b[j]:
    		l.append(a[i])
    		i+= 1
    		j+= 1
    		continue
    	elif a[i] < b[j]:
    		i += 1
    	else:
    		j += 1
    return l



def pruebas():
    assert interseccion([2],          [3])          == []
    assert interseccion([2],          [2])          == [2]
    assert interseccion([2, 2],       [2])          == [2]
    assert interseccion([2, 2],       [2, 2])       == [2, 2]
    assert interseccion([1, 2, 2, 4], [1, 2, 2, 3]) == [1, 2, 2]

    # OPCIONAL: pruebas adicionales

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()

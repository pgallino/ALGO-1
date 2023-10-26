def merge(a, b):
    # HACER: implementar la función

    if a == [] and b == []:
        return []
    
    elif a == [] and len(b) > 0:
        return b
    
    elif len(a) > 0 and b == []:
        return a

    else:
    
        if a[0] < b[0]:
            return [a[0]] + merge(a[1:],b)
    
        elif a[0] > b[0]:
            return [b[0]] + merge(a,b[1:])
    
        else:
            return [a[0],b[0]] + merge(a[1:],b[1:])

def pruebas():

    assert merge([2, 4, 6, 8], [1, 3, 5, 7]) == [1, 2, 3, 4, 5, 6, 7, 8]
    assert merge([2,4,6,8,9,10,11], [1,3,5,7]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert merge([],[]) == []
    assert merge([],[1,2,3]) == [1,2,3]

    # OPCIONAL: pruebas adicionales

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()


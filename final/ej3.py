def _intercalar(a, b, contador):
    # HACER: implementar la función en forma RECURSIVA

    if len(a) == 0 and len(b) == 0:
        return ""

    elif len(a) == 0 and len(b) > 0:
        return b
    
    elif len(a) > 0 and len(b) == 0:
        return a
    
    if contador%2 == 0:
        contador += 1
        return a[0] + _intercalar(a[1:], b, contador)
    
    elif contador%2 != 0:
        contador += 1
        return b[0] + _intercalar(a,b[1:], contador)

def intercalar(a,b):
    contador = 0
    return _intercalar(a,b,contador)

def pruebas():
    assert intercalar("hola", "mundo!") == "hmoulnado!"
    assert intercalar("mundo!", "hola") == "mhuonldao!"
    assert intercalar("", "") == ""
    assert intercalar("", "hola") == "hola"
    assert intercalar("hola", "") == "hola"

    # OPCIONAL: Pruebas adicionales

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()

# HACER: implementar la clase Persona

#AL IMPLEMENTAR BUSQUEDA BINARIA ES MEJOR QUE LINEAL.
class Persona:

    def __init__(self, dni, nombre, direccion):

        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion
    
    def obtener_dni(self):
        return self.dni

def buscar_en_padron(dni, personas):
    # HACER: implementar la función
    medio = len(personas) // 2
    if personas[medio].obtener_dni() == dni:
        return personas[medio]
    
    elif len(personas) == 1:
        return None
    
    elif personas[medio].obtener_dni() > dni:
        return buscar_en_padron(dni, personas[:medio])
    
    elif personas[medio].obtener_dni() < dni:
        return buscar_en_padron(dni, personas[medio:])

def pruebas():
    personas = [
        Persona(11111, "persona 1", "direccion 1"),
        Persona(22222, "persona 2", "direccion 2"),
        Persona(33333, "persona 3", "direccion 3"),
        Persona(44444, "persona 4", "direccion 4"),
    ]

    p = buscar_en_padron(33333, personas)
    assert(p is personas[2])

    # OPCIONAL: Pruebas adicionales
    p = buscar_en_padron(93242141, personas)
    assert(p is None)

    p = buscar_en_padron(11111, personas)
    assert(p is personas[0])

    p = buscar_en_padron(44444, personas)
    assert(p is personas[3])

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()

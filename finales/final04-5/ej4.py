
# HACER: implementar las funciones

class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def __eq__(self, otro):
        if self.titulo == otro.titulo and self.autor == otro.autor and self.año == otro.año:
            return True
        return False

def ordenar_libros(libros):

    for i in range(1, len(libros)):

        j = i - 1

        if libros[i].titulo >= libros[j].titulo:
            continue

        while libros[i].titulo < libros[j].titulo and j > 0:
            j -= 1
        
        if j == 0 and libros[i].titulo > libros[j].titulo:
            libros.insert(1, libros.pop(i))
        
        else:
            libros.insert(j, libros.pop(i))
    
    return libros

def buscar_libro(libros, titulo):
    medio = len(libros) // 2

    if titulo == libros[medio].titulo:
        return libros[medio]

    elif len(libros) == 1:
        return None
    
    elif titulo < libros[medio].titulo:

        return buscar_libro(libros[:medio], titulo)
    
    else:

        return buscar_libro(libros[medio:], titulo)


def pruebas():

    libros = [
        Libro("The Sittaford Mystery", "Agatha Christie", 1931),
        Libro("The Seven Dials Mystery", "Agatha Christie", 1929),
        Libro("The Murder at the Vicarage", "Agatha Christie", 1930),
        Libro("The Mystery of the Blue Train", "Agatha Christie", 1928),
        Libro("The Floating Admiral", "Agatha Christie", 1931),
        Libro("Giant's Bread", "Agatha Christie", 1930),
    ]

    ordenar_libros(libros)

    assert libros == [
        Libro("Giant's Bread", "Agatha Christie", 1930),
        Libro("The Floating Admiral", "Agatha Christie", 1931),
        Libro("The Murder at the Vicarage", "Agatha Christie", 1930),
        Libro("The Mystery of the Blue Train", "Agatha Christie", 1928),
        Libro("The Seven Dials Mystery", "Agatha Christie", 1929),
        Libro("The Sittaford Mystery", "Agatha Christie", 1931),
    ]

    libro = buscar_libro(libros, "The Floating Admiral")
    assert libro is libros[1]

    # OPCIONAL: pruebas adicionales. Ejemplo: buscar un libro que no exista

    libro = buscar_libro(libros, "chochocho")
    assert libro is None

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()

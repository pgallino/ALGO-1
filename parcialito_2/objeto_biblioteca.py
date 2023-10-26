"""Sabiendo que la clase Libro tiene los métodos obtener_autor y obtener_titulo que devuelven cadenas de caracteres, escribir la clase Biblioteca con los métodos:

agregar_libro que recibe un Libro y lo agrega a la colección.

sacar_libro que recibe el nombre de un título y el de un autor y lo saca de la biblioteca,
devolviéndolo o levantando una excepción en caso de que los datos no correspondan con los de algún libro agregado.

contiene_libro que recibe el nombre de un título y el de un autor y devuelve True o False de acuerdo a si está en la colección o no."""

class Libro:

    def __init__(self, autor, titulo):
        self.autor = autor
        self.titulo = titulo
    
    def obtener_autor(self):
        return self.autor
    
    def obtener_titulo(self):
        return self.titulo

class Biblioteca:

    def __init__(self):

        self.libros = []

    def __str__(self):
        return f"La biblioteca contiene: {self.libros}"

    def agregar_libro(self, libro):
        self.libros.append((libro.obtener_autor(),libro.obtener_titulo()))
    
    def sacar_libro(self, titulo, autor):
        if (autor,titulo) in self.libros:
            self.libros.remove((autor,titulo))
            return (autor, titulo)
        else:
            raise Exception("No está ese libro en la biblioteca")
    
    def contiene_libro(self, titulo, autor):
        if (autor,titulo) in self.libros:
            return True
        else:
            return False

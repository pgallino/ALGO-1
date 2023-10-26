"""Escribir una clase Item, que recibe en su constructor el nombre del objeto y su peso. 

Escribir también una clase Caja, que recibe en su constructor la capacidad de la misma (o sea, cuánto peso puede cargar). 

Además, esta clase debe tener los siguientes métodos:

guardar_item, que recibe un Item y lo guarda en su interior, siempre y cuando tenga capacidad. Si no tiene capacidad, debe lanzar una excepción.

obtener_mas_pesado y obtener_mas_liviano, que devuelven el Item con mayor y menor peso, respectivamente. 

En ambos casos devuelve None si no hay items guardados, y si hay más de uno con el mismo peso devuelve cualquiera de ellos."""

class Item:

    def __init__(self, nombre, peso):

        self.nombre = nombre
        self.peso = peso

class Caja:

    def __init__(self, capacidad):

        self.capacidad = capacidad
        self.contenido = []
        self.item_mas_pesado = (0, "ninguno")
        self.item_mas_liviano = (capacidad, "ninguno")

    def guardar_item(self, item):
        if item.peso > self.capacidad:
            raise Exception("La caja no puede aguantar el peso del objeto")
        else:
            self.capacidad = self.capacidad - item.peso
            self.contenido.append(item.nombre)
            if item.peso > self.item_mas_pesado[0]:
                self.item_mas_pesado = (item.peso,item.nombre)
            if item.peso < self.item_mas_liviano[0]:
                self.item_mas_liviano = (item.peso,item.nombre)



    def obtener_mas_pesado(self):
        return self.item_mas_pesado[1]

    def obtener_mas_liviano(self):
        return self.item_mas_liviano[1]
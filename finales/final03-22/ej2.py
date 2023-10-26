#
# HACER: implementar la clase y las funciones
#
class Producto:

    def __init__(self, id, nombre, cantidad):

        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
    
    def obtener_id(self):
        return self.id
    
    def obtener_nombre(self):
        return self.nombre
    
    def obtener_cantidad(self):
        return self.cantidad
    
    def comparar_id(self, otro):
        if self.id == otro.id:
            return True
        return False
    
    def __eq__(self, otro):
        if self.obtener_cantidad() == otro.obtener_cantidad() and self.obtener_id() == otro.obtener_id() and self.obtener_nombre() == otro.obtener_nombre():
            return True
        return False

def guardar(productos, ruta):

    with open(ruta, "w") as archivo:

        for i in range(len(productos)):

            producto = productos[i]
            id = producto.obtener_id()
            nombre = producto.obtener_nombre()
            cantidad = producto.obtener_cantidad()

            archivo.write(f"{id},{nombre},{cantidad}\n")

def cargar(ruta):

    lista = []

    with open(ruta) as archivo:

        for linea in archivo:

            if linea:

                linea = linea.rstrip("\n").split(",")

                id, nombre, cantidad = linea

                producto = Producto(int(id), nombre, int(cantidad))

                lista.append(producto)

    return lista

def verificar_ids(productos):

    for i in range(1,len(productos)):

        producto1 = productos[i-1]
        producto2 = productos[i]

        if producto1.comparar_id(producto2) == True:
            return False
    
    return True

def pruebas():

    productos = [
        # HACER: llenar la lista con al menos 3 productos diferentes
        Producto(2,"cocacola",5), Producto(3,"pepsi",10), Producto(4,"leche",81)]

    # HACER: llamar a la función guardar()
    guardar(productos, "supermercado.txt")

    # HACER: llamar a la función cargar()
    productos_cargado = cargar("supermercado.txt")

    # HACER: verificar que productos_cargado y productos son equivalentes

    pruebita = 1

    for i in range(len(productos_cargado)):
        if productos_cargado[i] != productos[i]:
            pruebita = 0
            break
    
    assert pruebita == 1

    assert verificar_ids(productos) == True

    # OPCIONAL: probar verificar_ids() con una lista que contiene repeticiones

    from os import path
    print(f"{path.basename(__file__)}: OK")

pruebas()

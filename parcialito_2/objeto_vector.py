class Vector:
    '''
    DOC: Completar
    '''
    def __init__(self, coordenadas):
        self.vector = coordenadas
    
    def __str__(self):
        cadena_string = []
        for coordenada in range(len(self.vector)):
            cadena_string.append(str(self.vector[coordenada]))

        cadena = ",".join(cadena_string)
        
        return f"[{cadena}]"
    
    def __add__(self, otro):
        if len(self.vector) != len(otro.vector):
            raise Exception("Vectores no tienen la misma cantidad de elementos.")

        elif len(self.vector) == len(otro.vector):

            suma_vectores = []
            for coordenada in range(len(self.vector)):
                suma_vectores.append(self.vector[coordenada] + otro.vector[coordenada])

            return Vector(suma_vectores)

    def __mul__(self, numero):

        vector_multiplicado=[]
        for coordenada in range(len(self.vector)):
            vector_multiplicado.append(self.vector[coordenada] * numero)

        return Vector(vector_multiplicado)
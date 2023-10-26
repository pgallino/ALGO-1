"""Se tiene un diccionario en el que la clave es el nombre de una persona y el valor una lista con sus amigos. 
Ejemplo: {'Juan': ['Caro', 'José', 'Daniela', 'Alejandro'], 'Caro': ['José', 'Daniela'],
 'José': ['Caro', 'Juan'], 'Daniela': [], 'Alejandro': ['Caro', 'José', 'Juan']}

Se quiere obtener una lista de tuplas con aquellas amistades que son correspondidas. 
Se considera correspondida la amistad si un nombre está en mi lista y yo estoy en la lista de ese nombre. 
Según el ejemplo dado, debe devolver: [('Juan', 'José'), ('José', ‘Juan’), ('Juan', 'Alejandro'), ('Caro', 'José'), ('José', ‘Caro’) ('Alejandro', 'Juan')]"""

def amistades_correspondidas(diccionario):
    resultado = []
    personas = list(diccionario.keys())
    for clave in diccionario:
        for persona in range(len(personas)):
            persona_2 = personas[persona]
            if clave in diccionario[persona_2] and persona_2 in diccionario[clave]:
                resultado.append((clave, persona_2))
    return resultado



#def amistades_correspondidas(diccionario):
    
#   lista = []

#    for nombre,amigos in diccionario.items():

#        for amigo in amigos:
#            if nombre in diccionario[amigo]:
#                lista.append((nombre,amigo))
#   return lista
def agenda_simplificada(busqueda, contactos):
    '''
    Recibe una cadena a buscar y una agenda en forma de lista de tuplas que continenen
    el nombre y el telefono del contacto.
    '''
    resultado = []
    busqueda = busqueda.lower()
    for i in range(len(contactos)):
        busqueda_aux = contactos[i][0]
        busqueda_aux = busqueda_aux.lower()
        if busqueda in busqueda_aux:
            resultado.append(contactos[i])
    
    return resultado
# 3. Se pide implementar una clase `CalendarioMes` con los siguientes métodos:
# - `__init__()`: toma como parámetro un entero que representa el número de
#   días del mes (entre 28 y 31). Debe lanar una excepción si no es un día válido.
# - `agregar_evento()`: toma como parámetro un día (número entero) y el nombre
#   de un evento (cadena) y lo almacena en el calendario. Debe lanzar una excepción si no es un día válido.
# - `eliminar_evento()`: toma como parámetro un día y el nombre de un evento y
#   lo elimina del calendario. Debe lanzar una excepción si no existe un evento con ese nombre.
# - `obtener_eventos_dia()`: toma como parámetro un día y devuelve una lista
#   con los eventos programados para ese día, o la lista vacía si no hay
#   eventos en ese día. Debe lanzar una excepción si no es un día válido.


# Completar la siguiente clase
class CalendarioMes:

    def __init__(self, cant_dias):
        if cant_dias > 31 or cant_dias < 28:
            raise Exception("dias no validos")
        else:
            lista = []
            for i in range(cant_dias):
                lista.append([])
        
        self.mes = lista
    
    def agregar_evento(self, dia, evento):
        if dia > len(self.mes) or dia<0:
            raise Exception("dia no valido")
        
        else:
            self.mes[dia-1].append(evento)
    
    def eliminar_evento(self, dia, evento):
        if dia > len(self.mes) or dia<0:
            raise Exception("dia no valido")
        
        else:
            if not evento in self.mes[dia-1]:
                raise Exception("no hay tal evento")
            else:
                self.mes[dia-1].remove(evento)
    
    def obtener_eventos_dia(self,dia):
        if dia > len(self.mes) or dia<0:
            raise Exception("dia no valido")
        
        else:
            return self.mes[dia-1]




# Pruebas
hay_excepcion = True
try:
    c = CalendarioMes(32)
    hay_excepcion = False
except:
    pass
assert hay_excepcion, "una excepcion no fue lanzada"

c = CalendarioMes(30)

try:
    c.agregar_evento(31, "evento1")
    hay_excepcion = False
except:
    pass
assert hay_excepcion, "una excepcion no fue lanzada"

c.agregar_evento(1, "evento1")
c.agregar_evento(1, "evento2")
c.agregar_evento(2, "evento3")

assert c.obtener_eventos_dia(1) == ["evento1", "evento2"]
assert c.obtener_eventos_dia(2) == ["evento3"]
assert c.obtener_eventos_dia(3) == []

c.eliminar_evento(1, "evento1")
c.eliminar_evento(2, "evento3")

assert c.obtener_eventos_dia(1) == ["evento2"]
assert c.obtener_eventos_dia(2) == []
assert c.obtener_eventos_dia(3) == []


try:
    c.eliminar_evento(1, "evento1")
    hay_excepcion = False
except:
    pass
assert hay_excepcion, "una excepcion no fue lanzada"


try:
    c.obtener_eventos_dia(31)
    hay_excepcion = False
except:
    pass
assert hay_excepcion, "una excepcion no fue lanzada"

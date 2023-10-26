# Se pide implementar una clase `Semaforo` con tres luces (roja, amarilla y verde) 
# y el siguiente comportamiento:

# - Al instanciar la clase se debe ver la luz roja prendida.​

# - Debe tener un metodo `siguiente` para apagar la luz actual y encender la siguiente 
# (el orden de encendido de las luces es `roja->amarilla->verde->roja->amarilla->...`)

# - Debe tener un metodo `apagar` que apague el semaforo. En un semaforo apagado todas las 
# luces estan apagadas y no se puede encender ninguna. Si se intenta usar el metodo 
# `siguiente` mientras el semaforo esta apagado se debe lanzar una excepcion del tipo ValueError.

# - Debe tener un metodo `encender` que encienda el semaforo. Al encender el semaforo 
# el estado de las luces debe ser el mismo que tenia antes de apagarlo.

# - Al imprimir una instancia de la clase semaforo, debe mostrar qué luz esta prendida. 
# Si el semaforo esta apagado, debe mostrar que esta apagado.

# La representacion interna de la clase es a criterio pero debe ser acorde al comportamiento y no agregar complejidad.


# Escribir debajo de este comentario el cdigo del ejercicio

class Semaforo:

    def __init__(self):

        self.prendido = True

        self.color = "roja"

        self.color_seguimiento = ["verde","amarilla","roja"]

    def __str__(self):

        return f"{self.color}"
    
    def siguiente(self):

        if self.prendido == False:
            raise ValueError("El semáforo está apagado")
        
        elif self.prendido == True:

            if self.color_seguimiento[-1] == "roja":
                self.color_seguimiento.append("amarilla")
                self.color_seguimiento.pop(0)
                self.color = "amarilla"

            elif self.color_seguimiento[-1] == "amarilla":
                self.color_seguimiento.append("verde")
                self.color_seguimiento.pop(0)
                self.color = "verde"

            elif self.color_seguimiento[-1] == "verde":
                self.color_seguimiento.append("roja")
                self.color_seguimiento.pop(0)
                self.color = "roja"

    def apagar(self):

        if self.prendido == False:
            raise ValueError("El semáforo ya está apagado")
        
        else:
            self.prendido = False
            self.color = "apagado"

    def encender(self):

        if self.prendido == True:
            raise ValueError("El semáforo ya está prendido")

        else:
            self.prendido = True
            self.color = self.color_seguimiento[-1]



# Pruebas

s = Semaforo()
assert 'roja' in str(s)
s.siguiente()
assert 'amarilla' in str(s)
s.siguiente()
assert 'verde' in str(s)
s.siguiente()
assert 'roja' in str(s)
s.apagar()
hay_excepcion = True
try:
    s.siguiente()
    hay_excepcion = False
except ValueError:
    pass
assert hay_excepcion, "excepcion no fue lanzada"
s.encender()
assert 'roja' in str(s)
s.siguiente()
assert 'amarilla' in str(s)

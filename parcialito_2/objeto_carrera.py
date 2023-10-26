""">>> analisis2 = Materia("61.03", "Análisis 2", 8)
>>> fisica2 = Materia("62.01", "Física 2", 8)
>>> algo1 = Materia("75.40", "Algoritmos 1", 6)
>>> c = Carrera([analisis2, fisica2, algo1])
>>> print(c)
Créditos: 0 -- Promedio: N/A -- Materias aprobadas:
>>> c.aprobar("95.14", 7)
ValueError: La materia 95.14 no es parte del plan de estudios
>>> c.aprobar("75.40", 10)
>>> c.aprobar("62.01", 7)
>>> print(c)
Créditos: 14 -- Promedio: 8.5 -- Materias aprobadas:
75.40 Algoritmos 1 (10)
62.01 Física 2 (7)
"""

class Materia:
    '''
    DOC: Completar
    '''
    def __init__ (self, codigo, materia, creditos):
        self.codigo = codigo
        self.nombre = materia
        self.creditos = creditos
        self.nota = 0
        self.aprobado = False

class Carrera:
    '''
    DOC: Completar
    '''
    def __init__ (self, lista_materia):
        self.plan_de_estudios = lista_materia
        self.hay_aprobadas = False

    def __str__(self):

        if self.hay_aprobadas == True:
            promedio = 0
            creditos = 0
            cadena = "\n"
            cantidad_aprobadas = 0
            for materia in self.plan_de_estudios:
                if materia.aprobado == True:
                    creditos += materia.creditos
                    cadena += f"{materia.codigo} {materia.nombre} ({str(materia.nota)})\n"
                    promedio += materia.nota
                    cantidad_aprobadas += 1

            promedio = promedio / cantidad_aprobadas
            return f"Créditos: {creditos} -- Promedio: {promedio} -- Materias aprobadas:" + cadena
        else:
            return f"Créditos: 0 -- Promedio: N/A -- Materias aprobadas:"
    
    def aprobar(self, codigo, nota):
        codigos = []
        for materia in self.plan_de_estudios:
            codigos.append(materia.codigo)
            
        if not codigo in codigos:
            raise ValueError(f"La materia {codigo} no es parte del plan de estudios")

        for materia in self.plan_de_estudios:
            if codigo == materia.codigo:
                materia.nota = nota
                materia.aprobado = True
                self.hay_aprobadas = True
                




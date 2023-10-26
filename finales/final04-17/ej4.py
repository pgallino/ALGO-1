import queue
def tail(entrada, salida, n):

    q = queue.Queue()
    contador = 0
    
    with open(entrada, encoding='utf8') as e, open(salida, "w") as s:

        for linea in e:
            contador += 1
            q.put(linea)
            if contador == n:
                break
        
        for linea in e:

            if linea == "":
                break
            
            else:
                q.get()
                q.put(linea)
        
        for i in range(n):
            if i == n-1:
                ultima = q.get()
                ultima = ultima.rstrip("\n")
                s.write(ultima)
            else:
                s.write(q.get())


def pruebas():
    tail("entrada.txt", "salida.txt", 6)

    # salida.txt debería contener las siguientes 6 líneas:
    #
    # Pero ponga su esperanza
    # en el Dios que lo formó;
    # y aquí me despido yo
    # que he relatao a mi modo
    # MALES QUE CONOCEN TODOS,
    # PERO QUE NAIDES CONTÓ.

    from os import path
    print(f"{path.basename(__file__)}: OK (verificar el contenido de salida.txt)")

pruebas()

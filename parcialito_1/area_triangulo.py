import norma as n
import diferencia as d
import prodvectorial as p

def area_triangulo(x1, y1, z1, x2, y2, z2, x3, y3, z3): #ESTA FUNCIÓN TOMA TRES PUNTOS DADOS EN R3 Y CALCULA EL ÁREA DEL TRIANGULO QUE FORMEN AL UNIRLOS           
        
    x21, y21, z21 = d.diferencia(x2, y2, z2, x1, y1, z1) #VECTOR LADO 1 DEL TRIÁNGULO
        
    x31, y31, z31 = d.diferencia(x3, y3, z3, x1, y1, z1) #VECTOR LADO 2 DEL TRIÁNGULO
        
    p1, p2, p3 = p.prod_vectorial(x21, y21, z21, x31, y31, z31) #PRODUCTO VECTORIAL ENTRE LADO 1 Y LADO 2
        
    nor = n.norma(p1, p2, p3) #NORMA DEL PRODUCTO VECTORIAL ENTRE LADO 1 Y LADO 2
        
    area = nor/2 #AREA DEL TRIÁNGULO 
        
    return(area)


assert area_triangulo(0,0,2,0,-2,0,0,0,0) == 2                     #PRUEBA 1

assert area_triangulo(0,0,2,0,4,0,0,0,0) == 4                      #PRUEBA 2

assert area_triangulo(0,-8,0,-10,0,0,0,0,0) == 40                  #PRUEBA 3
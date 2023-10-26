// Ejercicio 185 c
// Dado un arreglo de enteros y su longitud, escribir en lenguaje C una función que devuelva el mayor elemento del arreglo.

#include <stdio.h>

int devolver_mayor(int arreglo[], int len) {

    int valor;

    for (int i = 0; i < len; i++) {

        if (i == 0) {

            valor = arreglo[i];
        } else if (valor < arreglo[i]) {

            valor = arreglo[i];
        }

    }

    return valor;
}

int main(void) {
    int arreglo[] = {1,5,2,4,9,2};
    printf("%d", devolver_mayor(arreglo, 6));
    return 0;
}
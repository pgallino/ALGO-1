// 3. Implementar en C una función que reciba dos arreglos de enteros (y sus respectivos tamaños), 
// y que imprima los números del primer arreglo que **no** están presentes en el segundo.
// Ejemplo:
// int numeros[] = {1, 2, 7, 2, 3, 5};
// int ignorar[] = {2, 3};
// imprimir_faltantes(numeros, 6, ignorar, 2);
// // Salida:
// 1
// 7
// 5

// Escribir el codigo debajo de esta linea

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

void imprimir_faltantes(int numeros[], int largo1, int ignorar[], int largo2) {

    for (int i = 0; i < largo1; i++) {

        int j = 0;

        while (numeros[i] != ignorar[j] && j < largo2) {

            j++;
        }

        if (j == largo2) {
            printf("%d\n", numeros[i]);
        
        }
    }
}

// main para pruebas
int main() {
    int numeros[] = {1, 2, 7, 2, 3, 5};
    int ignorar[] = {2, 3};
    imprimir_faltantes(numeros, 6, ignorar, 2);
    return 0;
}
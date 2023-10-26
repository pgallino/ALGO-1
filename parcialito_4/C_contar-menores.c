// Escribir en C la función contar_menores, que recibe un vector de enteros y la cantidad de elementos, 
// y devuelve cuántos números del vector son menores al valor recibido.

#include <stdio.h>

int contar_menores(int numeros[], int len, int valor) {

    int cant_menores = 0;

    for (int i = 0; i != len; i++) {

        if (numeros[i] < valor) {
            cant_menores++;
        }
    }

    return cant_menores;

}

int main(void) {
    int numeros[] = {1,2,3,4,5,6,7,8,1};
    int len = 9;
    int valor = 1;
    printf("%d\n", contar_menores(numeros, len, valor));
    return 0;
}
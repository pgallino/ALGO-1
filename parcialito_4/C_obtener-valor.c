// Ejercicio 181 c

// Escribir en C la función int obtener_valor(const int vector[], int len, int pos). La función debe devolver el valor que se encuentra en vector[pos], 

// interpretando pos como en Python. Es decir, pos puede tomar valores entre -len y len - 1; 

// y para los valores negativos busca los elementos comenzando desde la última posición del vector. 

// Si pos no es válida, devolver la constante INT_MIN (asumir que la constante ya fue declarada).


#include <stdio.h>

int obtener_valor(const int vector[], int len, int pos) {

    int invalido = 999;

    if (pos < 0) {
        pos += len;
        if (pos < 0) {
            return invalido;
        }
    }

    if (pos >= len) {
        return invalido;
    }

    return vector[pos];

}

int main(void) {

    int vector[] = {1,2,3,4,5,6,7,8,2};
    int len = 9;
    int pos = -2;

    printf("%d \n", obtener_valor(vector, len, pos));
    return 0;
}
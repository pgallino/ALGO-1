// Ejercicio 184 c

// Escribir en C una función que pida al usuario que ingrese un número natural e imprima por pantalla los primeros n números primos. 

// Se debe implementar una función auxiliar es_primo que recibe un número y devuelve true o false dependiendo si el número es primo o no. 

// Por ej, si el usuario ingresa 4, debe imprimir 2,3,5,7.

#include <stdio.h>

int es_primo(int n) {

    int contador = 0;

    for(int i = 1; i < n + 1; i++) {
        if (n % i == 0) {
            contador++;
        }
    }

    if (contador != 2) {
        return 0;
    } else {
        return 1;
    }
}

void imprimir_primos(int r) {

    int m = 0;
    int l = 0;

    while (m < r) {

        if (es_primo(l) == 1) {
            printf("%d, ", l);
            l++;
            m++;
        } else {
            l++;
        }
    }
}

int main(void) {
    imprimir_primos(4);
    return 0;

}
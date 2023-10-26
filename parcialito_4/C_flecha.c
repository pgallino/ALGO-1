// Ejercicio 189 c
// Implementar en C una función que reciba un número entero positivo n e imprima una flecha hacia la derecha de longitud n. Por ejemplo, para n = 4:

// *
//  *
//   *
// ****
//   *
//  *
// *

#include <stdio.h>

void flecha(int n) {

    for (int i = 1; i < n; i++) {
        
        for (int r = 1; r != i; r++) {

            printf(" ");
        }

        printf("*\n");
        
    }

    for (int i = 0; i < n; i++) {

        if (i == n-1) {

            printf("*\n");

        } else {

            printf("*");
        }
    }

    for (int i = n; i > 0; i--) {
        
        for (int r = 1; r != i; r++) {

            printf(" ");
        }

        printf("*\n");
        
    }

}

int main(void) {
    int n = 4;
    flecha(n);
    return 0;
}
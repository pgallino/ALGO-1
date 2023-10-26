// Ejercicio 190 c
// Escribir en lenguaje C un programa que reciba un número entero positivo n e imprima un triángulo equilátero de esa base y altura. Por ejemplo, para n = 4:

//    *
//   * *
//  * * *
// * * * *

#include <stdio.h>

void triangulo(int n) {

    for (int i = 1; i < n + 1; i++) {

        for (int l = 0; l < n-i; l++) {

            printf(" ");
            
        }

        for (int r = 1; r < i + 1; r++) {

            printf("*");
            if (r == i) {
                printf("\n");
            } else {
                printf(" ");
            }
        }
        
    }

}

int main(void) {
    triangulo(7);
    return 0;
}
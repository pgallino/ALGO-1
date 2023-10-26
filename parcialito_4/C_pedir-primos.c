// Ejercicio 179 c
// Escribir un programa en C que pida un número al usuario, imprima un mensaje indicando si es primo o no, y repita lo mismo hasta que el usuario ingrese -1.


#include <stdio.h>
#include <stdlib.h>

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

void pedir_primos(void) {

    char numero[5];
    int valor;
    do {
        printf("Ingrese un entero ");
        fgets(numero,4,stdin);
        valor = atoi(numero);
        if (valor > 0) {
            if (es_primo(valor) == 1) {
            printf("ES PRIMO\n");
        } else {
            printf("NO ES PRIMO\n");
        }
        }
    
    } while (valor != -1);


}

int main(void) {
    pedir_primos();
    return 0;

}
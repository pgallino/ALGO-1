// Ejercicio 177 c
// Escribir en C un programa que le pregunte al usuario por 5 números enteros y luego los imprima de manera inversa al orden en que fueron ingresados.

#include <stdlib.h>
#include <stdio.h>

void pedir_devolver_inversa(void) {

    int diccionario[] = {0,0,0,0,0};
    char numero[5];
    int valor;

    for (int i = 4; i > -1; i--) {

        printf("Ingrese un numero entero: ");
        fgets(numero,4,stdin);
        valor = atoi(numero);
        diccionario[i] = valor;
    }

    for (int n = 0; n < 5; n++) {

        printf("%d\n", diccionario[n]);
    }


}

int main(void) {
    pedir_devolver_inversa();
    return 0;
}
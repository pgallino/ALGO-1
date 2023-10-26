// Ejercicio 191 c

// Implementar en C una función que reciba una cadena e imprima la cantidad de letras, números y espacios presentes en la misma.

// Usar las funciones de la biblioteca: int isalpha(char), int isdigit(char), isspace(char).

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

void contador_caracteres(char cadena[]) {

    int cant_tipos[] = {0,0,0};

    for (int i = 0; cadena[i] != '\0'; i++) {
        if (isalpha(cadena[i]) != 0) {
            cant_tipos[0]++;
        } else if (isdigit(cadena[i]) != 0) {
            cant_tipos[1]++;
        } else if (isspace(cadena[i]) != 0) {
            cant_tipos[2]++;
        }
    }

    printf("La cadena tiene %d espacios\n", cant_tipos[2]);
    printf("La cadena tiene %d letras\n", cant_tipos[0]);
    printf("La cadena tiene %d numeros\n", cant_tipos[1]);
}

int main(void){
    char cadena[] = "pedro el mas lindo tiene 20";
    contador_caracteres(cadena);
    return 0;
}




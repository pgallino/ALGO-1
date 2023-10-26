// Ejercicio 192 c
// Escribir en C un programa que pida al usuario dos palabras. 
// El programa debe imprimir ambas palabras en una línea, separadas por una secuencia de puntos de forma tal que la longitud total de la línea sea de 30 caracteres. 

// Ejemplo:

// Primera palabra: Hola
// Segunda palabra: Mundo
// Hola.....................Mundo

#include <stdio.h>
#include <stdlib.h>

int largo(char s[]) {
    int resultado = 0;
    
    for (int i = 0; s[i] != '\0'; i++) {
        resultado += 1;
    }
    return resultado;

}

void imprimir_separacion(void) {

    char cadena1[15];
    char cadena2[15];

    printf("Ingrese la primera palabra: ");

    fgets(cadena1, 14, stdin);

    if (cadena1[largo(cadena1) - 1 == '\n']) {
        cadena1[largo(cadena1) - 1] = '\0';
    }
    
    printf("Ingrese la segunda palabra: ");

    fgets(cadena2, 14, stdin);

    printf("%s", cadena1);

    for (int i = 1; i < (32 - largo(cadena1) - largo(cadena2)); i++) {

        printf(".");
    }

    printf("%s", cadena2);

    
}

int main(void) {
    imprimir_separacion();
    return 0;
}
// 3) Implementar en C un programa que le pida al usuario que ingrese una cadena 
// de texto e imprima por pantalla el resultado de reemplazar en esa cadena todos 
// los caracteres que no son una letra por un espacio.
// Nota: se puede usar la funcion isalpha del modulo ctype.
// ​Ejemplo de ejecucion:
/*
Ingrese una cadena: Esta es una oracion! Mira los signos (?) y cosas raras que tiene :).
Esta es una oracion  Mira los signos     y cosas raras que tiene    
*/

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int largo(char s[]) {
    int resultado = 0;
    
    for (int i = 0; s[i] != '\0'; i++) {
        resultado += 1;
    }
    return resultado;

}

void cambiar_por_espacios(void) {

    char cadena[100];                      //elegí 100 porque me parece un tamaño lógico para una oración y cumple con la del enunciado
    int largo_cadena = largo(cadena);

    printf("Ingrese una cadena: ");

    fgets(cadena, 99, stdin);

    if (cadena[largo_cadena - 1 == '\n']) {  //saco el /n porque no sé si quiere que se imprima con o sin, (si quisiese con un salto de linea al final, estas dos lineas sobran)
        cadena[largo_cadena - 1] = '\0';
    }

    for (int i = 0; cadena[i] != '\0'; i++) {

        if (isalpha(cadena[i]) == 0) {
            printf(" ");
        } else {
            printf("%c", cadena[i]);
        }
    }
}

// función main para realizar pruebas
int main() {
    cambiar_por_espacios();
    return 0;
}

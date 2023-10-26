// Ejercicio 183 c
// Escribir en lenguaje C una función que recibe una cadena de caracteres e imprime la cantidad de apariciones de cada caracter. Ejemplo:

// caracteres("Barbara")
// a: 3
// b: 1
// r: 2
// B: 1
// Ayuda: recordar que cada caracter (char) es un número entre 0 y 255. Usar un arreglo de 255 posiciones para contar la cantidad de ocurrencias de cada caracter.

#include <stdio.h>
void contar_caracteres(char cadena[]) {

    int arreglo[255];
    for(int i = 0; i < 255; i++) arreglo[i] = 0;

    for(int i = 0; cadena[i] != '\0'; i++) {
        int a = cadena[i];
        arreglo[a]++;
    }

    for(int i = 0; i < 255; i++) {
        if (arreglo[i] != 0) {
            printf("%c: %d\n", i, arreglo[i]);
        }
    }
}


int main(void) {
    contar_caracteres("pedro");
    return 0;
}
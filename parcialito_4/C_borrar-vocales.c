// Ejercicio 187 c
// Escribir un programa en C que le pida al usuario que ingrese una cadena y luego muestre por pantalla esa cadena pero reemplazando cada vocal por un *.


#include <stdio.h>

void borrar_vocales(char cadena[]) {

    for (int i = 0; cadena[i] != '\0'; i++) {

        if (cadena[i] == 'a' || cadena[i] == 'e' || cadena[i] == 'i' || cadena[i] == 'o' || cadena[i] == 'u') {
            
            printf("*");
            
        } else {

            printf("%c", cadena[i]);
        }
    }
}


int main(void) {
    char cadena[] = "aeiou pedro es un genio";
    borrar_vocales(cadena);
    return 0;
}
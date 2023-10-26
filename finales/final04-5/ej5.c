// Ejercicio 5 Implementar en C la función void join(char destino[], char delimitador, char
// *cadenas[], int n), que a partir de un arreglo de cadenas guarda en destino la cadena
// formada por todas las cadenas separadas por el delimitador. Asumir que destino tiene espacio
// suficiente. Ejemplo:
// char *cadenas[] = { "2021", "04", "05" };
// char s[16];
// join(s, '-', cadenas, 3);
// // s contiene "2021-04-05"


#include <stdio.h>
#include <assert.h>

#include <string.h>

void join(char destino[], char delimitador, char *cadenas[], int n) {
    // HACER: implementar la funcion

    int contador = 0;
    
    for (int i = 0; i < n; i++) {

        int j = 0;

        while (cadenas[i][j] != '\0') {

            destino[contador] = cadenas[i][j];

            contador++;

            j++;
        }

        if (i < n-1) {

            destino[contador] = delimitador;

            contador++;

        }
    
    }

    destino[contador] = '\0';
    
}

int main(void) {
    char *cadenas[] = { "2021", "04", "05" };
    char s[16];
    join(s, '-', cadenas, 3);
    assert(!strcmp(s, "2021-04-05"));

    // OPCIONAL: pruebas adicionales

    printf("%s: OK\n", __FILE__);
    return 0;
}

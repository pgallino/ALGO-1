#include <stdio.h>
#include <assert.h>
#include <string.h>

// HACER: implementar la funcion
void intercalar(const char *s1, const char *s2, char *dest) {

    int largo1 = strlen(s1);
    int largo2 = strlen(s2);

    if (largo1 > largo2) {

        int numero = (largo2 * 2);

        for (int i = 0; i < numero; i++) {

            if (i%2 == 0) {
                dest[i] = s1[i/2];
            } else if (i%2 != 0) {
                dest[i] = s2[(i-1)/2];
            }
        }

        for (int i = numero; s1[i-largo2] !='\0'; i++) {

            dest[i] = s1[i-largo2];
        }

        dest[largo1+largo2] = '\0';

    } else if (largo1 < largo2) {

        int numero = (largo1 * 2) - 1;

        for (int i = 0; i < numero; i++) {

            if (i%2 == 0) {
                dest[i] = s1[i/2];
            } else if (i%2 != 0) {
                dest[i] = s2[(i-1)/2];
            }
        }

        for (int i = numero; s2[i-largo1] != '\0'; i++) {

            dest[i] = s2[i-largo1];
        }
        
        dest[largo1+largo2] = '\0';


    } else {

        for (int i=0; i < largo1 * 2; i++) {

            if (i%2 == 0) {
                dest[i] = s1[i/2];
            } else if (i%2 != 0) {
                dest[i] = s2[(i-1)/2];
            }
        }

        dest[largo1 * 2] = '\0';
    }

    printf("%s\n", dest);
    
}

int main(void) {
    char dest[30];
    intercalar("hola", "", dest);

    assert(strcmp(dest, "hola") == 0);

    // OPCIONAL: Pruebas adicionales. Sugerencias:
    // - una cadena vacía
    // - ambas cadenas vacías

    printf("%s: OK\n", __FILE__);
    return 0;
}

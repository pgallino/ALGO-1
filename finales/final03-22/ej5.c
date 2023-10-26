#include <stdio.h>
#include <assert.h>
#include <string.h>

// HACER: implementar la funcion
void borrar_espacios_consecutivos(char s[]) {

    int contador = 0;
    int largo = strlen(s);

    if (strlen(s) > 1) {
        for (int i = 1; s[i] != '\0';i++) {

        if (s[i] == ' ' && s[i-1] == ' ') {
            contador++;
        }

        s[i-contador] = s[i];
    }

    s[largo - contador] = '\0';

    printf("%s", s);

    }
}


int main(void) {
    char s[] = "A otro    perro con   ese  hueso";
    borrar_espacios_consecutivos(s);
    assert(!strcmp(s, "A otro perro con ese hueso"));

    // OPCIONAL: Pruebas adicionales. Sugerencias:
    // - una cadena vacía
    // - una cadena que contiene solo espacios

    printf("%s: OK\n", __FILE__);
    return 0;
}

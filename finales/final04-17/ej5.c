#include <stdio.h>
#include <assert.h>
#include <string.h>

int buscar(const char *aguja, const char *pajar) {
    // HACER: implementar la funcion
    // Solo se permite utilizar la función `strlen` de la biblioteca estándar de C.
    int largo = strlen(pajar);
    int largo2 = strlen(aguja);
    int j = 1;
    for (int i=0; i < largo; i++) {
        if (pajar[i] == aguja[0]) {
            while (pajar[i + j] == aguja[j]) {
                j++;
            }
            if (j == largo2) {
                return i;
            }
        }
    }

    return -1;

}

int main(void) {
    assert(buscar("def", "abcdefhijk abcdefhijk") == 3);

    // OPCIONAL: pruebas adicionales

    printf("%s: OK\n", __FILE__);
    return 0;
}

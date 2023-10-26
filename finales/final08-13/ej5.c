#include <stdio.h>
#include <assert.h>
#include <string.h>
#include <ctype.h>

void title_case(char s[]) {
    // HACER: implementar la funcion

    if (isalpha(s[0]) == 0) {
        s[0] = toupper(s[0]);}

    for (int i = 1; s[i] != '\0'; i++){

        if (s[i-1] == ' ') {

            s[i] = toupper(s[i]);

        } else if (s[i-1] != ' ') {

            s[i] = tolower(s[i]);
        }
    }
}

int main(void) {
    char s[] = "HoLa QuE tAl";
    title_case(s);
    assert(!strcmp(s, "Hola Que Tal"));

    // OPCIONAL: pruebas adicionales

    printf("%s: OK\n", __FILE__);
    return 0;
}

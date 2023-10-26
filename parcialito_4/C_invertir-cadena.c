#include <stdio.h>

void invertir(char *s) {
    int len = 0;
    
    for (int i = 0; s[i] != '\0'; i++) {
        len += 1;
    }

    for (int n = 0; n < (len / 2); n++) {
        char aux = s[n];
        s[n] = s[len - 1 - n];
        s[len -1 - n] = aux;
    }
}

char s[] = "hola";

int main() {
    printf("%s \n", s);
  invertir(s);
  printf("%s \n", s);
  return 0;
}
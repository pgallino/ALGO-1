// Implementar la función unsigned int strlen(const char *s) que devuelve la
// longitud de la cadena s (sin contar el último caracter '\0'). La función se puede escribir estar en forma iterativa o recursiva.

#include <stdio.h>

int largo(char s[]) {
    int resultado = 0;
    
    for (int i = 0; s[i] != '\0'; i++) {
        resultado += 1;
    }
    return resultado;
}

char s[] = "hola";

int main() {
  printf("%d \n", largo(s));
  return 0;
}
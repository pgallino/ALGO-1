#include <stdio.h>

void copiar(char origen[], char destino[]) {
    

    int largo = 0;
    
    for (int i = 0; origen[i] != '\0'; i++) {
        destino[i] = origen[i];
        largo += 1;
    }
    
    destino[largo] = '\0';
    
}

int main(void) {
    char origen[] = "hola perro";
    char destino[sizeof(origen)];
    copiar(origen, destino);
  printf("copia -> %s\n", destino);
  printf("original -> %s\n", origen);
  printf("tamaño copia: %ld\n", sizeof(destino));
  printf("tamaño original: %ld\n", sizeof(origen));
  return 0;
}
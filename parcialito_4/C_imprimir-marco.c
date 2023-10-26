#include <stdio.h>
void imprimir_enmarcado(char mensaje[]) {
    int largo = 0;
    
    for (int i = 0; mensaje[i] != '\0'; i++) {
        largo += 1;
    }
    char asteriscos[largo + 4];
    for (int n = 0; n != largo + 4; n++) {
        asteriscos[n] = '*';
    }
    printf("%s\n", asteriscos);
    printf("* %s *\n", mensaje);
    printf("%s", asteriscos);

}

int main(void) {
  char mensaje[] = "HOLA HIJOS DE PERRA";
  imprimir_enmarcado(mensaje);
  return 0;
}
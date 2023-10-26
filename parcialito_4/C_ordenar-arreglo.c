#include <stdio.h>
void ordenar(int numeros[], int n) {
    int r = 0;
    while (r != n){
    int i = 0;
    while (i != n - 1) {
        if (numeros[i] > numeros[i + 1]) {
            int aux = numeros[i];
            numeros[i] = numeros[i + 1];
            numeros[i + 1] = aux;
            i++;
        } else {
            i++;
        }
    } 

    r++;

    }  

}

void imprimir_arreglo(int numeros[], int n) {
  for (int i = 0; i < n; i++) {
    printf("%d, ", numeros[i]);
  }
}

int numeros[] = {1,9,3,111,5};

int main(void) {
    imprimir_arreglo(numeros, 5);
    printf("aca termina la original");
    ordenar(numeros, 5);
    imprimir_arreglo(numeros, 5);
  return 0;
}
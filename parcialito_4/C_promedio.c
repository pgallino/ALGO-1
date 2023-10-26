#include <stdio.h>

float promedio(float numeros[], int n) {
    float resultado = 0;
    for (int i = 0; i != n; i++) {
        resultado += numeros[i];
    }
    return resultado / n;
}


float numeros[] = {1,2,3,111,5};

int main(void) {
  printf("%f \n", promedio(numeros, 5));
  return 0;
}
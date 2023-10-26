#include <stdio.h>
#include <assert.h>
#include <string.h>

void ordenar_seleccion(int numeros[], int n) {
    // HACER: implementar la funcion

    int p;
    int minimo;

    if (n > 1) { //verifico que n sea mayor a 1 ya que no hace falta ordenar una lista vacia o de un elemento.

        for (int i = 0; i < n; i++) {

            minimo = numeros[i];
            p = i;

            for (int j = i; j < n; j++) {

                if (minimo >= numeros[j]) {
                    minimo = numeros[j];
                    p = j;

                }
            
            }

            if (minimo != numeros[i]) {

                int intercambiable = numeros[i];

                numeros[i] = minimo;
                numeros[p] = intercambiable;
            }

        }

    }

}

void imprimir_arreglo(int numeros[], int n) { //imprimo el arreglo para verlo por pantalla
  for (int i = 0; i < n; i++) {
    printf("%d, ", numeros[i]);
  }
}

int main(int argc, char *argv[]) {
    int numeros[] =  {4, 8, 2, 6, 5, 4, 2, 1};

    imprimir_arreglo(numeros,8);   //printeo el arreglo sin ordenar
    printf("\n");
    ordenar_seleccion(numeros, 8); //ordeno
    imprimir_arreglo(numeros, 8); //printeo el arreglo ordenado

    int ordenado[] = {1, 2, 2, 4, 4, 5, 6, 8};
    // memcmp compara los dos arreglos y devuelve 0 si son iguales
    assert(memcmp(numeros, ordenado, 8 * sizeof(int)) == 0);

    // OPCIONAL: pruebas adicionales

    printf("%s: OK\n", __FILE__);
    return 0;
}



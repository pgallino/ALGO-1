// Ejercicio 186 c

// Implementar en C la función potencia(), que recibe la base (número entero) y el exponente (número entero no negativo) 

// y devuelva el resultado de elevar la base al exponente. 

// Nota: no pueden incluir bibliotecas para resolver la potencia, por lo que la funcion math.pow no está disponible para usar.

#include <stdio.h>

int potencia(int n, int e) {

    int resultado = 1;

    for (int i = 0; i < e; i++) {

        resultado *= n;
    }

    return resultado;

}

int main(void) {
    printf("%d", potencia(2,2));
    return 0;
}
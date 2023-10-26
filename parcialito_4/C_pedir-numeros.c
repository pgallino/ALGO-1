#include <stdio.h>
#include <stdlib.h>

// Escribir un programa en C que le pida al usuario que ingrese números del 0 al 9. Repetir este proceso hasta que el usuario ingresa -1. 7

// Luego, mostrar por pantalla cuantas veces ingresó cada número.

// Ayuda: usar un arreglo con las posiciones del 0 al 9 como diccionario.

// Ejemplo de la ejecución:

void pedir_numeros() {
    int numeros[] = {0,0,0,0,0,0,0,0,0,0};
    char numero[5];
    int valor;
    do {
        printf("Ingrese un numero del 0 al 9: ");
        fgets(numero,4,stdin);
        valor = atoi(numero);;
        if (valor > -1 && valor < 10) {
            numeros[valor] += 1;
            printf("la lista tiene %d", numeros[valor]);
            printf(" valor es: %d\n", valor);
        }
    } while (valor != -1);

    for (int i = 0; i <= 9; i++) {
        printf("El numero %d se repite %d veces\n", i, numeros[i]);
    }
}

void pedir_numeros_feo() {
    int cant_1 = 0;
    int cant_2 = 0;
    int cant_3 = 0;
    int cant_4 = 0;
    int cant_5 = 0;
    int cant_6 = 0;
    int cant_7 = 0;
    int cant_8 = 0;
    int cant_9 = 0;
    int cant_0 = 0;
    char numero[5];
    int valor = 0;
    
    do {
        printf("Ingrese un numero del 0 al 9: ");
        fgets(numero,4,stdin);
        valor = atoi(numero);
        printf(" valor es: %d\n", valor);

        switch (valor) {
            case 0:
            cant_0++;
            break;
            case 1:
            cant_1++;
            break;
            case 2:
            cant_2++;
            break;
            case 3:
            cant_3++;
            break;
            case 4:
            cant_4++;
            break;
            case 5:
            cant_5++;
            break;
            case 6:
            cant_6++;
            break;
            case 7:
            cant_7++;
            break;
            case 8:
            cant_8++;
            break;
            case 9:
            cant_9++;
            break;
        }

    } while (valor != -1);

    printf("El numero 0 se repite %d veces\n", cant_0);
    printf("El numero 1 se repite %d veces\n", cant_1);
    printf("El numero 2 se repite %d veces\n", cant_2);
    printf("El numero 3 se repite %d veces\n", cant_3);
    printf("El numero 4 se repite %d veces\n", cant_4);
    printf("El numero 5 se repite %d veces\n", cant_5);
    printf("El numero 6 se repite %d veces\n", cant_6);
    printf("El numero 7 se repite %d veces\n", cant_7);
    printf("El numero 8 se repite %d veces\n", cant_8);
    printf("El numero 9 se repite %d veces\n", cant_9);
    
}

int main(void) {
    pedir_numeros();
    return 0;
}

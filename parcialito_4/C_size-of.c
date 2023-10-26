//Usando las funciones printf y sizeof, escribir un programa que imprima el
// tamaño en bytes de cada uno de los siguientes tipos: bool, char, short, int, long, float, double,
// bool*, char*, short*, int*, long*, float*, double*.

// El programa debe mostrar la información con el siguiente formato:

// bool: 1
// char: 1
// short: 2
// . . .

#include <stdio.h>
#include <stdbool.h>

int main() {
    printf("bool: %ld\n", sizeof(bool));
    printf("char: %ld\n", sizeof(char));
    printf("short: %ld\n", sizeof(short));
    printf("int: %ld\n", sizeof(int));
    printf("long: %ld\n", sizeof(long));
    printf("float: %ld\n", sizeof(float));
    printf("double: %ld\n", sizeof(double));
    printf("bool*: %ld\n", sizeof(bool*));
    printf("char*: %ld\n", sizeof(char*));
    printf("short*: %ld\n", sizeof(short*));
    printf("int*: %ld\n", sizeof(int*));
    printf("long*: %ld\n", sizeof(long*));
    printf("float*: %ld\n", sizeof(float*));
    printf("double*: %ld\n", sizeof(double*));
    return 0;
}
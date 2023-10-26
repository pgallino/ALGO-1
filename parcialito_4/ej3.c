// 3. Escribir en C una función que reciba un número secreto `n` (de tipo `int`) y le
// pregunte un número al usuario. Si el número ingresado es distinto a `n`, debe
// indicarle si es mayor o menor y volver a pedirle otro número. Si es igual, debe
// felicitar al usuario, mostrar en cuántos intentos adivinó y devolver dicha cantidad.


// Completar la siguiente funcion

#include <stdio.h>
#include <stdlib.h>

void pedir_numero_secreto(int secreto) {

    char numero[5];
    int valor;

    do {

        printf("Ingrese un número ");
        fgets(numero,4,stdin);
        valor = atoi(numero);
        if (valor > secreto) {

            printf("el numero secreto es menor\n");

        } else if (valor < secreto) {

            printf("el numero secreto es mayor\n");
        
        }

    
    } while (valor != secreto);

    printf("FELICITACIONES");

}


int main() {
    int n = 15;
    pedir_numero_secreto(n);
    return 0;
}

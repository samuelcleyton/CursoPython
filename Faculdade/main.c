/*
1° Algoritmo: para o primeiro algoritmo, você deverá elaborar o algoritmo que o usuário informe a sua idade 
e caso a idade seja maior ou igual a 18 incluir a mensagem “Maior de idade” e caso contrário “Menor de idade”.
*/

#include <stdio.h>

int main() {
    int idade;
    printf("Digite sua idade: ");
    scanf("%d", &idade);

    if (idade >= 18) {
        printf("Maior de idade\n");
    } else {
        printf("Menor de idade\n");
    }

    return 0;
}

#include <stdio.h>

int main(){

    int n,varhelp;

    scanf("%d",&n);

    printf("%d\n",n);
    printf("%d nota(s) de R$ 100,00\n", n/100);
    varhelp = n%100;

    printf("%d nota(s) de R$ 50,00\n", varhelp/50);
    varhelp = varhelp%50;

    printf("%d nota(s) de R$ 20,00\n", varhelp/20);
    varhelp = varhelp%20;

    printf("%d nota(s) de R$ 10,00\n", varhelp/10);
    varhelp = varhelp%10;

    printf("%d nota(s) de R$ 5,00\n", varhelp/5);
    varhelp = varhelp%5;

    printf("%d nota(s) de R$ 2,00\n", varhelp/2);
    varhelp = varhelp%2;

    printf("%d nota(s) de R$ 1,00\n", varhelp/1);


    return 0;
}
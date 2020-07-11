#include <stdio.h>
#include <math.h>

int main(){

    float n;
    int varhelp;

    scanf("%d",&n);

    printf("NOTAS:\n");
    printf("%d nota(s) de R$ 100,00\n", n/100);
    varhelp = fmod(n,100);
    printf("%d nota(s) de R$ 50,00\n", varhelp/50);
    varhelp = fmod(varhelp,50);
    printf("%d nota(s) de R$ 20,00\n", varhelp/20);
    varhelp = fmod(varhelp,20);
    printf("%d nota(s) de R$ 10,00\n", varhelp/10);
    varhelp = fmod(varhelp,10);
    printf("%d nota(s) de R$ 5,00\n", varhelp/5);
    varhelp = fmod(varhelp,5);
    printf("%d nota(s) de R$ 2,00\n", varhelp/2);
    printf("MOEDAS\n");
    varhelp = fmod(varhelp,2);
    printf("%d moeda(s) de R$ 1,00\n", varhelp/1);
    varhelp= fmod(varhelp,1.00);
    printf("%d moeda(s) de R$ 0.50\n", varhelp/0.50);
    varhelp=fmod(varhelp,0.50);
    printf("%d moeda(s) de R$ 0.25\n", varhelp/0.25);
    varhelp=fmod(varhelp,0.10);
    printf("%d moeda(s) de R$ 0.10\n", varhelp/0.10);
    varhelp=fmod(varhelp,0.05);
    printf("%d moeda(s) de R$ 0.05\n", varhelp/0.05);
    varhelp=fmod(varhelp,0.01);
    printf("%d moeda(s) de R$ 0.01\n", varhelp/0.01);







    return 0;
}
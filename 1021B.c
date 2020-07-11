#include <stdio.h>

int main(){
    int n1,n2,varhelp;

    scanf("%d.%d",&n1,&n2);

    varhelp = n1*100+n2;
    printf("NOTAS:\n");
    printf("%d nota(s) de R$ 100.00\n", varhelp/10000);
    varhelp = varhelp%10000;
    printf("%d nota(s) de R$ 50.00\n", varhelp/5000);
    varhelp = varhelp%5000;
    printf("%d nota(s) de R$ 20.00\n", varhelp/2000);
    varhelp = varhelp%2000;
    printf("%d nota(s) de R$ 10.00\n", varhelp/1000);
    varhelp = varhelp%1000;
    printf("%d nota(s) de R$ 5.00\n", varhelp/500);
    varhelp = varhelp%500;
    printf("%d nota(s) de R$ 2.00\n", varhelp/200);
    varhelp = varhelp%200;
    printf("MOEDAS:\n");
    printf("%d moeda(s) de R$ 1.00\n", varhelp/100);
    varhelp= varhelp%100;
    printf("%d moeda(s) de R$ 0.50\n", varhelp/50);
    varhelp=varhelp%50;
    printf("%d moeda(s) de R$ 0.25\n", varhelp/25);
    varhelp=varhelp%25;
    printf("%d moeda(s) de R$ 0.10\n", varhelp/10);
    varhelp=varhelp%10;
    printf("%d moeda(s) de R$ 0.05\n", varhelp/5);
    varhelp=varhelp%5;
    printf("%d moeda(s) de R$ 0.01\n", varhelp);



    return 0;
}
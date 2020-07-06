#include <stdio.h>

int main(){

    int employe, perhour;
    float salary, total;

    scanf("%d",&employe);
    scanf("%d", &perhour);
    scanf("%f", &salary);

    total = salary*perhour;

    printf("NUMBER = %d\n",employe);
    printf("SALARY = U$ %.2f\n", total);

    return 0;
}
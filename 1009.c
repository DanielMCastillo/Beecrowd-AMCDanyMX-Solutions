#include <stdio.h>

int main(){

    char name;
    double salary, product, descount,total;

    scanf("%s",&name);
    scanf("%lf", &salary);
    scanf("%lf", &product);

    descount = product*0.15;
    total = descount + salary;

    printf("TOTAL = R$ %.2lf\n", total);

    return 0;
}
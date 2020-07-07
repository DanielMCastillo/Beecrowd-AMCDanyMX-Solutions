#include <stdio.h>

int main(){

    int x,y;
    double z,res;

    scanf("%d%d%lf",&x,&y,&z);
    res = y*z;
    scanf("%d%d%lf",&x,&y,&z);
    res+=y*z;


    printf("VALOR A PAGAR: R$ %.2lf\n", res);


    return 0;
}